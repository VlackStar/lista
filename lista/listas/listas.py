'''
Created on 30 nov. 2016

@author: MariaJesus
'''
"En esta función vamos a crear la lista a través de un bucle"
def crearlista (lista):
    try:
        ele=input("Introduce elementos a la lista: ")
        lista.append(ele)
    except:
        print("Error")
def sublistas (lista):
    id_paciente=lista[0]
    fase=lista[1]
    temperaturas=float(lista[2:])
    return id_paciente, fase, temperaturas
def flotante (lista):
    temperaturas=lista[2:]
    for numero in range(len(temperaturas)):
        temperaturas[numero]=float(temperaturas[numero])
    return temperaturas
def texto (lista):
    cadena_texto=lista[0:]
    for numero1 in range (len(cadena_texto)):
        cadena_texto[numero1]=str(cadena_texto[numero1])
    return cadena_texto
    
    