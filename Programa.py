Lista_Jugueria = ['manzanas', 'peras', 'platano', 'fresa', 'leche', 'yogurt', 'cereales', 'papaya']
Dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']


def pedido(antojo, dia):
    if (antojo == Lista_Jugueria[0] or antojo == Lista_Jugueria[1] and dia == Dias[0]):
        print(f"Puede desayunar jugo de {antojo} siendo el dia {dia}")
    elif (antojo == Lista_Jugueria[-1]):
        if (dia == Dias[3] or dia == Dias[4] or dia == Dias[5] or dia == Dias[6]):
            print(f"Puede desayunar jugo de {antojo} siendo el dia {dia}")
    else:
        print("No Podemos procesar su pedido.")


def pedido2(antojo, antojo1, dia):
    if (antojo == Lista_Jugueria[2] or antojo == Lista_Jugueria[3]):
        if (antojo1 == Lista_Jugueria[4] and dia == Dias[1]):
            print(f"Se puede desayunar jugo de leche con {antojo}")
    # no importa el orden de los terminos a ingresar
    elif (antojo == Lista_Jugueria[-3] or antojo == Lista_Jugueria[-2]):
        if (antojo1 == Lista_Jugueria[-3] or antojo1 == Lista_Jugueria[-2] and dia == Dias[2]):
            print(f"Podria tomar de desayuno {antojo} con {antojo1}")
    else:
        print("No podemos recomendarle ningun Desayuno")


antojo1 = input("Ingrese lo que desea comer: ")
if (antojo1 in Lista_Jugueria):
    antojo2 = input("desea agregar algo mas? Escriba si/no : ")
    if (antojo2 == 'si'):
        antojo3 = input("ingrese lo que desea comer: ")
        dia = input('ingrese el dia: ')
        pedido2(antojo1, antojo3, dia)
    elif (antojo2 == 'no'):
        dia = input('ingrese el dia: ')
        pedido(antojo1, dia)
else:
    print(f"{antojo1} no se encuentra dentro de nuestra Lista")