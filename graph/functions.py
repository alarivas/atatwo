import blowfish
from graph.models import *
from django.conf import settings


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


def add_relation_graph(request):
    if Relation.objects.filter(person_one__rut=settings.USER_RUT, person_two__rut=request.POST.get('rut')).exists():
        r = Relation.objects.filter(person_one__rut=settings.USER_RUT, person_two__rut=request.POST.get('rut'))[0]
        r.count += 1
        r.benefits.add(Benefit.objects.filter(name=request.POST.get('benefit'))[0])
        r.save()
    elif Relation.objects.filter(person_one__rut=request.POST.get('rut'), person_two__rut=settings.USER_RUT).exists():
        r = Relation.objects.filter(person_one__rut=request.POST.get('rut'), person_two__rut=settings.USER_RUT)[0]
        r.count += 1
        r.benefits.add(Benefit.objects.filter(name=request.POST.get('benefit'))[0])
        r.save()
    else:
        p1, created = Person.objects.get_or_create(name=settings.USER_NAME, rut=settings.USER_RUT)
        p2, created = Person.objects.get_or_create(name=request.POST.get('name'), rut=request.POST.get('rut'))
        r = Relation.objects.create(person_one=p1, person_two=p2)
        r.benefits.add(Benefit.objects.filter(name=request.POST.get('benefit'))[0])
