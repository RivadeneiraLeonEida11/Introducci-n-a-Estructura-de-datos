### 🔹 **1. Área y perímetro de un círculo**

##Escribe un programa que calcule el **área** y el **perímetro** de un círculo, dado el valor de su radio. El programa debe validar que el radio sea un valor positivo.
##Autor: FREDDY EDU RAIVADENEIRA LEON
# Area= A= Pi*radio*2
# datos
radio = float(input("Cual es el radio del circluo: "))
Pi = 3.1416
# Formula
area = Pi * radio ** 2
perimetro= 2* Pi * radio
# resultado
print("El area del circulo es: " + str(area))
print("El perimetro del circulo es: " + str(perimetro))