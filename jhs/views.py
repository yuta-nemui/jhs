from django.shortcuts import render, get_object_or_404, redirect
from jhs.models import Company
from jhs.forms import CompanyForm
from django.db.models import Q

# Create your views here.


def company_list(request):
    # print(Company.objects.get(id=1).__dict__)
    """会社情報の一覧"""
    # return HttpResponse('会社の一覧')
    form_name = request.GET.get('name')
    form_entered = bool(request.GET.get('entered'))
    form_not_entry = bool(request.GET.get('not_entry'))
    form_system = request.GET.get('system')
    if form_name:
        companies = Company.objects.filter(
            Q(name__icontains=form_name) | Q(interest_level__icontains=form_name))
    else:
        companies = Company.objects.all().order_by('id')
    if form_system is not None:
        companies = companies.filter(
            Q(system=form_system)
        )
    companies = companies.filter(
        Q(entered=form_entered) | Q(entered=not form_not_entry))
    # companies = companies.order_by('entered')
    return render(request,
                  'jhs/company_list.html',     # 使用するテンプレート
                  {'companies': companies, "systems": Company.CHOICE})         # テンプレートに渡すデータ


def company_edit(request, company_id=None):
    """会社情報の編集"""
    # return HttpResponse('会社の編集')
    if company_id:   # company_id が指定されている (修正時)
        company = get_object_or_404(Company, pk=company_id)
    else:         # company_id が指定されていない (追加時)
        company = Company()

    if request.method == 'POST':
        # POST された request データからフォームを作成
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():    # フォームのバリデーション
            company = form.save(commit=False)
            company.save()
            return redirect('jhs:company_list')
    else:    # GET の時
        form = CompanyForm(instance=company)  # company インスタンスからフォームを作成

    return render(request, 'jhs/company_edit.html', dict(form=form, company_id=company_id))


def company_del(request, company_id):
    """会社情報の削除"""
    # return HttpResponse('会社の削除')
    book = get_object_or_404(Company, pk=company_id)
    book.delete()
    return redirect('jhs:company_list')
