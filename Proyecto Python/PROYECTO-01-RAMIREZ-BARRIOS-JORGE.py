#Importación de librerias y cadenas predeterminadas de datos de ventas
import getpass
from os import system
import listas as l

#Declaración de funciones, procesos que pude reciclar por la frecuencia con la que lo utilizaba y lo básico de su estructura

#Ordenamiento de arreglos
def orden(best) :
    for k in range(len(best)-1,0,-1):
        for l in range(k):
            if best[l]<best[l+1]:
                temp = best[l]
                best[l] = best[l+1]
                best[l+1] = temp
    return best
#Impresion de datos con formato
def impresion(best, tipo):
            if tipo == "ventas":
                Tabla = """\
+------------------------------------------------------------------------------------------------------------------------------------------------+
| Ventas     ID         Producto                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------|
{}
+------------------------------------------------------------------------------------------------------------------------------------------------+\
"""
                Tabla = (Tabla.format('\n'.join("| {:<10} {:<10} {:<120} |".format(*fila)
                 for fila in best)))
                print (Tabla)
            if tipo == "busquedas":
                Tabla = """\
+------------------------------------------------------------------------------------------------------------------------------------------------+
| Busquedas  ID         Producto                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------|
{}
+------------------------------------------------------------------------------------------------------------------------------------------------+\
"""
                Tabla = (Tabla.format('\n'.join("| {:<10} {:<10} {:<120} |".format(*fila)
                 for fila in best)))
                print(Tabla)
            if tipo == "reseña":
                Tabla = """\
+------------------------------------------------------------------------------------------------------------------------------------------------+
| Reseña     ID         Producto                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------|
{}
+------------------------------------------------------------------------------------------------------------------------------------------------+\
"""
                Tabla = (Tabla.format('\n'.join("| {:<10} {:<10} {:<120} |".format(*fila)
                 for fila in best)))
                print (Tabla)
            if tipo == "years":
                Tabla = """\
+------------------------------+
| Ventas     Año               |
|------------------------------|
{}
+------------------------------+\
"""
                Tabla = (Tabla.format('\n'.join("| {:<10} {:<10} {:<6} |".format(*fila)
                 for fila in best)))
                print (Tabla)
                
            if tipo == "months":
                Tabla = """\
+------------------------------+
| Mes        Ventas  Ingresos  |
|------------------------------|
{}
+------------------------------+\
"""
                Tabla = (Tabla.format('\n'.join("| {:<10} {:<10} {:<6} |".format(*fila)
                 for fila in best)))
                print (Tabla)

            if tipo == "bestmonths":
                Tabla = """\
+------------------------------+
| Ventas     Mes               |
|------------------------------|
{}
+------------------------------+\
"""
                Tabla = (Tabla.format('\n'.join("| {:<10} {:<10} {:<6} |".format(*fila)
                 for fila in best)))
                print (Tabla)                
#Ordenamiento de arreglos inverso
def ordeni(best) :
    for k in range(len(best)-1,0,-1):
        for l in range(k):
            if best[l]>best[l+1]:
                temp = best[l]
                best[l] = best[l+1]
                best[l+1] = temp
    return best
            
#Declaración de usuario y contraseña
user="root" 
passw="root" 

#Sistema de control de ingreso, se permiten tres intentos para ingresar el usuario y contraseña correctos. Por cada fallo se limpia la pantalla y se despliega un mensaje de error junto con los intentos restantes.
#En caso de que el usuario falle los tres intentos el programa terminara su ejecución y en caso contrario puede ingresar al sistema principal.

for attempts in range(3, 0, -1):
  print("***  Sistema de login  *** \n")
  try_user = input("Ingrese el Usuario: ") 
  try_pass = getpass.getpass(prompt="Contraseña: ")  
  system("cls")
  if try_user == user and try_pass == passw:
    break
  elif attempts==1:
    print("Limite de intentos alcanzados")
    exit(0)
  else:
    print("Contraseña o usuario incorrecto")
    print("Intentos restantes: "+ str(attempts-1))

#Sistema principal, el sistema principal muestra las opciones disponibles para el usuario y espera que seleccione una, al hacerlo pasa por validaciones.

opcion = 0
while opcion != "10":
  system("cls")
  print("***  Bienvenido al Sistema de Control  ***\n\n" )
  print("[1] Productos más vendidos \n")
  print("[2] Productos más buscados \n")
  print("[3] Productos menos vendidos por categoría \n")
  print("[4] Productos menos buscados \n")
  print("[5] Mejores reseñas \n")
  print("[6] Peores reseñas \n")
  print("[7] Ingresos y ventas \n")
  print("[10] Salir \n")
  opcion = input("Ingrese la opción: ")
  system("cls")
  """
  This is the LifeStore-SalesList data:
  lifestore-searches = [id_search, id product]
  lifestore-sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
  lifestore-products = [id_product, name, price, category, stock]
  """
  #Se comprueba que el valor seleccionado este dentro del rango de opciones disponibles y que sea valido
  try:
      if int(opcion) in range(1,8):
        supp_list = []
        best = []
        categories = []

        #Opcion 1: Listado de los 100 productos más vendidos
        if int(opcion) == 1:
            supp_list = []
            best = []         
            #Lleno una lista con los productos que han sido vendidos excluyendo las devoluciones
            for sales in l.lifestore_sales:
                if sales[4] != 1:
                    supp_list.append(sales[1])
            #Llleno una lista con la cantidad de veces que ha sido vendido un proudcto junto a su id y nombre
            for product in l.lifestore_products:
                best.append([supp_list.count(product[0]),product[0], product[1]])
            #Llamo al metodo orden creado previamente para acomodar el arreglo de mayor a menor con referencia a las ventas
            best = orden(best)
            #Me aseguro que las ventas a mostrar sean las mejores 100
            print("Lista de los 100 productos mas vendidos \n\n")
            if(len(best) > 100):
                best = best[:100]
            #Llamo al metodo impresion creado previamente para concanenar los datos y posteriormente imprimirlos
            impresion(best,"ventas")
            input("Continuar")

        #Opcion 2: Listado de los 100 productos con mayores busquedas
        if int(opcion) == 2:
            supp_list = []
            best = []   
            #Lleno una lista con los productos que han sido buscados
            for serch in l.lifestore_searches:
                supp_list.append(serch[1])
            #Llenado de una lista con la cantidad de veces que ha sido buscado un producto junto a su id y nombre
            for product in l.lifestore_products:
                best.append([supp_list.count(product[0]), product[0], product[1]])
            #Llamo al metodo orden creado previamente para acomodar el arreglo de mayor a menor con referencia a las busquedas
            best = orden(best)
            #Me aseguro que las ventas a mostrar sean las mejores 100
            print("Lista de los 100 productos mas vendidos \n\n")
            if(len(best) > 100):
                best = best[:100]
            #Llamo al metodo impresion creado previamente para concanenar los datos y posteriormente imprimirlos
            impresion(best,"busquedas")
            input("Continuar")
            
        #Opcion 3: Listar los 50 productos con menores ventas por categoría
        if int(opcion) == 3:
            categories = []
            for i in l.lifestore_products:
                if i[3] not in categories:
                    categories.append(i[3])
            #Se lista como opciones las categorias encontradas y se espera una seleccion
            try:
                while int(opcion) != len(categories)+1:
                    print("Seleccione la categoría a revisar: \n")
                    for categorie in categories:
                        print("["+str(categories.index(categorie)+1)+"] "+categorie)
                    print("["+str(len(categorie))+"] Regresar")
                    opcion = input("\nSeleccione una opción: ")
                    system("cls")
                    supp_list = []
                    best = []
                    #Se comprueba que la seleccion este dentro del rango 
                    if int(opcion) in range(1,len(categories)+1):
                        categorie = categories[int(opcion)-1]
                        #Ingreso en un arreglo todas las ventas excluyendo las devoluciones
                        for sales in l.lifestore_sales:
                            if(sales[4]) != 1:
                                supp_list.append(sales[1])
                        #Compruebo los productos y el que este dentro de la catetoria seleccionada se comparara con las ventas del arreglo supp_lis
                        #Al comprobarse se ingresa en un arreglo                                
                        for product in l.lifestore_products:
                            if product[3] == categorie:
                                best.append([supp_list.count(product[0]), product[0], product[1]])
                        #Llamo al metodo orden creado previamente para acomdar el arreglo de menor a mayor con referencia a las ventas de esta categoria
                        best = ordeni(best)
                        #Me aseguro que las ventas de esta categoria a mostrar sean las peores 50
                        if len(best) > 50:
                            best = best[:50]
                        #Llamo al metodo impresion creado previamente para concanenar los datos y posteriormente imprimirlos
                        impresion(best,"ventas")
                        input("Continuar...")
                        system("cls")
            except:
                print("Ingrese una opción valida.")
                        
        #Opcion 4: Listar los 100 productos con menores ventas por categoria
        if int(opcion) == 4:
            categories = []
            for i in l.lifestore_products:
                if i[3] not in categories:
                    categories.append(i[3])
            #Se lista como opciones las categorias encontradas y se espera una seleccion
            try:
                while int(opcion) != len(categories)+1:
                    print("Seleccione la categoría a revisar: \n")
                    for categorie in categories:
                        print("["+str(categories.index(categorie)+1)+"] "+categorie)
                    print("["+str(len(categorie))+"] Regresar")
                    opcion = input("\nSeleccione una opción: ")
                    system("cls")
                    supp_list = []
                    best = []
                    #Se comprueba que la seleccion este dentro del rango 
                    if int(opcion) in range(1,len(categories)+1):
                        categorie = categories[int(opcion)-1]
                    #Ingreso en un arreglo todas las busquedas realizadas
                    for search in l.lifestore_searches:
                        supp_list.append(search[1])
                    #Compruebo los productos y los que pertenezcan a la categoria seleccionada seran contados dentro del arreglo supp_list
                    #Al comprobarse se ingrsea a un arreglo                        
                    for product in l.lifestore_products:
                        if product[3] == categorie:
                            best.append([supp_list.count(product[0]), product[0], product[1]])
                    #Llamo al metodo orden creado previamente para acomdar el arreglo de menor a mayor con referencia a las busquedas de esta categoria
                    best = ordeni(best)
                    #Me aseguro que las busquedas de esta categoria a mostrar sean las peores 100
                    if len(best) > 100:
                        best = best[:100]
                    #Llamo al metodo impresion creado previamente para concanenar los datos y posteriormente imprimirlos
                    impresion(best,"busquedas")
                    input("Continuar...")
                    system("cls")
            except:
                print("Ingrese una opción valida.")

        #Opcion 5: Listar los 20 productos con mejores reseñas
        if int(opcion) == 5:
            supp_list = []
            best = []
            #Recorro todo el arreglo de productos
            for product in l.lifestore_products:
                count = 0;
                val = 0;
                #Recorro todo el arreglo de ventas
                for sales in l.lifestore_sales:
                    #Verifico si el producto tiene alguna venta de tenerla sumo a val e incremento count
                    if product[0] == sales[1]:
                        val += sales[2]
                        count += 1
                #Agrego a un arreglo todos los productos que tengan por lo menos una reseña junto a su id y nombre
                if count != 0:
                    best.append([round(val/count,2), product[0], product[1]])
            #Llamo al metodo orden creado previamente para acomdar el arreglo de mayor a menor con referencia a las reseñas generalbes del producto
            best = orden(best)
            #Me aseguro que las reseñas a mostrar sean las mejores 20
            if len(best) > 20:
                best = best[:20]
            #Llamo al metodo impresion creado previamente para concanenar los datos y posteriormente imprimirlos
            impresion(best, "reseña")
            input("Continuar...")

        #Opcion 6: Listar los 20 productos con peores reseñas
        if int(opcion) == 6:
            supp_list = []
            best = []
            #Recorro todo el arreglo de productos
            for product in l.lifestore_products:
                count = 0;
                val = 0;
                #Recorro todo el arreglo de ventas
                for sales in l.lifestore_sales:
                    #Verifico si el producto tiene alguna venta de tenerla sumo a val e incremento count
                    if product[0] == sales[1]:
                        val += sales[2]
                        count += 1
                #Agrego a un arreglo todos los productos que tengan por lo menos una reseña junto a su id y nombre
                if count != 0:
                    best.append([round(val/count,2), product[0], product[1]])
            #Llamo al metodo orden creado previamente para acomdar el arreglo de menor a mayor con referencia a las reseñas generalbes del producto
            best = ordeni(best)
            #Me aseguro que las reseñas a mostrar sean las peores 20
            if len(best) > 20:
                best = best[:20]
            #Llamo al metodo impresion creado previamente para concanenar los datos y posteriormente imprimirlos
            impresion(best, "reseña")
            input("Continuar...")

        #Opcion 7: Mostrar el total de ingresos y ventas promedio mensuales, total anuales y meses con más ventas del año
        if int(opcion) == 7:
            years = []
            var = []
            while opcion != "4":
                try:
                    system("cls")
                    print("[1] Ventas e ingresos promedio mensuales \n")
                    print("[2] Ventas anuales \n")
                    print("[3] Meses con mayores ventas \n")
                    print("[4] Regresar \n")  
                    opcion = input("Ingrese la opción: ")
                    if int(opcion) in range(1,4):

                        #Mostrar las ventas e ingresos promedio mensuales
                        if int(opcion) == 1:
                            months = []
                            best = []
                            for sales in l.lifestore_sales:
                                var = sales[3].split("/")
                                if var[1] not in months:
                                    months.append(var[1])
                            for month in months:
                                global_sales = 0
                                income = 0
                                for sales in l.lifestore_sales:
                                    var = sales[3].split("/")
                                    if var[1] == month:
                                        global_sales +=1
                                        for product in l.lifestore_products:
                                            if sales[1] == product[0]:
                                                income += product[2]
                                best.append([month, global_sales, income])
                            orden(best)
                            impresion(best,"months")
                            input("Continuar")                            

                        #Mostrar las ventas anuales
                        if int(opcion) == 2:
                            years = []
                            best = []
                            for sales in l.lifestore_sales:
                                var = sales[3].split("/")
                                if var[2] not in years:
                                    years.append(var[2])
                            for year in years:
                                global_sales = 0
                                for sales in l.lifestore_sales:
                                    var = sales[3].split("/")
                                    if year == var[2]:
                                        global_sales += 1
                                best.append([global_sales, year, ""])
                            impresion(best,"years")                         
                            input("Continuar... ")

                        #Meses con mayores ventas    
                        if int(opcion) == 3:
                            months = []
                            best = []
                            for sales in l.lifestore_sales:
                                var = sales[3].split("/")
                                if var[1] not in months:
                                    months.append(var[1])
                            for month in months:
                                global_sales = 0
                                income = 0
                                for sales in l.lifestore_sales:
                                    var = sales[3].split("/")
                                    if var[1] == month:
                                        global_sales +=1
                                best.append([global_sales, month, ""])
                            orden(best)
                            impresion(best,"bestmonths")
                            input("Continuar")
                                
                except ValueError:
                    print(ValueError)
                    print("Ingrese una opción valida.")
            
      else :
        print("Ingrese una opción valida.")
  except ValueError:
      print("Ingrese una opción valida.")
exit(0)
