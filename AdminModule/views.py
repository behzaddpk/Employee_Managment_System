from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser
from PartnerModule.forms import *
from TeamLeader.models import TeamLeader
from .forms import *
from coordinator.models import Coordinator
from django.conf import settings
from django.core.mail import send_mail
import uuid
import sendgrid
from sendgrid.helpers.mail import *


# Create your views here.


def LOGIN(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'),)
        if user:
            #user is authenticated
            login(request, user)
            user_type = user.Designate
            if user_type == '1':
                return redirect('dashboard')
            elif user_type == '2':
                partner = Partner.objects.filter(user=user)
                
                if not user.partner.is_verified:
                    messages.warning(request, 'Your account is not verified yet.')
                    return redirect('login')
                else:
                    return redirect('PartnerDashboard')
            elif user_type == '3':
                coordinator = Coordinator.objects.filter(user=user)
                if not user.coordinator.is_verified:
                    messages.warning(request, 'Your account is not verified yet.')
                    return redirect('login')
                else:
                    return redirect('CoordinatorDashboard') 
            elif user_type == '4':
                return redirect('TeamLeaderDashboard') 
            elif user_type == '5':
                return redirect('WriterDashboard') 
            elif user_type == '6':
                return redirect('MemberDashboard') 
    return render(request, 'login.html')

    

def LOGOUT(request):
    logout(request)
    return redirect('login')


def StaffRegistration(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            team_captain = form.cleaned_data['team_captain']
            designate = form.cleaned_data['designate']
            password = form.cleaned_data['password']
            
            if CustomUser.objects.filter(username=username).exists():
                messages.warning(request, 'Username is already taken')

            if CustomUser.objects.filter(email=email).exists():
                messages.warning(request, 'Email is already taken')


            else:
                user = CustomUser(
                    first_name=first_name, 
                    last_name=last_name, 
                    username=username, 
                    email=email, 
                    Designate=designate, 
                    )
                user.set_password(password)
                user.save()

                auth_token = str(uuid.uuid4())

                if designate == '1':  # Admin
                    user.is_superuser = True
                    user.is_staff = True
                    user.team_captain = team_captain
                    user.auth_token = auth_token
                    user.save()

                elif designate == '2':  # Partner
                    partner = Partner(user=user, team_captain=team_captain, auth_token=auth_token)
                    partner.save()
                elif designate == '3':  # Coordinator
                    coordinator = Coordinator(user=user, team_captain=team_captain, auth_token=auth_token)
                    coordinator.save()
                elif designate == '4':  # Coordinator
                    coordinator = TeamLeader(user=user, team=team_captain, auth_token=auth_token)
                    coordinator.save()

                send_mail(email, auth_token)
                messages.success(request, 'Staff is registered')
                form = CustomUserForm() 
    else:
        form = CustomUserForm()
    
    return render(request, 'StaffRegisteration.html', {"form": form})


def send_mail(email, token):
    subject = 'Your Account Needs to be Verified'
    message = f'Hi, please click the link to verify your account: http://127.0.0.1:8000/verify/{token}'
    email_from = settings.DEFAULT_FROM_EMAIL

    # Create a SendGrid message object
    message = Mail(
        from_email=email_from,
        to_emails=email,
        subject=subject,
        plain_text_content=message
    )

    # Use SendGrid to send the email
    sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
    response = sg.send(message)
    print(response.status_code)

def verify_partner(request, auth_token):
    try:
        profile_obj = Partner.objects.filter(auth_token=auth_token).first()
        print(profile_obj)
        if profile_obj:
            if profile_obj.is_varified:
                messages.success(request, 'Account is already verified')
                return redirect('login')
            else:
                profile_obj.is_varified = True
                profile_obj.save()
                messages.success(request, 'Account has been verified')
                return redirect('login')
        else:
            return HttpResponseRedirect('login')
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/error')
    

def Profile(request):
    return render(request, 'profile.html')
