from django.urls import path
from . import views


app_name = 'location'

urlpatterns = [
    path('', views.index, name='index'),
]