from django.urls import path

from . import views

app_name = 'cipher'
urlpatterns = [
    path('', views.index, name='index'),
]