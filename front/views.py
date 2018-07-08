from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request, 'portal.html')


def beneficios(request):
    return render(request, 'descuentos.html')


def producto(request):
    return render(request, 'producto.html')