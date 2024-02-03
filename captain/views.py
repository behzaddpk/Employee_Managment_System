from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from team.models import Member
from django.core.paginator import Paginator
from django.db.models import Count
from clients.models import (
    Client,
)
from .models import *
from .forms import *
# Create your views here.


@login_required()
def dashboard(request):
    tasks = TaskDetail.objects.all().order_by('-id')[0:3]
    clients_count = Client.objects.aggregate(count=Count('id'))['count']
    task_count = TaskDetail.objects.aggregate(count=Count('id'))['count']

    context = {
        'tasks': tasks,
        'clients_count':clients_count,
        'task_count':task_count

    }
    return render(request, 'captain/index.html', context)

@login_required
def Tasklist(request):
    tasks = TaskDetail.objects.all()
    page = Paginator(tasks, 4)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'tasks': tasks,
        'page': page
    }
    return render(request, 'captain/task/tasklist.html', context)

@login_required
def TaskDescription(request, slug=None):
    task = None
    try:
        task = TaskDetail.objects.get(slug=slug) 
    except Exception as e:
        print(e)

    context = {
        'task': task
    }
    return render(request, 'captain/task/taskdescription.html', context)

@login_required()
def registration(request):

    if request.method == 'POST':
        
        username = request.POST.get('registerUsername')
        email = request.POST.get('registerEmail')
        password = request.POST.get('registerPassword')
        is_staff = request.POST.get('isStaff', False) == 'on'
        if User.objects.filter(username=username).exists():
            print('username is taken')
        elif User.objects.filter(email=email).exists():
            print('email already exists')
            user = User.objects.create_user(username=username, email=email, password=password, is_staff=is_staff)
            user_profile = User.objects.create(user = user, )
            user.save()
            return redirect('register')
    return render(request, 'captain/register.html')


@login_required()
def AddTask(request):
    if request.method == 'POST' and request.POST.get('add_task', False):
        TaskCategoryform = TaskCategoryForm(request.POST)
        if TaskCategoryform.is_valid():
            user = request.user
            name = TaskCategoryform.cleaned_data['taskname']
            task = TaskCategory(taskname=name)
            task.save()
            TaskCategoryform = TaskCategoryForm()
    else:
        TaskCategoryform = TaskCategoryForm()


    if request.method == 'POST' and request.POST.get('add_institution', False):
        InstitutionNameform = InstitutionNameForm(request.POST)
        if InstitutionNameform.is_valid():
            user = request.user
            name = InstitutionNameform.cleaned_data['InstitutionName']
            task = InstitutionName(InstitutionName=name)
            task.save()
            InstitutionNameform = InstitutionNameForm()
    else:
        InstitutionNameform = InstitutionNameForm()


    
    if request.method == 'POST' and request.POST.get('add_assesstment', False):
        AssessmentTypeform = AssessmentTypeForm(request.POST)
        if AssessmentTypeform.is_valid():
            user = request.user
            name = AssessmentTypeform.cleaned_data['AssessmentName']
            task = AssessmentType(AssessmentName=name)
            task.save()
            AssessmentTypeform = AssessmentTypeForm()
    else:
        AssessmentTypeform = AssessmentTypeForm()


    TaskDetailform = TaskDetailForm()
    if request.method == 'POST' and request.POST.get('add_tasks', False):
        TaskDetailform = TaskDetailForm(request.POST, request.FILES)
        if TaskDetailform.is_valid():
            task_name = TaskDetailform.cleaned_data['task_name']
            client = TaskDetailform.cleaned_data['client']
            task_category = TaskDetailform.cleaned_data['task_category']
            institution_name = TaskDetailform.cleaned_data['institution_name']
            course_code = TaskDetailform.cleaned_data['course_code']
            deadline = TaskDetailform.cleaned_data['deadline']
            instruction = TaskDetailform.cleaned_data['instruction']
            word_count = TaskDetailform.cleaned_data['word_count']
            assessment_type = TaskDetailform.cleaned_data['assessment_type']
            attachment_file = TaskDetailform.cleaned_data['attachment_file']
            send_to_username = TaskDetailform.cleaned_data['send_to']

            # Retrieve the Member object based on the provided username
            send_to = get_object_or_404(Member, user__username=send_to_username)

            form = TaskDetail(
                task_name=task_name,
                client=client,
                task_category=task_category,
                institution_name=institution_name,
                course_code=course_code,
                deadline=deadline,
                instruction=instruction,
                word_count=word_count,
                assessment_type=assessment_type,
                attachment_file=attachment_file,
                send_to=send_to
            )
            form.save()
            
            TaskDetailform = TaskDetailForm()
        else:
            TaskDetailform = TaskDetailForm()
    return render(request, 'captain/tasks.html', {'TaskCategoryform': TaskCategoryform, 'InstitutionNameform': InstitutionNameform, 'AssessmentTypeform': AssessmentTypeform, 'TaskDetailform':TaskDetailform})




@login_required()
def clients(request):
    return render(request, 'captain/clients/clients.html')

@login_required()
def add_client(request):
    return render(request, 'captain/clients/add_client.html')


@login_required()
def tables(request):
    return render(request, 'captain/tables.html')

@login_required()
def charts(request):
    return render(request, 'captain/charts.html')


@login_required()
def profile(request):
    return render(request, 'captain/profile.html')

def logout1(request):
    logout(request)
    return redirect('login')