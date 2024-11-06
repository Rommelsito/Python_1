
continuar = "si"

while continuar.lower() == "si":

    num = int(input("INGRESA UN NUMERO: "))
    
    if num %2 == 0:
        print("ES PAR")
    
    elif num %2 == 1:
        print("ES IMPAR")

    continuar = input("DESEAS CONTINUAR(SI/NO)?: ")

print("FIN DEL PROGRAMA")