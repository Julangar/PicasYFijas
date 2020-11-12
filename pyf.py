from random import randint

def generar_secreto(cantidad): #Se genera un numero aleatorio sin repeticion
    secreto = []
    while True:
        d = randint(0, 9)
        if d not in secreto:
            secreto.append(d)
        if len(secreto) == cantidad:
            break
    return secreto

def validar_numero(numero): # Se valida que cada digito del numero sea diferente
    if len(numero) == 1:
        return True
    else:
        if numero[0] in numero[1:]:
            return False
        else: 
            return validar_numero(numero[1:])

def validar_longitud(numero,longitud): #Se revisa la longitud del numero
    if len(numero) == longitud:
        return validar_numero(numero)
    else:
        return False


def puntaje(a):
    f = open("archivo.txt","r")
    menor=1000
    puntajes = []
    for i in f:
        i = i.rstrip()
        if not i.startswith(a):
            continue
        score = i.split(",")
        puntajes.append(score)
        puntaje = int(score[1])
        if(menor > puntaje):
            menor = puntaje
    for j in puntajes:
        menor=str(menor)
        if (j[1]==menor):
            print ("El mejor en ",a," digitos es:",j[3]," con ",j[1]," intentos")
    
    


def comprobar(intentos,numero,entrada): #Comienza el juego de picas y fijas
    resultado = ""
    for i in range(intentos):
            fijas = 0
            picas = 0
            if intentos == 1:
                resultado = "perdiste "
                print(resultado)
                intent = 0
                return [len(numero),intent, resultado]
            else:
                for i in range(len(entrada)):
                    if numero[i] == entrada[i]:
                        fijas = fijas + 1
                    elif numero[i] in entrada:
                        picas = picas + 1
                if fijas == len(entrada):
                    resultado = "ganaste"
                    print(resultado)
                    intent = 11 - intentos
                    return [len(numero),intent, resultado]
                intentos= intentos-1
                print("tienes ", fijas, "fijas y tienes ", picas, "picas\n intentos restantes: ",intentos)
                while True:
                    entrada = [int(x) for x in input("Ingrese un numero: ")]
                    if validar_longitud(entrada,len(numero)) == True:
                        break           
                    try:
                        e = validar_longitud(entrada,len(numero))
                        if e == False:
                            quit()
                    except:
                        print("Ingrese un numero valido")
                        continue
                
    
cifras = 0
intentos = 0

while True:
    opcion = input("Este es un juego de picas y fijas, con cuantas cifras desea jugar:\n" #Menu de opciones
    "a.3 cifras(10 intentos)\nb.4 cifras(15 intentos)\nc.5 cifras(20 intentos)\nd. ver puntajes")
    if opcion == "a":
        print("Opción de 3 cifras")
        cifras = 3
        intentos = 10
        s = generar_secreto(cifras)

    elif opcion == "b":
        print("Opción de 4 cifras")
        cifras = 4
        intentos = 15
        s = generar_secreto(cifras)

    elif opcion == "c":
        print("Opción de 5 cifras")
        cifras = 5
        intentos = 20
        s = generar_secreto(cifras)
        
    elif opcion == "d":
        a = input("¿Que puntaje  quiere ver?\n3. para tres cifras\n4. para cuatro cifras\n5. para cinco cifras")
        puntaje(a)
        break
    else:
        print("Fin del juego")
        break

    while True:
        n = [int(x) for x in input("Ingrese un numero: ")]
        if validar_longitud(n,cifras) == True:
            break           
        try:
            e = validar_longitud(n,cifras)
            if e == False:
                quit()
        except:
            print("Ingrese un numero valido")
            continue


    try:
        f = open("archivo.txt", "r")
        f.close()
    except:
        f = open("archivo.txt", "w")
        f.close()
    
    f = open("archivo.txt", "a")
    final = comprobar(intentos, s, n)
    nombre = input("Ingrese su nombre: ")
    final.append(nombre)
    if (final[2]=="ganaste"):
        f.write(str(final[0])+","+str(final[1])+","+str(final[2])+","+str(final[3]+"\n"))
        f.close()
    print(final)

    #Revisar archivo para el ganador de cada acategoria
