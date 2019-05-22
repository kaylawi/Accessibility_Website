from django.conf.urls import url 
from . import views


urlpatterns = [

    url(r'^$', views.home),
    url(r'^maps/$', views.map, name="map"),
    url(r'^projects/$',views.projects, name="projects"),
    url(r'^resources/$',views.resources, name="resources"),

   
   
   
]
