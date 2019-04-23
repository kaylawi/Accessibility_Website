from django.shortcuts import render

## Additional Notes Below

# request.POST is a dictionary-like object that lets you access submitted data by key name and its values are always strings 

# request.POST['choice'] returns ID of the selected choice, as a string. Also, raise KeyError if choice wasn't provided in POST data and redisplays the question form with an error messag if choice isn't given. 

# reverse() help avoid having to hardcode a URL in the view function 

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import IssuesReported 

#This function loads the template polls/index.html and pass it a context of dictionary mapping template variable names to Python objects

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_issues_list'

    def get_queryset(self):
        return IssuesReported.objects.order_by('-pub_date')[:5]  #Return the last five results

class DetailView(generic.DetailView):
    model = IssuesReported
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = IssuesReported
    template_name = 'polls/results.html'

def vote(request, IssuesReported_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    try:
        selected_choice = 
    issue.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
            # Redisplay the issue voting form.
        return render (request, 'polls/details.html', {
        'issue': issue,
        'error_message': " You didn't select a choice.",
    })

    else:
        selected_choice.votes +=1
        selected_choice.save()
        #Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the back button

        return HttpResponseRedirect(reverse('polls:results', args= (issue.id)))

# Error Message that issue doesn't exist
def detail(request, issues_id):
    issue = get_object_or_404(Issue, pk=issues_id)
    return render (request, 'polls/detail.html', {'Issue': issue })

