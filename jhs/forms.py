from django import forms
from django.db.models import fields
from django.forms import ModelForm
from jhs.models import Company


class CompanyForm(ModelForm):
    """会社のフォーム"""
    class Meta:
        model = Company
        fields = list(Company.__dict__.keys())
        # 何これ…ラジオボタン辞めてプルダウンにしたら生えてきたんだけど…分かるようなわからないような
        fields.remove('get_system_display')
        # fields = ('name', 'strengths', 'interest_level',
        #           'company_url', 'recruitment_site_url', 'my_page_url', 'system', 'entered')
        fields = fields[6:-2]       # 現状はこれで大丈夫だけど項目を増やしたらどうなるか分からない
        widgets = {
            'welfare_benefits': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            'impression': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }

    # system = forms.ChoiceField(
    #     label="系統",
    #     initial=[1],
    #     required=False,
    #     disabled=False,
    #     choices=[tuple([Company.CHOICE[0], Company.CHOICE[0]]), tuple(
    #         [Company.CHOICE[1], Company.CHOICE[1]]), tuple([Company.CHOICE[2], Company.CHOICE[2]])],
    #     widget=forms.RadioSelect(attrs={
    #         'id': 'system', 'class': 'form-group-input'}))
