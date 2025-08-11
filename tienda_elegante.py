#
# Simulador de ticket en tienda de indumentaria
#

ropa = ("Remera", "Camisa",  "Pantalón", "Falda", "Vestido", "Abrigo", "Calzado")
super_puntos = ("la prenda 'SI' participa de los super puntos.", "la prenda 'NO' participa de los super puntos.")

print()
print(('"' *20), ('TIENDA DE INDUMENTARIA'), ('"' *20))
#
# PRIMER PRENDA
#

print()
print("\t \t \t \t \t \t \t \t PRIMER PRENDA")
print()
print("Presione el número de la prenda correspondiente: " "\n \n 1= Remera \n 2= Camisa \n 3= Pantalón \n 4= Falda \n 5= Vestido \n 6= Abrigo \n 7= Calzado")
print()

prenda_1 = int(input("Seleccione la prenda: "))
eleccion_1 = ropa[prenda_1 - 1]
precio_1 = float(input("Ingrese el precio de la prenda: "))
super_puntos_1 = int(input("Ingrese el valor '1' si la prenda participa de los súper puntos ó el valor '2' si no cuenta con la promoción: "))
super_puntos_eleccion_1 = super_puntos[super_puntos_1 - 1]

print()
print("Usted eligió la prenda:", eleccion_1, "con un valor de $", precio_1, ".", "Además", super_puntos_eleccion_1)
print()
input("\t \t \t \t \t \t --PRESIONE ENTER PARA CONTINUAR--")
print()

#
# SEGUNDA PRENDA
#

print()
print("\t \t \t \t \t \t \t \t SEGUNDA PRENDA")
print()
print("Presione el número de la prenda correspondiente: " "\n \n 1= Remera \n 2= Camisa \n 3= Pantalon \n 4= Falda \n 5= Vestido \n 6= Abrigo \n 7= Calzado")
print()

prenda_2 = int(input("Seleccione la prenda: "))
eleccion_2 = ropa[prenda_2 - 1]
precio_2 = float(input("Ingrese el precio de la prenda: "))
super_puntos_2 = int(input("Ingrese el valor '1' si la prenda participa de los súper puntos ó el valor '2' si no cuenta con la promoción: "))
super_puntos_eleccion_2 = super_puntos[super_puntos_2 - 1]
print()
print("Usted eligió la prenda:", eleccion_2, "," " con un valor de $", precio_2, "además", super_puntos_eleccion_2)
print()
input("\t \t \t \t \t \t --PRESIONE ENTER PARA CONTINUAR--")
print()

#
# TERCER PRENDA
#

print()
print("\t \t \t \t \t \t \t \t TERCER PRENDA")
print()
print("Presione el número de la prenda correspondiente: " "\n \n 1= Remera \n 2= Camisa \n 3= Pantalon \n 4= Falda \n 5= Vestido \n 6= Abrigo \n 7= Calzado")
print()

prenda_3 = int(input("Seleccione la prenda: "))
eleccion_3 = ropa[prenda_3 - 1]
precio_3 = float(input("Ingrese el precio de la prenda: "))
super_puntos_3 = int(input("Ingrese el valor '1' si la prenda participa de los súper puntos ó el valor '2' si no cuenta con la promoción: "))
super_puntos_eleccion_3 = super_puntos[super_puntos_3 - 1]

print()
print("Usted eligió la prenda:", eleccion_3, "," " con un valor de $", precio_3, "además", super_puntos_eleccion_3)
print()
input("\t \t \t \t \t \t --PRESIONE ENTER PARA CONTINUAR--")
print()

suma_total_precios = precio_1 + precio_2 + precio_3

#
# PROMOCIÓN
#

if prenda_1 == prenda_2 == prenda_3:
    descuento = min(precio_1, precio_2, precio_3)
    precio_final = suma_total_precios - descuento
    print("La suma es de $", precio_final, "participando de la promo 3x2 - 1")
else:
    if prenda_1 == prenda_2 != prenda_3:
        prenda_con_descuento = max(precio_1, precio_2)
        descuento = prenda_con_descuento / 2
        precio_final = descuento + min(precio_1, precio_2) + precio_3
        print("La suma es de $", precio_final, "participando de la promo 50% OFF - 2")
    else:
        if prenda_1 == prenda_3 != prenda_2:
            prenda_con_descuento = max(precio_1, precio_3)
            descuento = prenda_con_descuento / 2
            precio_final = descuento + min(precio_1, precio_3) + precio_2
            print("La suma es de $", precio_final, "participando de la promo 50% OFF - 3")
        else:
            if prenda_2 == prenda_3 != prenda_1:
                prenda_con_descuento = max(precio_2, precio_3)
                descuento = prenda_con_descuento / 2
                precio_final = descuento + min(precio_2, precio_3) + precio_1
                print("La suma es de $", precio_final, "participando de la promo 50% OFF - 4")
            else:
                print("No participa en promo 3x2 y tampoco en promo 50%")
                descuento = 0
                precio_final = suma_total_precios
                print("La suma es de $", precio_final)

#
# PROGRAMA SUPER-PUNTOS
#

super_puntos_reaccion = super_puntos_1 + super_puntos_2 + super_puntos_3

if super_puntos_reaccion == 3:
    super_puntos_promo = (suma_total_precios) * 2
else:
    if super_puntos_1 == 1 and super_puntos_2 == 1:
        super_puntos_promo = precio_1 + precio_2
    else:
        if super_puntos_1 == 1 and super_puntos_3 == 1:
            super_puntos_promo = precio_1 + precio_3
        else:
            if super_puntos_2 == 1 and super_puntos_3 == 1:
                super_puntos_promo = precio_2 + precio_3
            else:
                if super_puntos_1 == 1:
                    super_puntos_promo = precio_1
                else:
                    if super_puntos_2 == 1:
                        super_puntos_promo = precio_2
                    else:
                        if super_puntos_3 == 1:
                            super_puntos_promo = precio_3
                        else:
                            super_puntos_promo = 0

#
# METODOS DE PAGO 'EFECTIVO' - 'TARJETA'
#

print("\t \t \t \t \t \t Método de pago \n 1 - EFECTIVO \n 2 - TARJETA")

forma_de_pago = int(input("Elija el metodo de pago: "))

if forma_de_pago < 2:
    paga_con = ("Efectivo (10% de descuento)")
    calculo = (precio_final * 10) / 100
    el_cliente_paga = precio_final - calculo
    precio_redondeado_final = round(el_cliente_paga, 2)
else:
    n_cuotas = int(input("Ingrese el numero de cuotas a pagar: "))
    if n_cuotas <= 3:
        paga_con = ("Tarjeta - se adiciona un 2% al monto al precio final")
        calculo = (precio_final * 2) / 100
        el_cliente_paga = precio_final + calculo
        precio_redondeado_final = round(el_cliente_paga, 2)
    else:
        paga_con = ("Tarjeta - se adiciona un 5% al monto al precio final")
        calculo = (precio_final * 5) / 100
        el_cliente_paga = precio_final + calculo
        precio_redondeado_final = round(el_cliente_paga, 2)

#
# MUESTRA DE RESULTADOS
#

print()
print("********************** TICKET **********************")
print('-' *50)
print()
print("TIENDA ELEGANCIA")
print()
print(eleccion_1, ": $", precio_1)
print(eleccion_2, ": $", precio_2)
print(eleccion_3, ": $", precio_3)
print("Total sin promo: $",suma_total_precios)
print("Ahorra: $", descuento)
print("Total con promo: $", precio_final)
print("Forma de pago", paga_con)
print("Monto final a pagar: $", precio_redondeado_final)
print("Usted obtiene: ",super_puntos_promo, "SuperPuntos")
print('-' * 50)
input()