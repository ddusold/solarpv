from django.shortcuts import render
from .forms import RegisterForm, DashboardForm
# Create your views here.


def index(request):
    return render(request, 'register/index.html')


def register(request):
    form = RegisterForm()

    context = {'form': form}
    return render(request, 'register/register.html', context)


def dashboard(request):
    form = DashboardForm()

    context = {'form': form}
    return render(request, 'register/dashboard.html', context)
