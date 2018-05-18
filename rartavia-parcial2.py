#Examen Parcial II 
#Autor: Ricardo Artavia Solano

#Ejercicio 1
#Entradas:
#Salidas:
#Restricciones:

def invertir(lista):
    return invertir_auxiliar(lista,0,1)

def invertir_auxiliar(lista,indice1,indice2):
    if indice1 == len(lista)+3:
        return lista

    elif indice2 == len(lista)+1:
        return invertir_auxiliar(lista,indice1,1)

    else:
        lista[indice2]=lista[indice2-1] and lista[indice2-1]=lista[indice2]
        return invertir_auxiliar(lista,indice1+1,indice2+1)


#Ejercicio 2.1
#Entradas:Matriz cuadrada nxn
#Salidas:True o False
#Restricciones:los numeros de la matriz no pueden repetirse

def consecutivos(lista):
    return consecutivos_aux(lista,0,0)

def consecutivos_aux(lista,indice1,indice2):
    if consecutivos2(lista,lista[indice1][indice2],indice1,indice2,0,1) == True:
        return False

    elif consecutivos2(lista,lista[indice1][indice2],indice1,indice2,0,1) == False:
        if indice2 == len(lista(0)):
            return consecutivos_aux(lista,indice1+1,0)
        else:
            return consecutivos_aux(lista,indice1,indice2+1)

def consecutivos2(lista,numero,indice1,indice2,indice3,indice4):
    if numero == lista[indice3][indice4]:
        return True

    elif indice4 == len(lista[0]):
        return consecutivos2(lista,numero,indice1,indice2,indice3+1,0)
    else:
        return False
        

#Ejercicio 2.2
#Entradas:Matriz cuadrada nxn
#Salidas:True o False
#Restricciones:los numeros de la matriz no pueden repetirse

def es_magico(lista):
    return es_magico_aux(lista,columnas(lista,0,0,0),filas(lista,0,0,0),diagonal(lista,0,0,0))

def es_magico_aux(lista,suma1,suma2,suma3):
    if suma1 == sum2 and suma2 == suma3:
        return True
    else:
        False

def filas(lista,indice1,indice2,sum1):
    if indice1 == len(lista):
        return sum1
    elif indice2 == len(lista[0]):
        return filas(lista,indice1+1,0,sum1)
    else:
        return filas(lista,indice1,indice2+1,sum1+lista[indice1][indice2])

def columnas(lista,indice3,indice4,sum2):
    if indice2 == len(lista):
        return sum2

    elif indice1 == len(lista[0]):
        return columnas(lista,indice1 + 1,0,sum2)

    else:
        return columnas(lista,indice1+1,indice2+1,suma+lista[indice1][indice2])
