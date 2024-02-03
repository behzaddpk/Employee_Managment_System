from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import sendgrid
from django.core.mail import send_mail
from django.conf import settings
from sendgrid.helpers.mail import *
import uuid
from writer.models import Writer
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
# from django.forms import inlineformset_factory


# Create your views here.

@login_required
def MemberDashboard(request):
    return render(request, 'MemberDashboard.html')

@login_required()
def TeamMembers(request):
    member = Member.objects.all()
    groups = {}
    if request.method == "POST":
        filter_option = request.POST.get('filter_option')
        mt = request.POST.get('searchmember')

        if mt:
            print(mt)
            member = Member.objects.filter(Q(username__icontains=mt))

        if filter_option == 'team':
            # teams = Team.objects.all()
            member = member.order_by('team')
            groups = {}
            for single in member:
                if not single.team.team_name in groups.keys():
                    groups[single.team.team_name] = []
                groups[single.team.team_name].append(single)
            print(groups[single.team.team_name])
            print(groups)


    return render(request, 'captain/team/TeamMember.html', {'members': member, 'groups': groups})





@login_required()
def AddTeamMember(request):
    if request.method == 'POST':
        teamform = TeamForm(request.POST)
        if teamform.is_valid():
            team_name = teamform.cleaned_data['team_name']
            team = Team(team_name=team_name)
            team.save()
            teamform = TeamForm()
    else:
        teamform = TeamForm()

    if request.method == 'POST':
        designationform = DesignationForm(request.POST)
        if designationform.is_valid():
            designation_name = designationform.cleaned_data['designation']
            designation = Designation(designation=designation_name)
            designation.save()
            designationform = DesignationForm()
    else:
        designationform = DesignationForm()

    if request.method == 'POST':
        team_form = MemberForm(request.POST, request.FILES)
        if team_form.is_valid():
            first_name = team_form.cleaned_data['first_name']
            last_name = team_form.cleaned_data['last_name']
            username = team_form.cleaned_data['username']
            email = team_form.cleaned_data['email']
            team = team_form.cleaned_data['team']
            desginate = team_form.cleaned_data['designate']
            password = team_form.cleaned_data['password']

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
                    Designate = desginate,
                    )
                user.set_password(password)
                user.save()

                auth_token = str(uuid.uuid4())
                
                if desginate == "5":
                    writer = Writer(
                        user=user, 
                        team=team, 
                        auth_token=auth_token
                        )
                    writer.save()
                # send_mail(email, auth_token)
                messages.success(request,'Writer Registered Successfully')
                team_form = MemberForm()


                if desginate == "6":
                    member = Member(
                        user=user, 
                        team=team, 
                        auth_token=auth_token
                        )
                    member.save()
                # send_mail(email, auth_token)
                messages.success(request,'Member Registered Successfully')
                team_form = MemberForm()
    else:
        team_form = MemberForm()


    context = {
        'teamform':teamform, 
        'designation':designationform, 
        'team_form': team_form
    }
            
    return render(request, 'captain/team/AddTeamMember.html', context)




def MemberProfiles(request, slug=None):
    member = None
    profile = None 
    bankdetail = None
    photo = None
    if slug is not None:
        try:
            member = Member.objects.get(user__slug=slug)
            profile = MemberProfile.objects.get(member=member)
            photo = MemberPhoto.objects.get(member=member)
            bankdetail = MemberBankDetail.objects.get(member=member)    
        except Exception as e:
            print(e)
    

    if request.method == 'POST':
        skill_formset = MemberSkillFormSet(request.POST)
        if skill_formset.is_valid():
            # Process the formset data
            for form in skill_formset:

                # Access form.cleaned_data to get the form field values
                skill_name = form.cleaned_data.get('skill')
                experience_years = form.cleaned_data.get('skill_experience')
                # Do something with the form field values
                if form.has_changed():
                    form.instance.member = member  # Assign the member instance to each form
                    form.save()
        
        skill_formset = MemberSkillFormSet()
            
    else:
        skill_formset = MemberSkillFormSet()

    
    if request.method == 'POST':
        experience_formset = ExperienceFormSet(request.POST)
        if experience_formset.is_valid():
            # Process the formset data
            for form in experience_formset:

                # Access form.cleaned_data to get the form field values
                field = form.cleaned_data.get('ExperiencedField')
                year = form.cleaned_data.get('ExperiencedYear')
                # Do something with the form field values
                if form.has_changed():
                    form.instance.member = member  # Assign the member instance to each form
                    form.save()
        
        experience_formset = ExperienceFormSet()
            
    else:
        experience_formset = ExperienceFormSet()



    if request.method == 'POST':
        education_formset = EducationFormset(request.POST)
        if education_formset.is_valid():
            # Process the formset data
            for form in education_formset:

                # Access form.cleaned_data to get the form field values
                field = form.cleaned_data.get('StudyIn')
                year = form.cleaned_data.get('PassingYear')
                # Do something with the form field values
                if form.has_changed():
                    form.instance.member = member  # Assign the member instance to each form
                    form.save()
        
        education_formset = EducationFormset()
            
    else:
        education_formset = EducationFormset()


    skill = MemberSkill.objects.filter(member=member)
    experiences = MemberExperience.objects.filter(member=member)
    education = MemberEducation.objects.filter(member=member)


    context = {
        'member': member,
        'profile': profile,
        'photo':photo,
        'skills': skill,
        'experiences': experiences,
        'educations':education,
        'bankdetail': bankdetail,
        'skill_formset':skill_formset,
        'experience_formset':experience_formset,
        'education_formset': education_formset
    }

    return render(request, 'captain/team/MemberProfile.html', context)


def MemberEvaluations(request):
    teams = Team.objects.filter(member__memberevaluation__isnull=False).distinct()
    staffs = MemberEvaluation.objects.select_related('member').filter(member__team__in=teams)
    member = Member.objects.all()
    return render(request, 'captain/team/MemberEvaluation.html', {'staffs': staffs, 'teams': teams, 'members': member})

def Evaluation(request):
    if request.method == 'POST':
        teamform = TeamForm(request.POST)
        if teamform.is_valid():
            team_name = teamform.cleaned_data['team_name']
            team = Team(team_name=team_name)
            team.save()
    else:
        teamform = TeamForm()

    if request.method == 'POST':
        form = MemberEvaluationForm(request.POST)
        if form.is_valid():
            members = form.cleaned_data['member']
            Monthevaluate = form.cleaned_data['Monthevaluate']
            punctuality = form.cleaned_data['Punctuality']
            attitude = form.cleaned_data['Attitude']
            performance = form.cleaned_data['Performance']
            utilities = form.cleaned_data['Utilities']
            formatting = form.cleaned_data['Formatiing']
            quality = form.cleaned_data['Quality']
            expertise = form.cleaned_data['Expertise']
            new_learning = form.cleaned_data['New_Learning']
            planning = form.cleaned_data['Planning']
            ai_flowed = form.cleaned_data['AI_Flowed']

            staff = MemberEvaluation(member=members, Monthevaluate=Monthevaluate, Punctuality=punctuality, Attitude=attitude, Performance=performance, Utilities=utilities, Formatiing=formatting, Quality=quality, Expertise=expertise, New_Learning=new_learning, Planning=planning, AI_Flowed=ai_flowed)
            staff.save()

            form = MemberEvaluationForm()
            messages.success(request, "Report Added Successfully")
    else:
        form = MemberEvaluationForm()

    
    return render(request, 'captain/team/Evaluation.html', {'form': form, 'teamform': teamform})


# def loginUser(request):
#     if request.method == 'POST':
#         username = request.POST.get('loginUsername')
#         password = request.POST.get('loginPassword')

#         user = authenticate(username=username, password=password)
#         if user is None:
#             print('Invalid username or password.')
#             messages.error(request, 'Invalid username or password')
#             return redirect('/loginUser')

#         profile = TeamMember.objects.filter(user=user).first()
#         if TeamMember is None:
#             print('User profile not found.')
#             messages.error(request, 'User profile not found')
#             return redirect('/loginUser')

#         if not profile.is_varified and not (user.is_superuser and profile.is_admin_verified):
#             print('Your account is not verified. Please check your email.')
#             messages.error(request, 'Your account is not verified. Please check your email.')
#             return redirect('/loginUser')

#         else:
#             login(request, user)
#             return redirect('dashboard')
    
#     return render(request, 'captain/login.html')

# def verify(request, auth_token):
#     try:
#         profile_obj = TeamMember.objects.filter(auth_token=auth_token).first()
#         print(profile_obj)
#         if profile_obj:
#             if profile_obj.is_varified:
#                 messages.success(request, 'Account is already verified')
#                 return redirect('loginUser')
#             else:
#                 profile_obj.is_varified = True
#                 profile_obj.save()
#                 messages.success(request, 'Account has been verified')
#                 return redirect('loginUser')
#         else:
#             return HttpResponseRedirect('/error')
#     except Exception as e:
#         print(e)
#         return HttpResponseRedirect('/error')


# def error_page(request):
#     return render(request, 'captain/team/error.html')

# def send_mail(email, token):
#     subject = 'Your Account Needs to be Verified'
#     message = f'Hi, please click the link to verify your account: http://127.0.0.1:8000/verify/{token}'
#     email_from = settings.DEFAULT_FROM_EMAIL

#     # Create a SendGrid message object
#     message = Mail(
#         from_email=email_from,
#         to_emails=email,
#         subject=subject,
#         plain_text_content=message
#     )

#     # Use SendGrid to send the email
#     sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
#     response = sg.send(message)
#     print(response.status_code)




    # subject = 'Your Account Need to be Verfied'
    # message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify{token}'
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = [email]
    # send_mail(subject, message, email_from, recipient_list)