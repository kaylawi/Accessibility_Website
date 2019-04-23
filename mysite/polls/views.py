## Additional Notes Below

# request.POST is a dictionary-like object that lets you access submitted data by key name and its values are always strings 

# request.POST['choice'] returns ID of the selected choice, as a string. Also, raise KeyError if choice wasn't provided in POST data and redisplays the question form with an error messag if choice isn't given. 

# reverse() help avoid having to hardcode a URL in the view function 

# Create your views here.

from django.shortcuts import get_object_or_404,render
from .models import IssuesReported

def index(request):
    latest_issue_list = IssuesReported.objects.order_by('-pub_date')[:5]
    context = {'latest_issue_list': latest_issue_list}
    return render(request, 'polls/index.html', context)

def detail(request, user_name_id):
    user_name_ = get_object_or_404(IssuesReported, pk=user_name_id) 
   return render(request, 'polls/detail.html', {'username': user_name})  

def results(request, user_name_id):
    response = "You're looking at the results of user %s"
    return HttpResponse(response % user_name_id)

def vote(request, user_name_id):
    return HttpResponse ("You're voting on question %s." %user_name_id)

# Leave the rest of the views (detail, results, vote) unchanged 