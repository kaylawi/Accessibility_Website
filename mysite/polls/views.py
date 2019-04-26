## Additional Notes Below

# request.POST is a dictionary-like object that lets you access submitted data by key name and its values are always strings 

# request.POST['choice'] returns ID of the selected choice, as a string. Also, raise KeyError if choice wasn't provided in POST data and redisplays the question form with an error messag if choice isn't given. 

# reverse() help avoid having to hardcode a URL in the view function 

# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Users, IssuesReported

def test(request):
    #return HttpResponse("test")
    return render(request, 'polls/test.html')

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_issue_list'

    def get_queryset(self):
        # Return the last five published questions
        return IssuesReported.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = IssuesReported
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = IssuesReported
    template_name = 'polls/results.html'


def vote(request, question_id):
    user_name = get_object_or_404(IssuesReported, pk=question_id)
    try:
        selected_choice = IssuesReported.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Users.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'username': user_name,
            'error_message': "You didn't select a user name.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(user_name.id,)))





