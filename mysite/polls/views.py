from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import IssuesReported 

def detail(request, IssuesReported_id)
    return HttpResponse("You're looking at issue %s." % IssuesReported_id)

def results(request, IssuesReported_id):
    response = "You're looking at the results of issues %s."
    return HttpResponse(response % IssuesReported_id)

def vote(request, IssuesReported_id):
    return HttpReponse ("You are voting on issue %s." % IssuesReported_id)


