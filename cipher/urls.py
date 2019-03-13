from django.urls import path

from . import views

app_name = 'cipher'

##Figure out why we can't have index and cipher_input both going to index page.
urlpatterns = [
    path('', views.cipher_input, name = 'cipher_input'),
    path('', views.index, name='index'),
]