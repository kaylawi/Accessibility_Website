from django.shortcuts import render


# Create your views here.

from django.http import Http404 
from django.shortcuts import render

from .models import IssuesReported 

#This function loads the template polls/index.html and pass it a context of dictionary mapping template variable names to Python objects

def index(request):
    latest_issues_list = IssuesReported.objects.order_by('-pub_date'])[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_issues_list': latest_issues_list}
    return render(request, 'polls/index.html', context)

def detail(request, IssuesReported_id)
    return HttpResponse("You're looking at issue %s." % IssuesReported_id)

def results(request, IssuesReported_id):
    response = "You're looking at the results of issues %s."
    return HttpResponse(response % IssuesReported_id)

def vote(request, IssuesReported_id):
    return HttpReponse ("You are voting on issue %s." % IssuesReported_id)

# Error Message that issue doesn't exist
def detail(request, issues_id):
    issue = get_object_or_404(Issue, pk=issues_id)
    return render (request, 'polls/detail.html', {'Issue': issue })

