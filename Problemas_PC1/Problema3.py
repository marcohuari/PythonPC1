"""
Problema 3:
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
último pedido y calcule el peso total del paquete que será enviado.
"""

peso_un_payaso = 112 #En gramos
peso_una_munieca = 75 #En gramos
#En el último pedido
nro_payaso = int(input('Digite el número de payasos vendidos: '))
nro_munieca = int(input('Digite el número de muniecas vendidas: '))

peso_total = ((peso_un_payaso*nro_payaso) + (peso_una_munieca*nro_munieca))/1000

print(f'\nEl número de payasos y muniecas vendidos fueron: {nro_payaso} y {nro_munieca} respectivamente con un peso total de {peso_total} kg.')
