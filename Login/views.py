from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Login(request):
    return HttpResponse(request, 'templates/Login/Login.html')