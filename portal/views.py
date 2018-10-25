from django.shortcuts import render

# Create your views here.
from .models import *

from django.contrib.auth.decorators import login_required, permission_required   

def home(request):
    return render(request, 'home.html')

@login_required
def checkauth(request):
    if request.user.is_staff:
        #your logic here
        return redirect("allprojects/")# or your url name
    if request.user.is_authenticated:
        #your logic here
        return redirect("users/")# or your url name
    
