# Generated by Django 3.1.7 on 2021-03-05 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jhs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='classification',
        ),
    ]
