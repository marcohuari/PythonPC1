"""
Problema 5:
Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows
"""

nro_show_music = int(input('Digite en número de show musicales que hubo en el último año: '))

if nro_show_music >= 0:
    if nro_show_music > 3:
        print(True)
    else:
        print(False)
else:
    print('Digite un número > 0, por favor')