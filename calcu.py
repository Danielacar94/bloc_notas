# Programa calculadora
while True:
    numero1 = input("Introduce el primer numero: ")
    numero2 = input("Introduce el segundo numero: ")
    operacion = input("Elige una operacion (+, -, *, /): ")

    try:
        numero1 = int(numero1)
        numero2 = int(numero2)

        if operacion == "+":
            resultado = numero1 + numero2
            print(f"El resultado de la suma es: {resultado}")
        elif operacion == "-":
            resultado = numero1 - numero2
            print(f"El resultado de la resta es: {resultado}")
        elif operacion == "*":
            resultado = numero1 * numero2
            print(f"El resultado de la multiplicacion es: {resultado}")
        elif operacion == "/":
            if numero2 == 0:
                print("No se puede dividir por cero")
            else:
                resultado = numero1 / numero2
                print(f"El resultado de la division es: {resultado}")
        else:
            print("Operacion no valida. Usa +, -, * o /")
    except ValueError:
        print("Los valores introducidos no son validos")

    continuar = input("Deseas continuar? (si/no): ").strip().lower()
    if continuar == "no" or continuar == "n":
        print("Saliendo de la calculadora...")
        break

