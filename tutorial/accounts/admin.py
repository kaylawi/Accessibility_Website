from django.contrib import admin

#Used to make changes to site administraition page

from .models import IssuesReported
admin.site.register(IssuesReported)
