from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.



@login_required
def CoordinatorDashboard(request):
    return render(request, 'coordinatordashboard.html')


@login_required
def CoordinatorList(request):
    coordinator = Coordinator.objects.all()
    cordphoto = CoordinatorPhoto.objects.all()

    context = {
        'coordinator': coordinator,
        'cordphoto': cordphoto
    }
    return render(request, 'coordinatorlist.html', context)


@login_required
def Coordinator_Profile(request, slug):
    
    if request.user.is_authenticated:
        cordinator = None
        photo = None
        bank = None
        profile = None
        if slug is not None:
            try:
                cord = Coordinator.objects.get(user__slug =slug)
                profile = CoordinatorProfile.objects.get(coordinator=cord)
                photo = CoordinatorPhoto.objects.get(coordinator=cord)
                bank = CoordinatorBankDetail.objects.get(coordinator=cord)
            except Exception as e:
                print(e)

        if request.method == 'POST' and request.POST.get('add_skill', False):
            cordskill_formset = CoordinatorSkillFormset(request.POST, instance=cord)
            if cordskill_formset.is_valid():
                if cord:
                    cord.save()
                for form in cordskill_formset:
                    skill = form.cleaned_data.get('skill')
                    if form.has_changed():
                        form.instance.cord = cord
                        form.save()
                cordskill_formset = CoordinatorSkillFormset()
        else:
            cordskill_formset = CoordinatorSkillFormset()

        if request.method == 'POST' and request.POST.get('add_experience', False):
            cordexperience_formset = CoordinatorExperienceFormset(request.POST, instance=cord)
            if cordexperience_formset.is_valid():
                if cord:
                    cord.save()
                for form in cordexperience_formset:
                    experiencefield = form.cleaned_data['ExperiencedField']
                    experienceyear = form.cleaned_data['ExperiencedYear']
                    if form.has_changed():
                        form.instance.cord = cord
                        form.save()
                
                cordexperience_formset = CoordinatorExperienceFormset()
        else:
            cordexperience_formset = CoordinatorExperienceFormset()


        if request.method == 'POST' and request.POST.get('add_education', False):
            coordeducation_formset = CoordinationEducationFormset(request.POST, instance=cord)
            if coordeducation_formset.is_valid():
                if cord:
                    cord.save()
                for form in coordeducation_formset:
                    StudyIn = form.cleaned_data['StudyIn']
                    PassingYear = form.cleaned_data['PassingYear']
                    if form.has_changed():
                        form.instance.cord = cord
                        form.save()
                coordeducation_formset = CoordinationEducationFormset()
        else:
            coordeducation_formset = CoordinationEducationFormset()



    skills = CoordinatorSkill.objects.filter(coordinator=cord)
    experience = CoordinatorExperience.objects.filter(coordinator=cord)
    education = CoordinatorEducation.objects.filter(coordinator=cord)
    context = {
        'cord':cord,
        'photo':photo,
        'profile':profile,
        'bank':bank,
        'skills':skills,
        'experiences':experience,
        'educations':education,
        'cordskill_formset': cordskill_formset,
        'cordexperience_formset': cordexperience_formset,
        'coordeducation_formset': coordeducation_formset,
    }
    return render(request, 'CoordinatorProfile.html', context)
