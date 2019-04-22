from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:IssuesReported_id>/',views.detail, name='detail'),
    path('<int:IssuesReported_id>/results/', views.results, mae='results'),
    path('<int:IssuesReported_id>/vote/', views.vote, name='vote'),
]
