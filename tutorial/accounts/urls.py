from django.conf.urls import url 
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [

    url(r'^$', views.home),
    url(r'^login/$', LoginView, {'template_name': 'accounts/login.html'}) 
   
]
