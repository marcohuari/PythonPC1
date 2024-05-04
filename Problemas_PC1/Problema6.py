"""
Problema 6:
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe
preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4
años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, S10.
"""

edad = int(input('Digite su edad: '))

if edad >= 0:
    if edad < 4:
        resultado = 'Puede entrar gratis'
    elif edad <= 18:
        resultado = 'Debe pagar $5'
    else:
        resultado = 'Debe pagar $10'
else:
    resultado = 'Digite un número > 0, por favor'

print(resultado)