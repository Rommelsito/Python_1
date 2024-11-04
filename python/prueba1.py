#CALCULADORA
#MENU DE OPCIONES
#BUCLE PARA REPETIR LA TAREA OTRA VEZ

continuar = True

while continuar:

    print(" \n OPCIONES.")
    print("<1>.Sumar")
    print("<2>.Restar")
    print("<3>.Multiplicar")
    print("<4>.Dividir")
    print("<5>.Salir \n")
    
    opcion = int(input("INGRESA TU OPCION: "))
    
    if opcion == 1:
        print("VAMOS A SUMAR \n")
    
        num1 = int(input("Introduce un numero: "))
        num2 = int(input("Introduce otro numero: "))
    
        sum = num1 + num2
        print(F"EL RESULTADO ES: {sum} \n")
    
    elif opcion == 2:
        print("VAMOS A RESTAR \n")
        
        num1 = int(input("Introduce un numero: "))
        num2 = int(input("Introduce otro numero: "))
    
        rest = num1 - num2
        print(F"EL RESULTADO ES: {rest} \n")
    
    elif opcion == 3:
        print("VAMOS A MULTIPLICAR \n")
    
        num1 = int(input("Introduce un numero: "))
        num2 = int(input("Introduce otro numero: "))
    
        mult = num1 * num2
        print(F"EL RESULTADO ES: {mult} \n")
    
    elif opcion == 4:
        print("VAMOS A DIVIDIR \n")
    
        num1 = int(input("Introduce un numero: "))
        num2 = int(input("Introduce otro numero: "))
    
        div = num1 // num2
        print(f"EL RESULTADO ES: {div}")

    elif opcion == 5:
        continuar = False
        print("Saliendo... \n")
    
    else:
        print("OPCION INVALIDA")

print("FIN DEL PROGRAMA")