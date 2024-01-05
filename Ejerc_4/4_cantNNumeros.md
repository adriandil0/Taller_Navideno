Problematica: Este código es un programa en Python que solicita al usuario que ingrese números enteros positivos. Calcula varias estadísticas basadas en los números ingresados, como la cantidad total de números, la cantidad de números pares, el promedio de los números pares e impares, y la cantidad de números que caen en ciertos rangos. Cuando el usuario ingresa un número negativo, el programa termina y muestra un resumen de las estadísticas calculadas.

Variables usadas:

Variables de entrada: num (el número ingresado por el usuario).
Variables de salida: totalNumeros, totalPares, sumaPares, sumaImpares, totalImpares, menorDiez, entreVeinteandCincuenta, mayorCien, promedio_pares, promedio_impares (estas variables almacenan las estadísticas calculadas y se imprimen al final).
Bucles y/o condiciones usadas y qué realizan:

Bucle while True: Este bucle se ejecuta indefinidamente hasta que el usuario ingresa un número negativo. Dentro de este bucle, el programa solicita un número al usuario y actualiza las estadísticas basadas en el número ingresado.
Condiciones if/elif/else: Estas condiciones verifican el valor del número ingresado y actualizan las estadísticas correspondientes. Por ejemplo, si el número es par, se incrementa totalPares y se suma el número a sumaPares.