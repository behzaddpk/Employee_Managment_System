from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
# from .forms import LeaveApplicationForm
from .forms import *
from django.contrib import messages
# Create your views here.


@login_required
def Application(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        date = request.POST.get('date')
        application_text = request.POST.get('application')
        user_id = request.POST.get('user_id')

        user = CustomUser.objects.get(id=user_id)

        application = LeaveApplication(
            user=user,
            subject=subject,
            date=date,
            application=application_text
        )
        application.save()
        messages.success(request, 'Application sent successfully...!!')

    return render(request, 'Application.html', {"user": request.user})
