# Generated by Django 2.1.2 on 2018-10-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20181028_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounttype',
            name='account_type',
            field=models.CharField(max_length=12),
        ),
    ]
