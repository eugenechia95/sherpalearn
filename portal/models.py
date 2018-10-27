from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class AccountType(models.Model):
    TYPES = [
        ('Free', 'Free'),
        ('Tutor', 'Tutor'),
        ('Student', 'Student'),
        ('Parent', 'Parent'),
        ('Child', 'Child'),
        ('Self Learner', 'Self Learner')
    ]
    account_type = models.CharField(max_length=12, choices=TYPES)

    def __str__(self):
        return self.account_type

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.ForeignKey("AccountType", on_delete=models.CASCADE)
    connections = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.user.username

