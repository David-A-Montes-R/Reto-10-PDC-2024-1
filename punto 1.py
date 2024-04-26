#Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

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