from django import forms
from django.db.models import fields
from django.forms import ModelForm
from jhs.models import Company


class CompanyForm(ModelForm):
    """会社のフォーム"""
    class Meta:
        model = Company
        fields = list(Company.__dict__.keys())
        # fields = ('name', 'strengths', 'classification', 'interest_level',                    # 現状はこれで大丈夫だけど項目を増やしたらどうなるか分からない
        #           'company_url', 'recruitment_site_url', 'my_page_url', 'system', 'entered')
        fields = tuple(fields[7:-2])

    system = forms.ChoiceField(
        label="系統",
        initial=[1],
        required=False,
        disabled=False,
        choices=[tuple([Company.CHOICE[0], Company.CHOICE[0]]), tuple(
            [Company.CHOICE[1], Company.CHOICE[1]]), tuple([Company.CHOICE[2], Company.CHOICE[2]])],
        widget=forms.RadioSelect(attrs={
            'id': 'system', 'class': 'form-group-input'}))
