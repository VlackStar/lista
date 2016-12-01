'''
Created on 1 dic. 2016

@author: MariaJesus
'''
"Este es el menu principal de la funcion"
from Crear_Lista.crear_lista import crearlista
if __name__ =="__main__":
    l=lista=[]
    crearlista(l)
while True:
        respuesta=input("¿Desea introducir más datos? ")
        if respuesta=="Sí" or respuesta=="Si" or respuesta=="sí" or respuesta=="si":
            crearlista(l)
            print(lista)
        else:
            print("Ya tenemos lista :D!!")
            break