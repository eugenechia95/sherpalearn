# Generated by Django 2.1.2 on 2018-12-08 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0022_demo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demo',
            name='impact',
        ),
        migrations.RemoveField(
            model_name='demo',
            name='scope',
        ),
    ]
