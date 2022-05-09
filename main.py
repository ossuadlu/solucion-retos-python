from classes.Ciclista import Ciclista

lista=[]
opcion=0
tiempo=0


while (opcion !=3):
    print("**********************************")
    print("           Bienvenido             ")
    print("              MENÚ                ")
    print("**********************************")
    print("1- ingreso de ciclistas: ")
    print("2- ver tiempo menor (ojo primero debes ingresar el ciclista):")
    print("0--> SALIR ")
    print("************************************")

    opcion=int(input("Ingrese una opción: "))

    if  (opcion == 1 ):
        ciclista=Ciclista() #OBJETO
        ciclista.nombre=input("Digite el nombre del ciclista: ")
        ciclista.edad=int(input("Digite edad del ciclista: "))
        ciclista.pais=input("Digite el pais del ciclista: ")
        ciclista.tiempo=int(input("Digite el tiempo del ciclista en minutos: "))
        lista.append(ciclista)
    elif(opcion ==2 ):
        menor=lista[0].tiempo
        nombre=lista[0].nombre

        print(menor)

        for ciclista in lista:
            if (ciclista.tiempo < menor):
                menor=ciclista.tiempo
        print("el menor tiempo es: ",menor, "el nombre del ciclista es: ",nombre)
    elif(opcion ==0):
        print("Gracias por utilizar nuestro software...")
        break
    else:
        print("Ingrese una opcion valida de nuestro sistema... :)")
    