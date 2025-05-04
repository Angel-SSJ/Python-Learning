# Trabjando con fechas y horas en Python
import locale
from datetime import datetime, timedelta

# 1. Obtener la fecha y hora actual
now=datetime.now()
print(f'Fecha y hora actual:{now}')

# 2. Crear una fecha y hora especifica

specific_date = datetime(2025,1,30)
print(f' Fecha y hora especifica {specific_date}')

# 3. Formatear fechas
# metodo  strftime() apra formatear fechas
# pasarle le objeto datetime y el formato especificado
# Document: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

format_date = now.strftime('%d/%m/%Y')
print(f"Fecha formateada: {format_date} :D ")

format_date = now.strftime('%d-%m-%Y %H-%M-%S') # %d son directivas y todas  inician con %
print(f"Fecha formateada: {format_date} :D ")

#4.Operaciones con fechas(sumar -restar dias, minutos, horas, meses)

yesterday = datetime.now()-timedelta(days=1) # UNA BURRADA
print(f'yesterday: {yesterday}')

yesterday = datetime.now()-timedelta(days=0.5) # UNA BURRADA
print(f'half day: {yesterday}')

tomorrow= datetime.now()+timedelta(days=1)
print(f'tomorrow: {tomorrow}')


# 5. COmponentes individuales de una fechas

#
year = now.year
print(f'Year: {year}')

month = now.month
print(f"Month: {month}")

# 6. Calcular la diferencia entre fechas
date1=datetime.now()
date2=datetime(2025,7,28)
difference = date2-date1
print(f'Diferencia entre fechas: {difference}') # timedelta seria como la diferencia o algo asi, osea restar una fecha a otra da un timedelta


# 7.
# para otros idiomas se usa locale
locale.setlocale(locale.LC_TIME,'es_ES') # si agrego .utf-8 no funciona me da error con el coding de los carecteres :C
format_date = now.strftime('%A %B %Y')
print(f"Fecha formateada: {format_date} :D ")

