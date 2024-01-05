def registrarCiudad(ciudades):
    ciudad = input("Ingrese el nombre de la ciudad: ")
    ciudades.append([ciudad, []])
    print(f"Ciudad {ciudad} registrada con éxito.")

def registrarSismo(ciudades):
    ciudad = input("Ingrese el nombre de la ciudad: ")
    for i in range(len(ciudades)):
        if ciudades[i][0] == ciudad:
            magnitud = float(input("Ingrese la magnitud del sismo: "))
            ciudades[i][1].append(magnitud)
            print(f"Sismo registrado con éxito en {ciudad}.")
            return
    print("Ciudad no encontrada.")

def buscarSismosPorCiudad(ciudades):
    ciudad = input("Ingrese el nombre de la ciudad: ")
    for i in range(len(ciudades)):
        if ciudades[i][0] == ciudad:
            print(f"Sismos registrados en {ciudad}: {ciudades[i][1]}")
            return
    print("Ciudad no encontrada.")

def informeDeRiesgo(ciudades):
    for ciudad in ciudades:
        promedio = sum(ciudad[1]) / len(ciudad[1])
        if promedio < 2.5:
            riesgo = "Amarillo (Sin riesgo)"
        elif 2.6 <= promedio <= 4.5:
            riesgo = "Naranja (Riesgo medio)"
        else:
            riesgo = "Rojo (Riesgo alto)"
        print(f"Ciudad: {ciudad[0]}, Promedio: {promedio}, Riesgo: {riesgo}")