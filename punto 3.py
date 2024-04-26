#Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo
lista_números=[1,2,0,6,9,0,8,0,1,0,5,0,987] #este arreglo tiene valores arbitrarios
lista_ceros=[]
def lista_final(lista_números,lista_ceros):
    while 0 in lista_números:
        lista_números.remove(0)
        lista_ceros.append(0)
    lista_final= lista_números+lista_ceros
    return lista_final
if __name__=="__main__":
    print("esta es su lista actual:",lista_números)
    lista_f=lista_final(lista_números,lista_ceros)
    print("esta es la misma lista con los números ""0"" al final",lista_f)