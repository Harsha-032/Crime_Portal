from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from crime.models import *



def registerPage(request): 
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        p1=request.POST.get('pass1')

        my_user=User.objects.create_user(uname,email,p1)
        my_user.save()
        return redirect('login')
    return render(request, 'register.html')
    
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user) 
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def report(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        dob = request.POST.get('dob')
        number = request.POST.get('number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')  
        state = request.POST.get('state') 
        pin = request.POST.get('pin')  
        ca = request.POST.get('ca')  
        someone = request.POST.get('someone')    
        cin = request.POST.get('cin')  
        


        send_mail(
        'contact Form',
        f"FirstName: {fname}\nLastname: {lname}\nDateofbirth: {dob}\nEmail: {email}\nPhone Number: {number}\nAddress: {address}\nCity: {city}\nCountry: {country}\nState: {state}\nPin-code: {pin}\nCrime Address: {ca}\nReporting behalf of some one else: {someone}\ncrime/incident: {cin}",
        settings.EMAIL_HOST_USER,
        ['test.dev032@gmail.com'],
        fail_silently=False,
        )
    return render(request, 'reportcrime.html')


@login_required(login_url='login')
def wanted(request):
    Wantedlist = wantedlist.objects.all()
    return render(request, 'wantedlist.html',{'wantedlist':Wantedlist})


@login_required(login_url='login')
def safety(request):
    safety = safe.objects.all()
    return render(request, 'safety.html',{'Safety':safety})