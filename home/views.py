from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    return render(request, "home.html")


def home3(request):
    return render(request, "home-2.html")