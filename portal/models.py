from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    account_type = models.CharField(max_length=12)

    def __str__(self):
        return self.account_type

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    account_type = models.ForeignKey("AccountType", on_delete=models.CASCADE, null=True, blank=True)
#    connections = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

