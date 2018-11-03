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
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE, null=True, blank=True)
    account_type = models.ForeignKey("AccountType", on_delete=models.CASCADE, null=True, blank=True)
    connections = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Subjects(models.Model):
    subject = models.CharField(max_length=64)

    def __str__(self):
        return self.subject

class Topics(models.Model):
    topic = models.CharField(max_length=64)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {}".format(self.subject, self.topic)

class QuestionType(models.Model):
    question_type = models.CharField(max_length=64, primary_key=True)

    def __str__(self):
        return self.question_type

class Questions(models.Model):
    question_id = models.AutoField(primary_key=True)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    question = models.CharField(max_length=5096)
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    answer = models.CharField(max_length=5096)

class Worksheets(models.Model):
    worksheet_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Questions)
    profile_assigned = models.ManyToManyField(Profile)

    date_assigned = models.DateField(auto_now_add=True)
    due_date = models.DateTimeField()

    STATUS = [
        ('A', 'Assigned'),
        ('O', 'Overdue'),
        ('C', 'Completed')
    ]
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default='A',
    )

    def __str__(self):
        return "Worksheet", self.worksheet_id

class Notes(models.Model):
    
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    profile_assigned = models.ManyToManyField(Profile)




    