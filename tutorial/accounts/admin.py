from django.contrib import admin

# This file is used to make changes to site administration page

# Register your models here.

from .models import IssuesReported

admin.site.register(IssuesReported)