from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'expense/index.html')
    #return HttpResponse('<h1>Hello</h1>')

def expense(request):
    return render(request, 'expense/expense.html')