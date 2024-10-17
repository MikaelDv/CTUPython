import pygame

pygame.init()

screen = pygame.display.set_mode((800,600),0,32)

sair = False
while not sair:

    # Regras

    # Imagem
    altura_max = 400
    largura_max = 400
    screen.fill((0,0,0))
    for i in range(10):
        if i%2 == 0:
            altura = 40 * (i + 1)
            deslocamento = altura//2
            y = altura_max - (100 + deslocamento)
            pygame.draw.ellipse(screen, (255,255,0), ((100,y), (400,altura)), 2)

    for i in range(10):
        if i%2 == 0:
            largura = 40 * (i + 1)
            deslocamento = largura//2
            x = largura_max - (100 + deslocamento)
            pygame.draw.ellipse(screen, (255,255,0), ((x, y), (largura,altura)), 2)
    pygame.display.update()

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True