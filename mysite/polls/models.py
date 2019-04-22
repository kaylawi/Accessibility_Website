import datetime

from django.db import models
from django.utils import timezone 

#DateTimeField = datetimes
#CharField = character fields and requires max_length 
#ForeignKey = tells which tables are related to each other

class IssuesReported(models.Model): #This class represents a table that will represent all of the incoming and current issues on campus 
    text = models.CharField(max_length = 280) #Won't accept strings > 280 Characters
    pub_date = models.DateTimeField('date published') #Dates reports of issues were sent

class Users(models.Model): #This class represents users who reported issues
    user_name = models.CharField(max_length = 25) #Won't accept string > 25 Characters
    display_name = models.CharField(max_length = 100) # Won't accept string > 100 Characters
     