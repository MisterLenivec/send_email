from django.db import models


class Contact(models.Model):
    """Подписка по email"""
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
