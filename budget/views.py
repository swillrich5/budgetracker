from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Budget
# Create your views here.

def budget(request):
    budget = Budget.objects.all()
    context = {
        'budget': budget,
    }
    return render(request, 'budget/transaction_list.html', context)