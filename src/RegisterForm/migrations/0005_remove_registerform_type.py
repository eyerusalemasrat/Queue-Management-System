# Generated by Django 3.0.2 on 2020-01-17 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterForm', '0004_auto_20200117_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerform',
            name='type',
        ),
    ]
