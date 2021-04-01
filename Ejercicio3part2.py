'''Ejercicio 3, parte 2 (Cadenas, listas y diccionarios)
"Supermercado Familiar"
Nombre: Josué Samuel Argueta Hernández
Carne: 211024
Fecha: 16/03/2021'''
import os
def principal():
    #diccionariarios
    expediente_cant = {'leche':  20,'mantequilla':15,'queso':15,'yogurt':35,'manzanas':35,'naranjas':40,
                       'bananos':23,'galletas':   32,'pan':  20,'jalea': 18}
    expediente_price = {'leche':1.19,'mantequilla':1.90,'queso':2.59,'yogurt':3.15,'manzanas':2.15,'naranjas':0.99,
                        'bananos':1.29,'galletas':1.45,'pan':4.99,'jalea':3.65}
    #listas vacias
    product_canasta,cantidad_canast, gasto_client,precio = [],[],[],[]
    clientes, productos = {},{}
    #cierre de caja, variables
    Recibos, ganancias = 0,0
    bandera = True
    #repetir el proceso segun sea la cantidad de clientes y disponibilidad en el almacen
    while bandera:
        nombre_cliente = input("\nIngrese su nombre: ")
        Recibos += 1
        #repetir el proceso segun la cantidad de productos que el cliente desee adquirir
        ventas = True
        while ventas:
            verificacion = True
            while verificacion:
                #mostrar los productos existentes en almacen
                print("\nPRODUCTO\tCANTIDAD\n")
                for claves,cantidad in expediente_cant.items():
                    print(claves,"    \t  ",cantidad)
                producto = input("\nIngrese el producto: ")
                #Verificar si el producto esta en almacen o si es inexistente
                #repetir la pregunta, en caso de pedir producto inexistente en bodega
                if producto.lower() not in expediente_cant.keys():
                    print("\nDEBE INGRESAR 1 DE LOS PRODUCTOS EXISTENTES\n")
                    verificacion = True
                #almacenar el producto en una lista
                else:
                    #almacenar el producto en la lista producto_canasta
                    minimizar = producto.lower()
                    product_canasta.append(minimizar)
                    verificacion = False
            #obtener un valor numerico
            mal_dato = True
            while mal_dato:
                try:
                    cant_almacen = True
                    #repetir en caso de exceder la cantidad de producto existente
                    while cant_almacen:
                        #comprobar si ingresan valor numerico, sino, repetir hasta que ingresen un valor
                        cantidad = int(input("Ingrese la cantidad que desea comprar: "))
                        #comprobar si es una cantidad validad, segun la cantidad de producto
                        if cantidad > expediente_cant[minimizar] or cantidad <= 0:
                            print("Debe ingresar un valor segun el almacen")
                            cant_almacen = True
                        else:
                            #almacenar en lista, si es valor numerico
                            cantidad_canast.append(cantidad)
                            cant_almacen = False
                        #restar valores al diccionario
                    expediente_cant[minimizar] -= cantidad
                    break
                except ValueError:
                    print("\nDebe ingresar un valor numerico")
                    mal_dato = True   
            
            #llamar a la funcion calculo
            gasto_producto = calculos(minimizar, cantidad, expediente_price)
            #almacenar el resultado flotante con 2 decimales
            gasto_client.append(f"{gasto_producto:.2f}")
            #en caso de no obtner un SI o un NO como respuesta
            incongruencia = True
            while incongruencia:
                pregunta = input("\n¿Desea seguir comprando? (Si/No): ")
                #repetir el proceso si es un si
                if pregunta.lower() == 'si':
                    Recibos += 0
                    incongruencia = False
                    ventas = True
                #mostrar recibo de caja
                elif pregunta.lower() == 'no':
                    #alamcaenar en una lista los valores del diccionario con los precios
                    for item in expediente_price:
                        precio.append(expediente_price[item])
                    print(f"\nRecibo de {nombre_cliente}")
                    print("Cantidad  Producto\tprecio\ttotal")
                    #mostar por columnas los productos adquiridos
                    for i in range (len(product_canasta)):
                        print(f"{cantidad_canast[i]}  {product_canasta[i]}\t\t{precio[i]}\t{gasto_client[i]}")
                    total = sumar(gasto_client)
                    print(f"\t\tTotal a pagar\t{total:.2f}\n")
                    ganancias += total
                    #almacenar los valores en 1 diccionario
                    clientes[nombre_cliente] = gasto_client
                    for i in range(len(product_canasta)):
                        productos[product_canasta[i]] = cantidad_canast[i]
                    #resetear las listas, para que no se cobre lo que no se debe
                    for i in range(len(product_canasta)):
                        cantidad_canast.pop()
                        product_canasta.pop()
                        gasto_client.pop()
                    incongruencia = False   
                    ventas = False
                    #hacer lista el diccionario, debido a que no puede sufrir alteraciones como diccionario
                    for item in list(expediente_cant.keys()):
                    #eliminar el producto del expediente, debido a que no hay existencias
                        if expediente_cant[item] <= 0:
                            del expediente_cant[item]
                else:
                    print("RESPUESTA INCONGRUENTE, VUELVA A INRESAR SU RESPUESTA (SI/NO)")
                    incongruencia = True
        cliente_nuevo = True
        while cliente_nuevo:
            #volvera ingresar los datos con un nuevo cliente
            pregunta = input("¿Nuevo Cliente? (Si/No): ")
            if pregunta.lower() == 'si':
                cliente_nuevo = False
                bandera = True
            elif pregunta.lower() == 'no':
                cliente_nuevo = False
                bandera = False
            else:
                print("RESPUESTA INCONGRUENTE, INGRESE 'SI' O 'NO'")
                cliente_nuevo = True
    #mostrar cierre de caja
    caja = True
    while caja:
        pregunta2 = input("¿Desea ver el cierre de caja?: ")
        if pregunta2.lower() == 'si':
            print(f"\nCantidad de Facturas: {Recibos}")
            print(f"Ganancias del dia: {ganancias:.2f}\n")
            print("SI NO ENCUENTRA EL PRODUCTO EN CIERRE DE CAJA. NO HAY EXISTENCIAS\n")
            print("PRODUCTO\tCANTIDAD\n")
            for claves,cantidad in expediente_cant.items():
                    print(f"{claves}    \t  {cantidad}")
            print()
            os.system("PAUSE")
            caja = False
        elif pregunta2.lower() == 'no':
            print("\nTENGA UN FELIZ DÍA\n")
            caja = False
            os.system("PAUSE")
        else:
            print("\nINGRESO UNA INCONGRUENCIA, DEBE INGRESAR SI O NO")
            caja = True

def calculos(producto, cantidad,expediente_price):
    '''obtener el costo de cada producto segun la cantidad y el precio '''
    precio = float(expediente_price[producto])
    gasto = precio * int(cantidad)
    return gasto
def sumar(lista):
    '''Calcular el gasto total de cada cliente, seguna la cantidad de productos
    que adquieran'''
    suma = 0.00
    #volver los valores caracter de la lista a tipo flotante
    try:
        for i in range(len(lista)):
            float(lista[i])
            suma += float(lista[i])
    except:
        print("No es posible realizar la conversion")
    return suma
principal()