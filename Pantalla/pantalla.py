import pygame

ancho = 600
largo = 600

pantalla = pygame.display.set_mode((ancho,largo))

dragon = pygame.image.load("Pantalla/dragon.png")
dragon_cachapa = dragon.get_rect()
dragon_cachapa.topleft = (ancho/2,largo/2)

velocidad = 1
run = True
while run:

    tecla = pygame.key.get_pressed()

    if tecla[pygame.K_RIGHT] and dragon_cachapa.right < ancho:
        dragon_cachapa.x += velocidad
        print("Funciona")

    elif tecla[pygame.K_LEFT] and dragon_cachapa.left > 0:
        dragon_cachapa.x -= velocidad
        print("Funciona")

    elif tecla[pygame.K_UP] and dragon_cachapa.top > 0:
        dragon_cachapa.y -= velocidad
        print("Funciona")

    elif tecla[pygame.K_DOWN] and dragon_cachapa.bottom < largo:
        dragon_cachapa.y += velocidad
        print("Funciona")

    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            run = False
    
    pantalla.blit(dragon,dragon_cachapa)
    pygame.display.update()