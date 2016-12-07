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
def sublistas (lista): #Esto no me funciona :(
    id_paciente=lista[0]
    fase=lista[1]
    temperaturas=float(lista[2:])
    return id_paciente, fase, temperaturas    