# Generated by Django 3.1.7 on 2021-03-05 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='会社名(必須)')),
                ('strengths', models.TextField(blank=True, max_length=255, verbose_name='強味')),
                ('classification', models.CharField(blank=True, max_length=5, verbose_name='分類')),
                ('interest_level', models.FloatField(max_length=15, verbose_name='興味度(必須)')),
                ('system', models.CharField(blank=True, max_length=5, verbose_name='系統')),
                ('company_url', models.CharField(max_length=100, verbose_name='会社URL(必須)')),
                ('recruitment_site_url', models.CharField(max_length=100, verbose_name='採用サイトURL(必須)')),
                ('my_page_url', models.CharField(blank=True, max_length=100, verbose_name='マイページURL')),
                ('my_page_id', models.CharField(blank=True, max_length=20, verbose_name='マイページID')),
                ('my_page_password', models.CharField(blank=True, max_length=20, verbose_name='マイページパスワード')),
                ('entered', models.BooleanField(default=False, verbose_name='エントリー')),
            ],
        ),
    ]
