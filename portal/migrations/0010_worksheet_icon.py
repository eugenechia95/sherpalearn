# Generated by Django 2.1.2 on 2018-11-03 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_profile_connections'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksheet',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/worksheetref'),
        ),
    ]
