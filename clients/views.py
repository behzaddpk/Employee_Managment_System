from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ClientForm
from .models import Client


# Create your views here.


@login_required()
def client(request):
    client = Client.objects.all()
    return render(request, 'captain/clients/clients.html', {'clients': client})

@login_required()
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            full_name = form.cleaned_data['Full_name']
            email = form.cleaned_data['email']
            country = form.cleaned_data['country']
            contactno = form.cleaned_data['contactno']
            bank_account = form.cleaned_data['bank_account']
            weblink = form.cleaned_data['weblink']
            img = form.cleaned_data['img']
            reg = Client(user=user, Full_name=full_name, email=email, country=country, contactno=contactno, bank_account=bank_account, weblink=weblink, img=img)
            reg.save()
            form = ClientForm()
        # else not form.is_valid():
        #     print(form.errors)
    else:
        form = ClientForm()
    return render(request, 'captain/clients/add_client.html', {'forms': form})


def client_profile(request, slug=None):
    client = None
    if slug is not None:
        try:
            client = Client.objects.get(slug=slug)
        except:
            pass
    return render(request, 'captain/clients/client_profile.html', {'clients': client})


