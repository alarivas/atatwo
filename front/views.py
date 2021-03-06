from django.shortcuts import HttpResponse, render
from graph.functions import *
from django.conf import settings
import qrcode
from graph.functions import decrypt, rut_return
from notifications.views import email_generator


def index(request):
    return render(request, 'portal.html')


def beneficios(request):
    return render(request, 'descuentos.html')


def producto(request, producto):

    print(producto)

    is_hidden = True

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
        return render(request, 'producto.html', {'is_hidden': is_hidden,'qr_img': qr_name})
    return render(request, 'producto.html', {'is_hidden': is_hidden})


def send_email(request, producto):
    user_rut = rut_transform(settings.USER_RUT)
    qr_name = "media/qr/" + user_rut + producto + ".png"
    email_generator(qr_name)
    return HttpResponse('Email enviado')


def descuento_single(request):
    return render(request, 'descuento_single.html')


def exectutive(request):
    return render(request,'executive.html')


def comprove(request):
    try:
        user, u_benefit, benefit = decrypt(request.GET.get('encode'))
        user = rut_return(user)
        u_benefit = rut_return(u_benefit)
        return render(request, 'result-positive.html', {'user': user, 'benefit_rut': u_benefit, 'benefit': benefit})
    except ValueError:
        return render(request, 'result-negative.html')

def result_positive(request):
    return render(request,'result-positive.html')

def result_negative(request):
    return render(request,'result-negative.html')

def dashboard(request):

    return render(request, 'dashboard.html')
