from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def xburger(request):
    return render(request, 'xburger.html')

def pizza(request):
    return render(request, 'pizza.html')

def contato(request):
    return render(request, 'contato.html')

