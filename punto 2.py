#Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

#para este ejercicio he decidido que el usuario introduzca dos vectores de 3 dimensiones, aunque la solución es generalizable
#la idea tampoco es hacer hardcoding a todo


lista_productos=[]
i=0

def suma_final(lista_productos): #suma final de los productos obtenidos para obtener el producto punto
    suma_fin=0
    for i in lista_productos:
        suma_fin+=float(i)
    return suma_fin
if __name__=="__main__":
    lista_productos=[]
    x1:float=input("introduzca el valor x del primer vector: ")
    y1:float=input("introduzca el valor y del primer vector: ")
    z1:float=input("introduzca el valor z del primer vector: ")
    vector_1=[x1,y1,z1]
    x2:float=input("introduzca el valor x del segundo vector: ")
    y2:float=input("introduzca el valor y del segundo vector: ")
    z2:float=input("introduzca el valor z del segundo vector: ")
    vector_2=[x2,y2,z2]
    while i< len(vector_1): #uso el while approach porque no me salía con el for approach
        a=float(vector_1[i])
        b=float(vector_2[i])
        i=i+1
        prv=a*b
        lista_productos.append(prv)
        #debido a que .append no funciona dentro de una función, esta parte de código sí o sí tiene que ir aquí
    suma=suma_final(lista_productos)
    print("usted ingreso el vector 1 con valores XYZ:",vector_1)
    print("usted ingreso el vector 2 con valores XYZ:",vector_2)
    print("cuyo producto punto o producto escalar es: ",suma)


    