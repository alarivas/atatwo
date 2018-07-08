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
    if request.method == 'POST':
        user_benefit = request.POST.get("rut") #rut
        user_rut = rut_transform(settings.USER_RUT)
        benefit_rut = rut_transform(user_benefit)
        to_qr = encrypt(user_rut, benefit_rut, producto)
        qr = qrcode.make(to_qr)
        qr_name = "media/qr/" + user_rut + producto + ".png"
        qr.save(qr_name)
        add_relation_graph(request)
        return HttpResponse('QR generado')
    return render(request, 'producto.html')


def send_email(request, producto):
    user_rut = rut_transform(settings.USER_RUT)
    qr_name = "media/qr/" + user_rut + producto + ".png"
    email_generator(qr_name)
    return HttpResponse('Email enviado')


def descuento_single(request):
    return render(request, 'descuento_single.html')
