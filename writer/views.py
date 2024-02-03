from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

@login_required 
def WriterDashboard(request):
    return render(request, 'WriterDashboard.html')


@login_required
def WriterList(request):
    writer = Writer.objects.all()
    
    context = {
        'writers': writer
    }
    return render(request, 'WriterList.html', context)


@login_required
def Writer_Profile(request, slug):
    writer = Writer.objects.get(user__slug =slug)
    photo = WriterPhoto.objects.get(Writer=writer)
    profile = WriterProfile.objects.get(Writer=writer)
    Bank = BankDetail.objects.get(Writer=writer)

    if request.method == 'POST' and request.POST.get('add_skill', False):
        writerskill_formset = WriterSkillFormset(request.POST, instance=writer)
        if writerskill_formset.is_valid():
            if writer:
                writer.save()
            for form in writerskill_formset:
                skill = form.cleaned_data.get('skill')
                if form.has_changed():
                    form.instance.writer = writer
                    form.save()

            writerskill_formset = WriterSkillFormset()
    else:
        writerskill_formset = WriterSkillFormset()

    if request.method == 'POST' and request.POST.get('add_experience', False):
        writerexperience_formset = WriterExperienceFormset(request.POST, instance=writer)
        if writerexperience_formset.is_valid():
            if writer:
                writer.save()
                for form in writerexperience_formset:
                    experience = form.cleaned_data['ExperiencedField']
                    year = form.cleaned_data['ExperiencedYear']
                    if form.has_changed():
                        form.instance.writer = writer
                        form.save()

                writerexperience_formset = WriterExperienceFormset()

    else:
        writerexperience_formset = WriterExperienceFormset()

    if request.method == 'POST' and request.POST.get('add_education', False):
        writededucation_formset = WriterEducationFormset(request.POST, instance=writer)
        if writededucation_formset.is_valid():
            if writer:
                writer.save()
                for form in writededucation_formset:
                    studyin = form.cleaned_data['StudyIn']
                    pasingyar = form.cleaned_data['PassingYear']
                    if form.has_changed():
                        form.instance.writer = writer
                        form.save()
                writededucation_formset = WriterEducationFormset()
    else:
        writededucation_formset = WriterEducationFormset()


    skill = WriterSkill.objects.filter(Writer=writer)
    experience = WriterExperience.objects.filter(Writer=writer)
    education = WriterEducation.objects.filter(Writer=writer)
    context = {
        "writer": writer,
        'photo':photo,
        'profile':profile,
        'bank': Bank,
        'writerskill_formset':writerskill_formset,
        'skills': skill,
        'writerexperience_formset': writerexperience_formset,
        'experiences':experience,
        'writededucation_formset':writededucation_formset,
        'educations':education
    }
    return render(request, 'WriterProfile.html', context)