### 🔹 **3. Perímetro y área de un rectángulo**

##Escribe un programa que calcule el **perímetro** y el **área** de un rectángulo, dados su largo y ancho. El programa debe validar que ambos valores sean positivos.

##Autor: FREDDY EDU RIVADENEIRA LEON

ladoa = float(input("Lado A: "))
ladob = float(input("Lado B: "))
if ladoa>0 and ladob>0:
    area = ladoa * ladob
    perimetro = (2*ladoa) + (2*ladob)
    print("El valor del area es: ", area)
    print("El valor del perimetro es: ", perimetro)
else:
    print("Al menos uno de los números no es positivo o es igual a 0.")

