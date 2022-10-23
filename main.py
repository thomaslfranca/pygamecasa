# tutorial no youtube:
# https://www.youtube.com/watch?v=k7PLSocEREs&list=PLJ8PYFcmwFOxtJS4EZTGEPxMEo4YdbxdQ&index=2

import pygame
from pygame.locals import *
from mundo import Casa, Tiro
from mundo import LARGURA, ALTURA
from sys import exit

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogaço do Thomas')
relogio = pygame.time.Clock()

casa = Casa(tela)
tiros = []

while True:
    relogio.tick(30)
    # escuta os eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
#        if event.type == KEYDOWN:
#            if event.key == pygame.K_SPACE:
#                tiros.append(casa.constroi_tiro())
   
    if pygame.key.get_pressed()[K_a]:
        casa.move(-20, 0)
    if pygame.key.get_pressed()[K_d]:
        casa.move(20, 0)
    if pygame.key.get_pressed()[K_w]:
        casa.move(0, -20)
    if pygame.key.get_pressed()[K_s]:
        casa.move(0, 20)
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        tiros.append(casa.constroi_tiro())
    
    for tiro in tiros:
        tiro.move()

    tela.fill((0, 0, 0))
    casa.desenha()
    for tiro in tiros:
        tiro.desenha()
    pygame.display.update()
