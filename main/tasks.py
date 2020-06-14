from celery import shared_task
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


# Examples, run on shell (delay, apply_async)

@app.task
def my_task(a, b):
    c = a + b
    return c


@app.task(bind=True, default_retry_delay=5 * 60)
def my_task_retry(self, x, y):
    try:
        return x + y
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@shared_task()
def my_sh_task(msg):
    return msg + '!!!'
