# Generated by Django 2.1.2 on 2018-11-03 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_auto_20181103_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worksheet',
            name='profile_assigned',
            field=models.ManyToManyField(blank=True, to='portal.Profile'),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='questions',
            field=models.ManyToManyField(blank=True, to='portal.Question'),
        ),
    ]
