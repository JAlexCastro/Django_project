from django.shortcuts import render, redirect

def popUp(request):
    return render(request, "popUpEmail.html")