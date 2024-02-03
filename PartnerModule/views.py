from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from .models import *
import sendgrid
from django.core.mail import send_mail
from django.conf import settings
from sendgrid.helpers.mail import *
import uuid
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required
def PartnerDashboard(request):
    return render(request, 'PartnerDashboard.html')




@login_required
def PartnerList(request):
    partner = Partner.objects.all()
    photo = PartnerPhoto.objects.all()
    return render(request, 'PartnerList.html', {'partners':partner, 'photo':photo})


@login_required
def PartnerProfiles(request, slug=None):
    if request.user.is_authenticated:
        user = request.user
        partner = None
        profile = None  
        photo = None
        skills = None
        experience = None
        bankdetail = None
        bio = None
        if slug is not None:
            try:
                partner = Partner.objects.get(user__slug=slug)
                photo = PartnerPhoto.objects.get(partner=partner)
                profile = PartnerProfile.objects.get(partner=partner)
                bankdetail = BankDetail.objects.get(Partner=partner)
                bio = PartnerBio.objects.get(Partner=partner)

                
            except Exception as e:
                print(e)

        if request.method == 'POST' and request.POST.get('add_skill', False):
            partnerskill_formset = PartnerSkillFormSet(request.POST, instance=partner)
            if partnerskill_formset.is_valid():
                if partner:
                    partner.save()
                for form in partnerskill_formset:
                    skill = form.cleaned_data.get('skill')
                    if form.has_changed():
                        form.instance.partner = partner
                        form.save()
                partnerskill_formset = PartnerSkillFormSet()
        else:
            partnerskill_formset = PartnerSkillFormSet()

        if request.method == 'POST' and request.POST.get('add_experience', False):
            partnerexperience_formset = PartnerExperienceFormset(request.POST, instance=partner)
            if partnerexperience_formset.is_valid():
                for form in partnerexperience_formset:
                    experience1 = form.cleaned_data.get('ExperiencedField')
                    year = form.cleaned_data.get('ExperiencedYear')
                    if form.has_changed():
                        form.instance.partner = partner
                        form.save()
                partnerexperience_formset = PartnerExperienceFormset()
        else:
            partnerexperience_formset = PartnerExperienceFormset()


        if request.method == 'POST' and request.POST.get('add_bio', False):
            partnerbio_formset = PartnerBioFormset(request.POST, instance=partner)
            if partnerbio_formset.is_valid():
                for form in partnerbio_formset:
                    bio1 = form.cleaned_data.get('bio')
                    if form.has_changed():
                        form.instance.partner = partner
                        form.save()
                partnerbio_formset = PartnerBioFormset()
        else:
            partnerbio_formset = PartnerBioFormset()


        
        if request.method == 'POST' and request.POST.get('add_education', False):
            education_formset = PartnerEducationFormset(request.POST, instance=partner)
            if education_formset.is_valid():
                for form in education_formset:
                    studyin = form.cleaned_data.get('StudyIn')
                    PassingYear = form.cleaned_data.get('PassingYear')
                    if form.has_changed():
                        form.instance.partner = partner
                        form.save()
                education_formset = PartnerEducationFormset()
        else:
            education_formset = PartnerEducationFormset()

    skills = PartnerSkill.objects.filter(Partner=partner)
    experience = PartnerExperience.objects.filter(Partner=partner)
    education = PartnerEducation.objects.filter(Partner=partner)
    # bio = PartnerBio.objects.filter(Partner=partner)



    context = {
        'partner': partner,
        'photo': photo,
        'profile': profile,
        'bankdetail':bankdetail,
        'skills': skills,
        'experiences': experience,
        'educations': education,
        'bio': bio,
        'skill_formset': partnerskill_formset,
        'experience_formset': partnerexperience_formset,
        'bio_formset': partnerbio_formset,
        'education_formset':education_formset
    }

    return render(request, 'PartnerProfile.html', context)
