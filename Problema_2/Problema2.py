"""
Problema 2:
En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
dejar como propina.
"""

precio_consumo = float(input('Digite el precio consumido en el restaurante: '))
porcentaje_propina = float(input('Digite el porcentaje de propina a dejar al mesero (en decimales): '))

if porcentaje_propina >= 0 and porcentaje_propina <= 1:
    propina = precio_consumo*porcentaje_propina
    print(f'La cantidad de propina a dejar es: {propina}')
else:
    print('El porcentaje de propina fue mal digitado, debe estar entre 0 y 1')
