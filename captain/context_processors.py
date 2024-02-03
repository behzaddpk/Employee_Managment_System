from .models import TaskDetail

def tasks_processor(request):
    tasks = TaskDetail.objects.all().order_by('-id')[0:3]
    return {'tasks': tasks}