from django.shortcuts import HttpResponse
import os
import sendgrid
from sendgrid import Email
from sendgrid.helpers.mail import Content, Mail


def send_email(vto, vsubject, vcontent, vfrom):
    sg = sendgrid.SendGridAPIClient(apikey='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')
    from_email = Email(vfrom)
    to_email = Email(vto)
    subject = vsubject
    content = Content("text/html", vcontent)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
    return response


def send_qr(request):
    response = send_email('alanrivas@thedogcompany.cl',
                          'testing',
                          '<html><head></head><body>hola</body></html>',
                          'hola <atatwo@atatwo.cl>')

    return HttpResponse("Correo enviado")
