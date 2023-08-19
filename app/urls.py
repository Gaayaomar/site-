from django.urls import path

from . import views


urlpatterns = [
    path ( '', views.index, name='index' ),
    path ( 'details1', views.details, name='index' ),
    path ( 'details2', views.details2, name='index' ),


]