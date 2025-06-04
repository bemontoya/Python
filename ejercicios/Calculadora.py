while True:
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir")
    op = int(input("¿Que desea hacer?: "))
    if op == 1:
        while True:
            try:
                n1 = int(input("Ingrese el primer número: "))
                n2 = int(input("Ingrese el segundo número: "))
                resultadoSuma = n1 + n2
                print(f"El resultado de la suma es {resultadoSuma}")
                break
            except ValueError:
                print("Debe ingresar un número entero.")
    elif op == 2:
        while True:
            try:
                n1 = int(input("Ingrese el primer número: "))
                n2 = int(input("Ingrese el segundo número: "))
                resultadoResta = n1 - n2
                print(f"El resultado de la resta es {resultadoResta}")
                break
            except ValueError:
                print("Debe ingresar un número entero.")
    elif op == 3:
        while True:
            try:
                n1 = int(input("Ingrese el primer número: "))
                n2 = int(input("Ingrese el segundo número: "))
                resultadoMultiplicacion = n1 * n2
                print(f"El resultado de la multiplicación es {resultadoMultiplicacion}")
                break
            except ValueError:
                print("Debe ingresar un número entero.")      
    elif op == 4:
        while True:
            try:
                n1 = int(input("Ingrese el primer número: "))
                n2 = int(input("Ingrese el segundo número: "))
                resultadoDivision = n1 / n2
                print(f"El resultado de la división es {resultadoDivision}")
                break
            except ValueError:
                print("Debe ingresar un númeor entero.")
            except ZeroDivisionError:
                print("El divisor que está ingresando es 0.")      
    elif op == 5:
        print("Saliendo del programa....")
        break            
            


        

