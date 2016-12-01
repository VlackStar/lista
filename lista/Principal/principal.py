'''
Created on 30 nov. 2016

@author: MariaJesus
'''
"En esta función vamos a crear la lista a través de un bucle"
def crearlista (lista):
    ele=input("Introduce elementos a la lista: ")
    lista.append(ele)
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