# Generated by Django 3.0.2 on 2020-01-11 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterForm', '0002_auto_20200111_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerform',
            name='Enterprise',
            field=models.TextField(),
        ),
    ]
