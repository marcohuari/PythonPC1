"""
Problema 7:
Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.
"""

n1 = float(input('Digite en primer número: '))
n2 = float(input('Digite el segundo número: '))
opc = input('Digite la opción sumar, restar o multiplicar: ').lower()

if opc == 'sumar':
    resultado = n1 + n2
elif opc == 'restar':
    resultado = n1 - n2
elif opc == 'multiplicar':
    resultado = n1 * n2
else:
    resultado ='Digite solamente las opciones sumar, restar o multiplicar'

if opc == 'sumar' or opc == 'restar' or opc == 'multiplicar':
    print(f'El resultado de {opc} el número {n1} y el número {n2} es: {resultado}')
else:
    print(resultado)