contador=0
sumatoria=0
while contador < 3:
    num=int(input("Ingrese un numero : "))
    if num < 0:
        print("El numero no puede ser negativo")
    else:
        sumatoria=num+sumatoria
        contador+=1
print("*****************************************")
print(f"El resultado de la suma es: {sumatoria}")