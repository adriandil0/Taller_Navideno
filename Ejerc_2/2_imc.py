import os
isContinue = ''
def indiceMasaCorporal(altura, peso):
    imc = round((peso/altura**2),2)
    status=['normal','sobrepeso','obesidad I', 'obesidad II', 'obesidad III']
    if imc >= 18.5 and imc < 25:
        print(f"Su estado es : {status[0]} con un IMC de : {imc}")
    elif imc >= 25 and imc < 30:
        print(f"Su estado es : {status[1]} con un IMC de : {imc}")
    elif imc >= 30 and imc < 35:
        print(f"Su estado es : {status[2]} con un IMC de : {imc}")
    elif imc >= 35 and imc < 40:
        print(f"Su estado es : {status[3]} con un IMC de : {imc}")
    elif imc >= 40:
        print(f"Su estado es : {status[4]} con un IMC de : {imc}")
    else:
        print("Valor fuera de rango")        
    return imc , status

while isContinue == '':
    peso = float(input("Ingrese su peso en [KG]    : "))
    altura = float(input("Ingrese su altura en [m] : "))
    # Llamada a la función
    indiceMasaCorporal(altura, peso)
    decision = input("Presiona enter para hacer otra consulta o finish para terminar : ").lower()
    while decision != 'finish' and decision != '':
        print('Valor invalido\n')
        decision = input("Presiona enter para hacer otra consulta o finish para terminar : ").lower()
        os.system('cls')
    isContinue = decision