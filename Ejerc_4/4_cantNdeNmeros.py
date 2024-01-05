# Inicializar las variables
totalNumeros = 0
totalPares = 0
sumaPares = 0
sumaImpares = 0
totalImpares = 0
menorDiez = 0
entreVeinteandCincuenta = 0
mayorCien = 0

while True:
    # Solicitar un número al usuario
    num = int(input("Ingrese un número entero positivo (o un número negativo para terminar): "))
    
    # Verificar si el número es negativo
    if num < 0:
        break
    
    # Actualizar las estadísticas
    totalNumeros += 1
    if num % 2 == 0:
        totalPares += 1
        sumaPares += num
    else:
        totalImpares += 1
        sumaImpares += num
    if num < 10:
        menorDiez += 1
    if 20 <= num <= 50:
        entreVeinteandCincuenta += 1
    if num > 100:
        mayorCien += 1

# Calcular los promedios
promedio_pares = sumaPares / totalPares if totalPares > 0 else 0
promedio_impares = sumaImpares / totalImpares if totalImpares > 0 else 0

# Imprimir el reporte
print(f"Total de números ingresados: {totalNumeros}")
print(f"Total de números pares ingresados: {totalPares}")
print(f"Promedio de los números pares: {promedio_pares}")
print(f"Promedio de los números impares: {promedio_impares}")
print(f"Cantidad de números menores que 10: {menorDiez}")
print(f"Cantidad de números entre 20 y 50: {entreVeinteandCincuenta}")
print(f"Cantidad de números mayores que 100: {mayorCien}")