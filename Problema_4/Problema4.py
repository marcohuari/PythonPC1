"""
Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
puede ser calculada de la siguiente forma:
"""

nro_positivo = abs(int(input('Digite un número positivo: ')))

sumatoria = (nro_positivo*(nro_positivo+1))/2

print(f'La sumatoria desde el 1 hasta en {nro_positivo} es: {sumatoria}')