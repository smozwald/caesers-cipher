from django.shortcuts import render

# Create your views here.
from libraries.cipher import cipher

def index(request):
    return render(request, 'cipher/index.html')
