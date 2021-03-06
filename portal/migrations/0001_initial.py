# Generated by Django 2.1.2 on 2018-10-27 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('Free', 'Free'), ('Tutor', 'Tutor'), ('Student', 'Student'), ('Parent', 'Parent'), ('Child', 'Child'), ('Self Learner', 'Self Learner')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.AccountType')),
                ('connections', models.ManyToManyField(blank=True, related_name='_profile_connections_+', to='portal.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
