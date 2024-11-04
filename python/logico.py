again = "si"

while again.lower() == "si":

    temperatura = int(input("INGRESA TEMPERATURA: "))
    
    if temperatura <=14 or temperatura >= 37:
        print("NO ES IDEAL PARA IR A LA PLAYA \n")
    
    elif temperatura >14 and temperatura <37:
        print("ES IDEAL PARA IR \n")

    again = input("QUIERES INICIALIZAR OTRA VEZ (SI/NO): ")

print("FIN DEL PROGRAMA")
