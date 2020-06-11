from django.core.mail import send_mail
from send_email.celery import app
from send_email.settings import EMAIL_HOST_USER

from .service import send
from main.models import Contact


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписались на рассылку.',
            'Мы будем присылать вам новости.',
            EMAIL_HOST_USER,
            [contact.email],
            fail_silently=False,
        )
