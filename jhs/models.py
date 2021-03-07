from django.db import models


CHOICES = (
    ('メーカー系', 'メーカー系'),
    ('独立系', '独立系'),
    ('ユーザー系', 'ユーザー系')
)


class Company(models.Model):
    """会社"""
    name = models.CharField('会社名(必須)', max_length=30)
    strengths = models.TextField('強味', max_length=255, blank=True)
    interest_level = models.FloatField('興味度(必須)', max_length=15,)
    working_times = models.CharField(
        '出勤・退勤(後から方式変えるかもだけど、今は00:00~00:00)', max_length=15, blank=True)
    welfare_benefits = models.TextField(
        '福利厚生(後から方式変えるから、[, ]で区切る。(タグとか検索機能つけたい))', max_length=150, blank=True)
    system = models.CharField('系統', max_length=5, choices=CHOICES, blank=True)
    impression = models.TextField('感想', max_length=50, blank=True)
    company_url = models.CharField('会社URL(必須)', max_length=100)
    recruitment_site_url = models.CharField('採用サイトURL(必須)', max_length=100)
    my_page_url = models.CharField('マイページURL', max_length=100, blank=True)
    my_page_id = models.CharField('マイページID', max_length=20, blank=True)
    my_page_password = models.CharField(
        'マイページパスワード', max_length=20, blank=True)
    entered = models.BooleanField('エントリー', default=False)
    entry_sheet = models.BooleanField('ES提出', default=False)

    def __str__(self):
        return self.name
