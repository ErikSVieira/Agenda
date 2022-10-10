from django.db import models
from django.contrib.auth.models import User  # Importar usuarios do Django
from datetime import timezone, timedelta

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
        data = self.date_event
        tzBR = timezone(timedelta(hours=-3))
        tzData = data.astimezone(tzBR)
        return tzData.strftime('%d/%m/%Y %H:%M')
        # return self.date_event.strftime('%d/%m/%Y %H:%M')
    
    def get_input_date_event(self):
        data = self.date_event
        tzBR = timezone(timedelta(hours=-3))
        tzData = data.astimezone(tzBR)
        return tzData.strftime('%Y-%m-%dT%H:%M')
        # return self.date_event.strftime('%Y-%m-%dT%H:%M')
