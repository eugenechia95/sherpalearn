# Generated by Django 2.1.2 on 2018-11-03 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_auto_20181103_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksheet',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Topic'),
        ),
    ]