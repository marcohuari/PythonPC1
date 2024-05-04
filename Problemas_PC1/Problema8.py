"""
Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la
hora del almuerzo o la hora de la cena. Si no es hora de comer, no envíes nada.
Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar.
"""

h,m = input('Digite la hora actual en formato ##:##: ').split(":")

h = float(h)
m = float(m)

if (h >= 0 and h <= 24) and (m >= 0 and m <= 60):
    if (h >= 7 and h <= 8) and (m >= 0 and m <= 60):
        resultado = 'Es la hora del desayuno'
    elif (h >= 12 and h <= 13) and (m >= 0 and m <= 60):
        resultado = 'Es la hora del almuerzo'
    elif (h >= 18 and h <= 19) and (m >= 0 and m <= 60):
        resultado = 'Es hora de la cena'
    else:
        resultado = ''
else:
    resultado = 'Digite una hora entre 0 y 24, y un minuto entre 0 y 60'

print(resultado)