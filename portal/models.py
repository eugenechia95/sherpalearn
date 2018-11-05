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

class Subject(models.Model):
    subject = models.CharField(max_length=64)

    def __str__(self):
        return self.subject

class Topic(models.Model):
    topic = models.CharField(max_length=64)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {}".format(self.subject, self.topic)

class QuestionType(models.Model):
    question_type = models.CharField(max_length=64, primary_key=True)

    def __str__(self):
        return self.question_type

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.CharField(max_length=5096)
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    answer = models.CharField(max_length=5096)
    
    def __str__(self):
        return self.question

class Worksheet(models.Model):
    worksheet_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=75, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True)
    questions = models.ManyToManyField(Question, blank=True)
    profile_assigned = models.ManyToManyField(Profile, blank=True)
    icon = models.ImageField(upload_to= "uploads/worksheetref", max_length=100, null=True, blank=True)

    date_assigned = models.DateField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)

    STATUS = [
        ('U', 'Unassigned'),
        ('A', 'Assigned'),
        ('O', 'Overdue'),
        ('C', 'Completed')
    ]
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default='U',
    )

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=75, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    profile_assigned = models.ManyToManyField(Profile)
    
    def __str__(self):
        return self.title
    
class Subscribe(models.Model):
        
    country = models.CharField(max_length=200, null=True, blank=True)
    persontype = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.email
    
class Enquiry(models.Model):
        
    name = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    number = models.IntegerField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    enquiries = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    

