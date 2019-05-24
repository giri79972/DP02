from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def index(request):
    x="Welcome to 1st Web Application"
    return HttpResponse(x)