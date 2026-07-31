ids = []
articulos = []
categorias = []
marcas = []
precios = []
cantidades = []
proveedores = []
fechas = []
estados = []
observaciones = []
#--------------------------------------------#
#--|menu_principal_administrador_articulos|--#
#--------------------------------------------#
while True:
    print("menu principal administrador de articulos")
    print("1) crear artículo")
    print("2) editar artículo")
    print("3) eliminar artículo")
    print("4) buscar artículo")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #--------------------#
    #--|crear_articulo|--#
    #--------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_articulo = 1
        else:
            id_articulo = ids[-1] + 1
        articulo = input("nombre del artículo: ")
        categoria = input("categoría: ")
        marca = input("marca: ")
        precio = float(input("precio: "))
        cantidad = int(input("cantidad disponible: "))
        proveedor = input("proveedor: ")
        fecha = input("fecha de ingreso: ")
        estado = input("estado del artículo: ")
        observacion = input("observación: ")
        ids.append(id_articulo)
        articulos.append(articulo)
        categorias.append(categoria)
        marcas.append(marca)
        precios.append(precio)
        cantidades.append(cantidad)
        proveedores.append(proveedor)
        fechas.append(fecha)
        estados.append(estado)
        observaciones.append(observacion)
        print("artículo registrado correctamente.")
        print("id:", id_articulo)
    #---------------------#
    #--|editar_articulo|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar artículo")
            for i in range(len(ids)):
                print(f"{ids[i]} | {articulos[i]} | {categorias[i]} | {marcas[i]} | {precios[i]} | {cantidades[i]} | {proveedores[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {articulos[posicion]} | {categorias[posicion]} | {marcas[posicion]} | {precios[posicion]} | {cantidades[posicion]} | {proveedores[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                articulos[posicion] = input("nuevo artículo: ")
                categorias[posicion] = input("nueva categoría: ")
                marcas[posicion] = input("nueva marca: ")
                precios[posicion] = float(input("nuevo precio: "))
                cantidades[posicion] = int(input("nueva cantidad: "))
                proveedores[posicion] = input("nuevo proveedor: ")
                fechas[posicion] = input("nueva fecha de ingreso: ")
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|eliminar_articulo|--#
    #-----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar artículo")
            for i in range(len(ids)):
                print(f"{ids[i]} | {articulos[i]} | {categorias[i]} | {marcas[i]} | {precios[i]} | {cantidades[i]} | {proveedores[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {articulos[posicion]} | {categorias[posicion]} | {marcas[posicion]} | {precios[posicion]} | {cantidades[posicion]} | {proveedores[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    articulos.pop(posicion)
                    categorias.pop(posicion)
                    marcas.pop(posicion)
                    precios.pop(posicion)
                    cantidades.pop(posicion)
                    proveedores.pop(posicion)
                    fechas.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|buscar_articulo|--#
    #---------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar artículo")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {articulos[posicion]} | {categorias[posicion]} | {marcas[posicion]} | {precios[posicion]} | {cantidades[posicion]} | {proveedores[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            valor_total = 0
            mayor = precios[0]
            menor = precios[0]
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {articulos[i]} | {categorias[i]} | {marcas[i]} | {precios[i]} | {cantidades[i]} | {proveedores[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
                valor_total += precios[i] * cantidades[i]
                if precios[i] > mayor:
                    mayor = precios[i]
                if precios[i] < menor:
                    menor = precios[i]
            promedio = valor_total / len(ids)
            print("estadísticas administrador de artículos")
            print("cantidad de registros:", len(ids))
            print("valor total del inventario: $", round(valor_total, 2))
            print("valor promedio por registro: $", round(promedio, 2))
            print("artículo más costoso: $", round(mayor, 2))
            print("artículo más económico: $", round(menor, 2))
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el programa.")
        break
    else:
        print("opción inválida.")