from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'index.html', context)

def orders(request):
    context = {}
    return render(request, 'orders.html', context)


def create_orders(request):
    context = {}
    return render(request, 'create_orders.html', context)