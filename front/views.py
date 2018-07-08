from django.shortcuts import HttpResponse, render
from graph.functions import *
from django.conf import settings
import qrcode
from notifications.views import email_generator


def index(request):
    return render(request, 'portal.html')


def beneficios(request):
    return render(request, 'descuentos.html')


def producto(request, producto):
<<<<<<< HEAD
    print(producto)
=======
    is_hidden = True
>>>>>>> a791563c064e62d92d0f6e2634348d26237d9f32
    if request.method == 'POST':
        user_benefit = request.POST.get("rut") #rut
        user_rut = rut_transform(settings.USER_RUT)
        benefit_rut = rut_transform(user_benefit)
        to_qr = encrypt(user_rut, benefit_rut, producto)
        qr = qrcode.make(to_qr)
        qr_name = "media/qr/" + user_rut + producto + ".png"
        qr.save(qr_name)
        add_relation_graph(request)
        is_hidden = False
    return render(request, 'producto.html', {'is_hidden': is_hidden})


def send_email(request, producto):
    user_rut = rut_transform(settings.USER_RUT)
    qr_name = "media/qr/" + user_rut + producto + ".png"
    email_generator(qr_name)
    return HttpResponse('Email enviado')


def descuento_single(request):
    return render(request, 'descuento_single.html')
