import datetime

from django.db import models
from django.utils import timezone 
from flask_sqlalchemy import SQLAlchemy 


# class IssuesReported(db.Model): #This class represents a table that will represent all of the incoming and current issues on campus 
#     __tablename__ = "issues" 
#     id = db.Column(db.String, primary_key=True) #Primary key means its unique and will update automatically
#     text = db.Column(db.String(280)) #Won't accept strings > 280 Characters

#     def __repr__(self): 
#         # This method allows us to print out instances and see a representation
#         return "{} (ID: {})".format(self.text,self.id) 



#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text 


class IssuesReported(models.Model): #This class represents a table that will represent all of the incoming and current issues on campus 
    text = models.CharField(max_length = 280) 