from django.shortcuts import render, redirect
from .forms import *
from .models import *

def home(request):
    return render(request, 'web/home.html')
def events(request):
    return render(request, 'web/events.html')
def tevents(request):
    return render(request, 'web/tevents.html')
def nevents(request):
    return render(request, 'web/nevents.html')
def register(request):
    if request.method == 'GET':
        return render(request, 'web/register.html', {'form': RegisterForm()})
    else:
        try:
            form = RegisterForm(request.POST)
            data = form.save()
            data.save()
            return redirect('success')
        except ValueError:
            return render(request, 'content/register.html', {'form': RegisterForm(), 'error': 'Bad data passed in. Try again.'})
def success(request):
    return render(request, 'web/success.html')