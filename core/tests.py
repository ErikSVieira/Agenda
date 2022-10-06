from django.test import TestCase
from datetime import datetime, timezone, timedelta

# Create your tests here.


data = datetime.now()
print(str(data))

diferenca = timedelta(hours=-3)
print(diferenca)

fuso_horario = timezone(diferenca)
print(fuso_horario)

data_e_hora_sao_paulo = data.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_sao_paulo_em_texto)
