from random import randint

def generar_secreto(cantidad):
    secreto = []
    while True:
        d = randint(0, 9)
        if d not in secreto:
            secreto.append(d)
        if len(secreto) == cantidad:
            break
    return secreto

def validar_numero(numero):
    if len(numero) == 1:
        return True
    else:
        if numero[0] in numero[1:]:
            return False
        else: 
            return validar_numero(numero[1:])

def validar_longitud(numero,longitud):
    if len(numero) == longitud:
        return validar_numero(numero)
    else:
        return False

def comprobar(intentos,numero,entrada):
    resultado = ""
    for i in range(intentos):
            fijas = 0
            picas = 0
            if intentos == 1:
                resultado = "perdiste "
                print(resultado)
                return [intentos, resultado]
            else:
                for i in range(len(entrada)):
                    if numero[i] == entrada[i]:
                        fijas = fijas + 1
                    elif numero[i] in entrada:
                        picas = picas + 1
                if fijas == len(entrada):
                    resultado = "ganaste"
                    print(resultado)
                    return [intentos, resultado]
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
    opcion = input("Este es un juego de picas y fijas, con cuantas cifras desea jugar:\n"
    "a.3 cifras(10 intentos)\nb.4 cifras(15 intentos)\nc.5 cifras(20 intentos)\n")
    if opcion == "a":
        print("opcion de 3 cifras")
        cifras = 3
        intentos = 10
        s = generar_secreto(cifras)
        print(s)
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

        print(n)
        final = comprobar(intentos, s, n)
        print(final)
        nombre = input("Ingrese su nombre: ")
        final.append(nombre)
        print(final)

    elif opcion == "b":
        print("opcion de 4 cifras")
        cifras = 4
        s = generar_secreto(cifras)
        print(s)
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

        print(n)
        final = comprobar(intentos, s, n)
        print(final)
        nombre = input("Ingrese su nombre: ")
        final.append(nombre)
        print(final)

    elif opcion == "c":
        print("opcion de 5 cifras")
        cifras = 5
        intentos = 20
        s = generar_secreto(cifras)
        print(s)
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

        print(n)
        final = comprobar(intentos, s, n)
        print(final)
        nombre = input("Ingrese su nombre: ")
        final.append(nombre)
        print(final)
    else:
        print("opcion invalida")
        break