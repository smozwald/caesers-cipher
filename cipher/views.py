from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
from cipher.libraries.cipher import cipher
from .forms import InputForm

def index(request, output = "Output will appear here"):
    return render(request, 'cipher/index.html', {'output': output})

def cipher_input(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            string = form.cleaned_data['string']
            offset = form.cleaned_data['offset']
            output = cipher(string, offset)
            return index(request, output)