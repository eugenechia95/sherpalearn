from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass

@admin.register(QuestionType)
class QuestionTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Worksheet)
class WorksheetAdmin(admin.ModelAdmin):
    pass

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    pass

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    pass

@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    pass