from django.db import models


class Company(models.Model):
    """会社"""
    name = models.CharField('会社名(必須)', max_length=30)
    strengths = models.TextField('強味', max_length=255, blank=True)
    interest_level = models.FloatField('興味度(必須)', max_length=15,)
    system = models.CharField('系統', max_length=5, blank=True)
    company_url = models.CharField('会社URL(必須)', max_length=100)
    recruitment_site_url = models.CharField('採用サイトURL(必須)', max_length=100)
    my_page_url = models.CharField('マイページURL', max_length=100, blank=True)
    my_page_id = models.CharField('マイページID', max_length=20, blank=True)
    my_page_password = models.CharField(
        'マイページパスワード', max_length=20, blank=True)
    entered = models.BooleanField('エントリー', default=False)

    CHOICE = ['ユーザー系', '独立系', 'メーカー系']

    def __str__(self):
        return self.name
