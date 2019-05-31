from django.shortcuts import render, HttpResponse

# Polling



#Home Page 

def home(request):
    return render(request, 'accounts/home.html')

# Links to View Details Sections of site 

def map(request):
    return render(request, 'accounts/map.html')

def resources(request):
    return render(request, 'accounts/resources.html')

def projects(request):
    return render(request, 'accounts/projects.html')

def administration(request):
    return render(request, 'accounts/administration.html')

def support(request):
    return render(request, 'accounts/support.html')

def orgs(request):
    return render(request, 'accounts/orgs.html')

def report(request):
    return render(request, 'accounts/report.html')

def fix(request):
    return render(request, 'accounts/report/map.html')

    
