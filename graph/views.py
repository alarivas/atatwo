from django.shortcuts import render
import blowfish
import qrcode
from django.shortcuts import HttpResponse
from .models import Person, Relation
from notifications.views import email_generator
from graph.functions import *
from django.conf import settings
# Create your views here.


def qr_generate(request):
    if request.method == 'POST':
        benefit = request.POST.get("benefit") #beneficio
        user_benefit = request.POST.get("rut") #rut
        user_name = request.POST.get("name")
        user_rut = rut_transform(settings.USER_RUT)
        benefit_rut = rut_transform(user_benefit)
        to_qr = encrypt(user_rut, benefit_rut, benefit)
        qr = qrcode.make(to_qr)
        qr_name = "media/qr/" + user_rut + benefit + ".png"
        qr.save(qr_name)
        add_relation_graph(request)
        email_generator(qr_name)
        return HttpResponse('QR generado')
    return HttpResponse('QR no generado')


def send_qr(request):
    pass


def email():
    pass


def compute_risk(request):
    p = Person.objects.all()[0]
    friends = [(p.person_two, p.count) for p in p.person_one.all()] + [(p.person_one, p.count) for p in p.person_two.all()]
    count = 0
    for friend, weight in friends:
        print(friend)
        if friend.is_good_payer:
            count += 1*weight
        else:
            count -= 1*weight
    return HttpResponse(count)
