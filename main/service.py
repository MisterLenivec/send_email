from django.core.mail import send_mail
from send_email.settings import EMAIL_HOST_USER


def send(user_email):
    send_mail(
        'Вы подписались на рассылку.',
        'Мы будем присылать вам новости.',
        EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )
