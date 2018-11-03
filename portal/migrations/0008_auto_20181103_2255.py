# Generated by Django 2.1.2 on 2018-11-03 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_auto_20181103_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_assigned', models.ManyToManyField(to='portal.Profile')),
            ],
        ),
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
        migrations.RenameModel(
            old_name='Worksheets',
            new_name='Worksheet',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='profile_assigned',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='topic',
        ),
        migrations.RenameModel(
            old_name='Subjects',
            new_name='Subject',
        ),
        migrations.RenameModel(
            old_name='Topics',
            new_name='Topic',
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
        migrations.AddField(
            model_name='note',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Subject'),
        ),
        migrations.AddField(
            model_name='note',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Topic'),
        ),
    ]
