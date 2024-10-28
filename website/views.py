from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting
from datetime import datetime

def welcome(request):
    return render(request, "website/home.html", {"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse(f"This page was served at {str(datetime.now())}")

def about(request):
    return HttpResponse("My name is Muslim Helalee")