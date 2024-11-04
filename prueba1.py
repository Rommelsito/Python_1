#CALCULADORA
#MENU DE OPCIONES
#BUCLE PARA REPETIR LA TAREA OTRA VEZ

continuar = "si"

while continuar.lower() == "si":

    print(" \nOPCIONES.")
    print("<1>.Sumar")
    print("<2>.Restar")
    print("<3>.Multiplicar")
    print("<4>.Dividir \n")
    
    opcion = int(input("INGRESA TU OPCION: "))
    
    if opcion == 1:
        print("VAMOS A SUMAR: ")
    
        num1 = int(input("Introduce un numero: "))
        num2 = int(input("Introduce otro numero: "))
    
        sum = num1 + num2
        print(F"El resultado es {sum} \n")
    
    elif opcion == 2:
        print("VAMOS A RESTAR:")
        
        num1 = int(input("Introduce un numero: "))
        num2 = int(input("Introduce otro numero: "))
    
        rest = num1 - num2
        print(F"El resultado es {rest} \n")
    
    elif opcion == 3:
        print("VAMOS A MULTIPLICAR")
    
        num1 = int(input("Introduce un numero: "))
        num2 = int(input("Introduce otro numero: "))
    
        mult = num1 * num2
        print(F"El resultado de la multiplicacion es {mult} \n")
    
    elif opcion == 4:
        print("VAMOS A DIVIDIR")
    
        num1 = int(input("Introduce un numero: "))
        num2 = int(input("Introduce otro numero: "))
    
        div = num1 // num2
        print(F"El resultado de la division es {div} \n")
    
    else:
        print("OPCION INVALIDA \n")
    
    continuar = input("QUIERES CONTINUAR(SI/NO)?:  ")

print("FIN DEL PROGRAMA")