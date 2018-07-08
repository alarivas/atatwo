from django.shortcuts import render
import blowfish
import qrcode
from django.shortcuts import HttpResponse
from .models import Person, Relation
from notifications.views import email_generator
# Create your views here.

USER_RUT = '18808706-k'
USER_NAME = 'Cele Alarcón'

def rut_transform(_rut):

    rut = _rut[:-2]
    if _rut[-1] == 'K' or _rut[-1] == 'k':
        rut += '1'
        rut += '0'
    else:
        rut += '0'
        rut += _rut[-1]
    return rut


def rut_return(__rut):
    _rut = str(__rut)
    rut = _rut[:-2]
    if _rut[-2] == '1':
        rut += '-'
        rut += 'k'
    else:
        rut += '-'
        rut += _rut[-1]
    return rut


def encrypt(user_rut, benefit_rut, _benefit):
    cipher = blowfish.Cipher(b"secret key")
    b_user_rut = int(user_rut).to_bytes(8, byteorder='big')
    txt_encrypt = b"".join(cipher.encrypt_ecb(b_user_rut))

    b_benefit = bytes(_benefit, 'utf-8')
    while len(b_benefit) % 8 != 0:
        b_benefit += b"0"

    #for rut in benefit_rut:
    b_rut = int(benefit_rut).to_bytes(8, byteorder='big')
    txt_encrypt += b"".join(cipher.encrypt_ecb(b_rut))
    txt_encrypt += b"".join(cipher.encrypt_ecb(b_benefit))

    return txt_encrypt.hex()


def decrypt(txt_encrypt_hex):
    cipher = blowfish.Cipher(b"secret key")
    txt_encrypt = bytearray.fromhex(txt_encrypt_hex)

    #e_ruts = [txt_encrypt[0+i:8+i] for i in range(0, len(txt_encrypt), 8)]
    #ruts = list()
    #for e_rut in e_ruts:
    user_rut = int.from_bytes(b"".join(cipher.decrypt_ecb(txt_encrypt[:8])), byteorder='big')
    benefit_rut = int.from_bytes(b"".join(cipher.decrypt_ecb(txt_encrypt[8:8*2])), byteorder='big')
    benefit = (b"".join(cipher.decrypt_ecb(txt_encrypt[8*2:]))).decode('utf-8').replace("0", "")

    return str(user_rut), str(benefit_rut), benefit


def qr_generate(request):
    if request.method == 'POST':
        benefit = request.POST.get("benefit") #beneficio
        user_benefit = request.POST.get("rut") #rut
        user_name = request.POST.get("name")
        user_rut = rut_transform(USER_RUT)
        benefit_rut = rut_transform(user_benefit)
        to_qr = encrypt(user_rut, benefit_rut, benefit)
        qr = qrcode.make(to_qr)
        qr_name = "media/qr/" + user_rut + benefit + ".png"
        qr.save(qr_name)
        add_relation_graph(request)
        email_generator(qr_name)
        return HttpResponse('QR generado')
    return HttpResponse('QR no generado')


def add_relation_graph(request):
    if Relation.objects.filter(person_one__rut=USER_RUT, person_two__rut=request.POST.get('rut')).exists():
        r = Relation.objects.filter(person_one__rut=USER_RUT, person_two__rut=request.POST.get('rut'))[0]
        r.count += 1
        r.save()
    elif Relation.objects.filter(person_one__rut=request.POST.get('rut'), person_two__rut=USER_RUT).exists():
        r = Relation.objects.filter(person_one__rut=request.POST.get('rut'), person_two__rut=USER_RUT)[0]
        r.count += 1
        r.save()
    else:
        p1, created = Person.objects.get_or_create(name=USER_NAME, rut=USER_RUT)
        p2, created = Person.objects.get_or_create(name=request.POST.get('name'), rut=request.POST.get('rut'))
        Relation.objects.create(person_one=p1, person_two=p2)


def send_qr(request):
    pass


def email():
    pass
