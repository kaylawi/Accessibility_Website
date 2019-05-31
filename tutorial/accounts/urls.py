from django.conf.urls import url 
from . import views


urlpatterns = [

    url(r'^$', views.home),
    url(r'^maps/$', views.map, name="map"),
    url(r'^projects/$',views.projects, name="projects"),
    url(r'^resources/$',views.resources, name="resources"),
    url(r'^administration/$',views.administration, name="administration"),
    url(r'^support/$', views.support, name="support"),
    url(r'^orgs/$', views.orgs, name="orgs"),
    url(r'^report/$', views.report, name="report"),
    url(r'^report/map/$', views.fix, name="fix"),


]
