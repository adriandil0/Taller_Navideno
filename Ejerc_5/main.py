from funciones import registrarCiudad, registrarSismo, buscarSismosPorCiudad, informeDeRiesgo

ciudades = []
while True:
    print("\n1. Registrar Ciudad\n2. Registrar Sismo\n3. Buscar sismos por ciudad\n4. Informe de riesgo\n5. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        registrarCiudad(ciudades)
    elif opcion == 2:
        registrarSismo(ciudades)
    elif opcion == 3:
        buscarSismosPorCiudad(ciudades)
    elif opcion == 4:
        informeDeRiesgo(ciudades)
    elif opcion == 5:
        break
    else:
        print("Opción no válida. Intente de nuevo.")