from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def budget(request):
    return HttpResponse("<h1>Hello</h1>")