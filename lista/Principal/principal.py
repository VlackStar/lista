'''
Created on 1 dic. 2016

@author: MariaJesus
'''
"Este es el menu principal de la funcion"
from listas.listas import crearlista
from listas.listas import sublistas
from listas.listas import texto
from listas.listas import flotante
if __name__ =="__main__":
    l=[]
    crearlista(l)
while True:
        respuesta=input("¿Desea introducir más datos? ")
        if respuesta=="Sí" or respuesta=="Si" or respuesta=="sí" or respuesta=="si":
            crearlista(l)
            print(l)
        else:
            print("Ya tenemos lista :D!!")
            break
print(flotante (l))
print(texto (l))