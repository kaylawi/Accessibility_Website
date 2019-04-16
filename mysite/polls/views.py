from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import IssuesReported 

def detail(request, IssuesReported_id)
    return HttpResponse("You're looking at issue %s." % IssuesReported_id)
