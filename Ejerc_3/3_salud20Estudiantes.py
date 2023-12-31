conteoStatus={'normal':0,'sobrepeso':0,'obesidad I':0, 'obesidad II':0, 'obesidad III':0}
def indiceMasaCorporal(altura, peso):
    imc = round((peso/altura**2),2)
    if imc >= 18.5 and imc < 25:
        conteoStatus['normal']+=1
    elif imc >= 25 and imc < 30:
        conteoStatus['sobrepeso']+=1
    elif imc >= 30 and imc < 35:
        conteoStatus['obesidad I']+=1
    elif imc >= 35 and imc < 40:
        conteoStatus['obesidad II']+=1
    elif imc >= 40:
        conteoStatus['obesidad III']+=1
    else:
        print("Valor fuera de rango")        
    return imc , conteoStatus

for item in range(19):
    name = input(f"Ingrese nombre del estudiante N° {item+1} : ")
    # edad = int(input(f"Ingrese su edad de {name} : "))
    peso = float(input(f"Ingrese peso de {name} en [KG] : "))
    altura = float(input(f"Ingrese altura de {name} en [m] : "))
    # Llamada a la función
    indiceMasaCorporal(altura, peso)
for estado, conteo in conteoStatus.items():
    print("El resumen del estado corporal de los estudiantes : ")
    print(f"{estado} : {conteo}")