from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_blogapp(request):
    return HttpResponse("Hello, I'm going to be a blog one day!")