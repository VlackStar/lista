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