from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.



@login_required
def TeamLeaderDashboard(request):
    pass


@login_required
def TeamLeaderList(request):
    teamleader = TeamLeader.objects.all()

    context = {
        'teamleader': teamleader
    }
    return render(request, 'TeamLeaderList.html', context)


@login_required
def TeamLeader_Profile(request, slug=None):

    if request.user.is_authenticated:
        leader = None
        profile = None
        photo = None
        bank = None
        if slug is not None:
            leader = TeamLeader.objects.get(user__slug = slug) 
            photo = TeamLeaderPhoto.objects.get(user=leader)
            bank = TeamLeaderBankDetail.objects.get(user=leader)
            profile = TeamLeaderProfile.objects.get(user=leader)
            
        # ...

        if request.method == 'POST' and request.POST.get('add_skill', False):
            leaderskill_formset = LeaderSkillFormset(request.POST, instance=leader)
            if leaderskill_formset.is_valid():
                if leader:
                    leader.save()
                for form in leaderskill_formset:
                    skill = form.cleaned_data.get('skill')
                    if form.has_changed():
                        form.instance.leader = leader
                        form.save()
                leaderskill_formset = LeaderSkillFormset()
        else:
            leaderskill_formset = LeaderSkillFormset()

        if request.method == 'POST' and request.POST.get('add_experience', False):
            leaderexperience_formset = LeaderExperiencedFormset(request.POST, instance=leader)
            if leaderexperience_formset.is_valid():
                if leader:
                    leader.save()
                for form in leaderexperience_formset:
                    experiencefield = form.cleaned_data.get('ExperiencedField')
                    experienceyear = form.cleaned_data.get('ExperiencedYear')
                    if form.has_changed():
                        form.instance.leader = leader
                        form.save()

                leaderexperience_formset = LeaderExperiencedFormset()
        else:
            leaderexperience_formset = LeaderExperiencedFormset()




        if request.method == 'POST' and request.POST.get('add_education', False):
            leadereducation_formset = LeaderEducationFormset(request.POST, instance=leader)
            if leadereducation_formset.is_valid():
                if leader:
                    leader.save()
                for form in leadereducation_formset:
                    studyIn = form.cleaned_data.get('StudyIn')
                    passingyear = form.cleaned_data.get('PassingYear')
                    if form.has_changed():
                        form.instance.leader = leader
                        form.save()
                leadereducation_formset = LeaderEducationFormset()
        else:
            leadereducation_formset = LeaderEducationFormset()


    

    skill = TeamLeaderSkill.objects.filter(user=leader)
    experience = TeamLeaderExperience.objects.filter(user=leader)
    education = TeamLeaderEducation.objects.filter(user=leader)
    context ={
        'leader': leader,
        'photo': photo,
        'bank': bank,
        'profile':profile,
        'leaderskill_formset': leaderskill_formset,
        'skills':skill,
        'leaderexperience_formset': leaderexperience_formset,
        'experiences':experience,
        'leadereducation_formset': leadereducation_formset,
        'educations':education
    }


    return render(request, 'TeamLeaderProfile.html', context)