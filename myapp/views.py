from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')
def contact (request):
    return render(request, "contact.html")
def about (request):
    return render(request, "about.html")