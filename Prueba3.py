lista_peliculas = ["SPIDERMAN","EL REY LEÓN", "TOY STORY 4"]
lista_asiento = [["🔳"]* 15 for _ in range (10)]

def asientos ():
    for fila in lista_asiento:
        print (*fila, sep= " ", end="\n")

#def elegir_pelicula_asiento_duoc():
#    print (lista_peliculas)
#    selec_pelicula = input("ELIGA QUE PELICULA VER : ")
#    if selec_pelicula == lista_peliculas:
#        print ("PELÍCULA", selec_pelicula, "SELECCIONADA")
#    asientos()
#    selec_asiento = input("SELECCIONE LAS COORDENADAS DEL ASIENTO A ELEGIR: ")
#    fila_elegida,columna_elegida = map (int, selec_asiento.split(","))
#    lista_asiento[fila_elegida - 1][columna_elegida - 1] = "❌"
#    for fila in lista_asiento:
#        print (*fila, sep=" ", end="\n")
#    print ("ASIENTO SELECCIONADO CON EXITO")

def elegir_pelicula_asiento():
    print (lista_peliculas)
    selec_pelicula = input("ELIGA QUE PELICULA VER : ")
    if selec_pelicula == lista_peliculas:
        print ("PELÍCULA", selec_pelicula, "SELECCIONADA")
    asientos()
    selec_asiento = input("SELECCIONE LAS COORDENADAS DEL ASIENTO A ELEGIR: ")
    fila_elegida,columna_elegida = map (int, selec_asiento.split(","))
    lista_asiento[fila_elegida - 1][columna_elegida - 1] = "❌"
    for fila in lista_asiento:
        print (*fila, sep=" ", end="\n")  
    print ("ASIENTO SELECCIONADO CON EXITO")
    confirmar_compra = input(" ¿DESEA CONFIRMAR COMPRA? S/N :").upper()
    if confirmar_compra == "S":
        print ("INGRESE LOS SIGUIENTES DATOS POR FAVOR : ")
        nombre = input("NOMBRE : ").upper()
        asiento = input("ASIENTO ELEGIDO : ")
        boleta = "--COMPRA : "+nombre+"--ASIENTO : "+asiento+"--PELICULA : "+selec_pelicula+"--$2500"
        guardar_compra("compras.txt", boleta)
        print ("COMPRA CONFIRMADA CON EXITO")
    elif confirmar_compra == "N":
        print ("COMPRA CANCELADA")
        print ("VOLVIENDO AL MENÚ...")
        menu()

def guardar_compra(nombre_archivo,contenido):
    archivo = open(nombre_archivo, "a")
    archivo.write(contenido + "\n")
    archivo.close()

          
while True:
    def menu():
        print ("*********************************************")
        print ("*********************************************")
        print ("**********BIENVENIDO A CINE DUOC*************")
        print ("*******-- PELICULAS EN CARTELERA --**********")
        print ("-",lista_peliculas,"-")
        print ("***********[1] ELEGIR PELICULA***************")
        print ("***********[2] VER ASIENTOS DISPONIBLES******")
        print ("***********[3] OPCION ALUMNO DUOC************")
    menu()

    opc = int(input("ESCOGER OPCIÓN A REALIZAR :"))

    if opc == 1:
        elegir_pelicula_asiento()
        otro_asiento = input("¿DESEA RESERVAR OTRO ASIENTO? S/N").upper()
        if otro_asiento == "S":
            asientos()
    elif opc == 2:
        asientos()
        volver_menu = input("PRESIONE ENTER PARA VOLVER AL MENÚ : ")
    elif opc == 3:
        conf_alumno_duoc = input("¿ES USTED ALUMNO DE DUOC? DE SER ASÍ SOLO PODRÁ COMPRAR UNA ENTRADA -- S/N : ").upper()
        if conf_alumno_duoc == "N":
            print ("USTED NO ES ALUMNO DUOC 😕 -- VOLVIENDO A MENÚ PRINCIPAL...")
        elif conf_alumno_duoc == "S":
            print ("USTED SI ES ALUMNO DUOC 😀")
            #if


    



