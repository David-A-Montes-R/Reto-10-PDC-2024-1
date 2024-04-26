# Reto 10 PDC 2024-1

<div align='center'>
<figure> <img src="https://i.postimg.cc/HkMddSNw/error-418.png" alt="" width="300" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

## Por: David Alejandro Montes Rodríguez

# 1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
Para este punto simplemente se usa un bucle for para sumar todos los elementos de la lista de números reales ``lista_reales``, cuyos datos fueron ingresados por el usuario. La suma de los números reales se trata como un ``float`` y luego se divide entre el número de valores ingresados, en este caso 5.

```python
def promedio_reales(lista_reales):
    suma_reales=0
    for i in lista_reales:
        suma_reales+=float(i)
        promedio_reales:float=suma_reales/5
    return promedio_reales

if __name__=="__main__":
    real_1:float=input("ingrese el primer número real:")
    real_2:float=input("ingrese el segundo número real:")
    real_3:float=input("ingrese el tercer número real:")
    real_4:float=input("ingrese el cuarto número real:")
    real_5:float=input("ingrese el quinto número real:")
    lista_reales=[real_1,real_2,real_3,real_4,real_5]
    prom=promedio_reales(lista_reales)
    print("el promedio de los números reales es:",prom)
```

# 2. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

En este punto tuve mis complicaciones, porque si bien (y en el código está comentado), para el ejercicio el usuario puede introducir 2 vectores tridimensionales (con coordenadas XYZ), porque es una minoría de casos en la que se requieran más dimensiones, quería hacer que el algoritmo funcionará para vectores de un número indeterminado de dimensiones, así que la idea es que recorriera simultaneamente ambos vectores y fuera multiplicando el valor de cada índice, con su equivalente en el otro vector; para lo cual sirvió usar el ``while approach`` y actualizar el índice por cada iteración. Luego se almacenan los productos de los índices en una lista y se usa un método similar al usado en el punto 1, para sumar todos los productos.

```python
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
```
# 3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo

Para este punto simplemente se agarra una lista con valores númericos arbitrarios, y se usa un ``while`` para borrar los ceros en la lista, luego por cada cero borrado se añade un cero a una lista originalmente vacía, y al final se concatenan ambas listas.

```python
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
```

# 4. Revisar que son los algoritmos de sorting, entender bubble-sort (enlace a implementación).

Adicional a la bibliografía recomendada por el docente, también revisé los siguientes enlaces:

[https://es.wikipedia.org/wiki/Algoritmo_de_ordenamiento](https://es.wikipedia.org/wiki/Algoritmo_de_ordenamiento)


[https://www.youtube.com/watch?v=QH-Z67tjzUo](https://www.youtube.com/watch?v=QH-Z67tjzUo)

Un algoritmo que especialmente me llamó la atención fue el ``library sort`` y los de tipo natural, en los cuales supoongo que la IA puede estar bastante presente.