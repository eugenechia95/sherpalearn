from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import SignUpForm

from django.contrib.auth.decorators import login_required, permission_required  
from django.contrib.auth import views as auth_views 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

import csv


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
        return redirect("beta/")# or your url name
    

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
    
@login_required
def gwoo(request):
    return render(
        request,
        'gwoo.html')
    
@login_required
def circle(request):
    return render(
        request,
        'circle.html')
    
@staff_member_required
def bulk(request):
    users=[]
#    pw = static('pw.csv')
#    
#    with open(pw, 'r') as csvFile:
#        reader = csv.reader(csvFile)
#        next(reader)
#        for row in reader:
#            ls.append(row)
#    csvFile.close()
    userlist = [['yPSqLD', '9jNwTu72'], ['ubUSgs', 'qUnA8sLH'], ['fWqXDU', '9DX3N8BW'], ['fDmbBJ', 'EwZ8QH87'], ['TGYnNC', 'kUXwd2X4'], ['yBZSUp', 'ht6LX8Gw'], ['dqHxdt', 'N7YXahK7'], ['YeJQZY', 'x4UhAyF3'], ['LLZFuv', '98Ux4Rns'], ['yDQGWp', '2Th2u4Vn'], ['pdmvNT', 'h3DWTZFS'], ['ABDHbE', '6UrR8Ck9'], ['ykVJCe', 'C8ArQYqF'], ['Rudzsu', 'YqND9Rqy'], ['VTvwqf', 'aKbnUs5w'], ['KqBQaf', 'jLRS4VPM'], ['TEGpvu', 'Mqs9JaTn'], ['SdKLCB', 'ENQ9FDXr'], ['QpFrum', 'C28rQWgw'], ['PYkdNA', 'FWpa2f35'], ['sHjGKD', 'N3UPDhza'], ['YUxdHp', '7US7MRWs'], ['cRxdHv', '3cgt8dGB'], ['DLcWXH', 'dU9R9B7J'], ['ZvXYEg', 'tfdGhqa5'], ['YSYcrK', 'd9m4et8C'], ['sHzGfq', 'r2s2PwuR'], ['edYqYt', 'cqDEDS69'], ['eKPhXe', 'fyQcJQ89'], ['XWGAFr', 'E2hX59Tb'], ['XDAeKM', '2c4Qcj87'], ['cDbLSM', 'UjRKDsZ2'], ['quWhZF', 'qdRQRsd7'], ['YDSnDC', 'Ur52QjXz'], ['DftJeF', '2MDj4mVu'], ['GENXLZ', 'zBd26MXj'], ['kCzmqg', '2xSXvB9W'], ['YBGsdP', 'L7y2BL73'], ['sKPwgX', 'ZpNeYBV3'], ['JTHAmH', '2gA82BDP'], ['YDFaru', 'PY4L3pKf'], ['XqTKQL', 'pX8dzEPV'], ['LBKUJZ', 'Z85dETxq'], ['hSgkGW', 'DMjWLp8K'], ['XFQFZL', '9XN54yWk'], ['TNnAKP', 'KZ8UwSLr'], ['yVmvjJ', '8SEYZc35'], ['UfykZD', 'rByfZs2K'], ['XdHRXG', '682YDRJd'], ['VJpYgZ', 'mWqd3Jyh'], ['ZRwRSD', 'F4nRNcaY'], ['yAKPCb', 'XMYw7Lu5'], ['tVHcbV', 'aM9wbnrg'], ['TUdvTT', 'x8YY5zkt'], ['qtsMPG', '4aPQ3FjR'], ['sbVNVL', 'm5AYyHNv'], ['jXPUFX', 'P3dKAf5r'], ['PPDCDL', '5BFTUYF5'], ['WwxMkX', 'CSwbdNw7'], ['CGBhYm', 'cC7dDDW7'], ['ruCfQC', 'TdCJN5c7'], ['vUSPAd', 'RaRLWgA6'], ['BEdvpG', 'f55SRZKu'], ['whrZCq', 'SVCSF8Ma'], ['fZqDVn', 'ELgXkDK9'], ['FswfvQ', 'DZ88zuDD'], ['ZNZrfK', '9x89VjAN'], ['uHCWfL', 's8wCw52E'], ['bTAgGn', 'aLS5Thwq'], ['nPaSaA', 'ab8GKwgB'], ['kmeFHF', 'BB4EQUV6'], ['BGxrFT', '2bh3ndP7'], ['XXasjv', 'EGXf6sD9'], ['USWCQu', 'tEBxXd66'], ['aGWZSr', '6ydAAC3G'], ['jqApDb', 'gpEQV3Bs'], ['PtnAqQ', '8VD9pkJ5'], ['vGGUVb', 'yESRZeQ9'], ['sQtKNk', 'ajXHKL8q'], ['jZXhUu', '7m4JAXCa'], ['PXkpuR', 'BDMU9wj6'], ['XdwQds', 'NT8YW5F3'], ['eZHfDR', 'L3Hf7Bda'], ['dHGavV', 'WG99tesF'], ['gqWCwB', 'sZ47SdMK'], ['TFUsGR', '47YNeu6t'], ['JMZRQe', 'DnC6PrK6'], ['DYtQkK', 'YWD2EXMd'], ['MVbWLu', 'JCc3g6TJ'], ['SNdXeG', 'DZaJ884P'], ['RTNqUe', 'jm7xtRtR'], ['qGsLJM', 'JAEF6xRH'], ['DNkdKC', 'xG8Psnew'], ['MRTtVG', 'mK4QKvLf'], ['mrWHCg', '5BfStdFn'], ['aHMDbG', 'TxDw4d5L'], ['zHcCGy', 'r3dEvYVS'], ['DXJSZD', 'AP7d34Vf'], ['TLYXfw', '3sNxBaXa'], ['DNEYwK', '2ZHzgbQv']]
    
    for i in range(99):
        user = User(
                    username=userlist[i][0],
                    password= make_password(userlist[i][1], salt=None, hasher='default'),
                    is_active=True)
        users.append(user)
     
    User.objects.bulk_create(users)
    for eachuser in users:
        Profile.objects.create(user=eachuser)
    
    return render(request, 'bulkcreate.html')

@login_required
def beta(request):
    current_user = request.user
    if not current_user.email:
        return HttpResponseRedirect(reverse('updatedetails'))
    return render(
        request,
        'betawelcome.html')
    
@login_required
def updatedetails(request):
    current_user = request.user
    current_profile = (Profile.objects.filter(user=current_user))[0]
    if request.method == 'POST':
        current_user.username = request.POST.get('username')
        current_user.email = request.POST.get('Email1')
        current_user.first_name = request.POST.get('firstname')
        current_user.last_name = request.POST.get('lastname')
        current_profile.country = request.POST.get('country')
        account_type = request.POST.get('persontype')
        allaccounttypes = AccountType.objects.all()
        for i in allaccounttypes:
            if account_type == i.account_type:
                current_profile.account_type = i
        current_user.save()
        current_profile.save()
        return HttpResponseRedirect(reverse('pwreset'))          
    return render(
        request,
        'updatedetails.html')
    
@login_required    
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect(reverse('beta')) 
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_reset.html', {
        'form': form
    })