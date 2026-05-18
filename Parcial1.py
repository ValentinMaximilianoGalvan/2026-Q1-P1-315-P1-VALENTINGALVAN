
productosinfo = []

opcion = 0

while opcion != 7:
    print("1.Cargar producto \n" 
    "2.Mostrar productos \n" 
    "3.buscar productos por codigo \n" 
    "4.Mostrar producto por precio \n" 
    "5.Mostrar productocon menor stock \n" 
    "6.Calcular valor total del inventario \n"
    "7.Salir"
    )

   

    

    opcion = int(input("Elegir la opcion de forma numerica: "))

    if opcion == 1:
        
        codigo = int(input("Ingrese el codigo de producto: "))
        
        nombre = input("Ingrese el nombre del producto: ")
        
        precio = int(input("ingrese el precio del producto: "))
        
        stock = int(input("introduzca el stock del producto: "))
        

        datos = {
        "codigo" : codigo ,
        "nombre" : nombre ,
        "precio" : precio ,
        "stock"  : stock
                         }
        
        if datos["codigo"] == codigo:
            print("codigo repetido,no valido")
            codigo = int(input("Ingrese el codigo de producto: "))
        else:
            datos.append(codigo)

        datos.append(nombre)    
        if precio <= 0:
            print("No puede ser menor o igual a 0")
            precio = int(input("ingrese el precio del producto: "))
        else:
            datos.append(precio)



        if stock < 0:
            print("No puede ser menor a 0")
            stock = int(input("introduzca el stock del producto: "))
           
        else:
            datos.append(stock)
        productosinfo.append(datos)


    elif opcion == 2:
        for datos["producto"] in productosinfo:
            print(datos["producto"])
    
    elif opcion == 3:
        codigoa_buscar = input("introduca el codigo a bsucar:") 
        for datos["codigo"] in productosinfo:
            if codigoa_buscar == datos["codigo"]:
                print("codigo "+ datos["codigo"] + " encontrado")

            else:
                print("codigo no encontrado")


    elif opcion == 4:
        sorted.datos["precio"]

    elif opcion == 5:
        
        sorted.datos["stock"]
        for datos["stock"] in productosinfo:
            print(datos["producto"], datos["stock"])
            break
    elif opcion == 6:
        for datos["precio"] in productosinfo:
            sumadeprecios += datos["precio"]

        for datos["stock"] in productosinfo:
            sumadestock += datos["stock"]

        print(sumadeprecios * sumadestock)
            


print("Usted salió correctamente")    


        
