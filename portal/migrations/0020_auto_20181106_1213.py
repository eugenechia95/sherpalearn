# Generated by Django 2.1.2 on 2018-11-06 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0019_auto_20181105_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
