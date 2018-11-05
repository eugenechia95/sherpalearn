from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import SignUpForm

from django.contrib.auth.decorators import login_required, permission_required  
from django.contrib.auth import views as auth_views 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def home(request):
    if request.method == 'POST':
            if request.POST.get('email'):
                country = request.POST.get('country')
                persontype = request.POST.get('persontype')
                email = request.POST.get('email')
                
                Subscribe.objects.create(email=email, country=country, persontype=persontype)
                
            if request.POST.get('email1'):
                name = request.POST.get('name')
                country1 = request.POST.get('country1')
                number = request.POST.get('number')
                email1 = request.POST.get('email1')
                enquiries = request.POST.get('enquiries')
                
                Enquiry.objects.create(name=name, email=email1, country=country1, 
                                       number=number, enquiries=enquiries)

    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.is_superuser = True
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def checkauth(request):
    if request.user.is_authenticated:
        #your logic here
        return redirect("users/")# or your url name
    

@login_required
def users(request):
    worksheets=Worksheet.objects.all()
    newworksheets = Worksheet.objects.filter(status='U')
    subjects=Subject.objects.all()
    topics=Topic.objects.all()
    assignedws = Worksheet.objects.filter(status='A')
    
    # Render the HTML template users.html with the data in the context variable
    return render(
        request,
        'users.html',context={"worksheets":worksheets, "newws":newworksheets,"subjects":subjects, "topics":topics, "assignedws":assignedws})
    
