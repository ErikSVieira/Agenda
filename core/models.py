from django.db import models
from django.contrib.auth.models import User  # Importar usuarios do Django

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    description = models.TextField(
        blank=True, null=True, verbose_name='Desrcição')
    date_event = models.DateTimeField(verbose_name='Data do evento')
    date_created = models.DateTimeField(
        verbose_name='Data de criação', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'event'

    def __str__(self):
        return self.title

    def get_date_event(self):
        return self.date_event.strftime('%d/%m/%Y %H:%M horas')
