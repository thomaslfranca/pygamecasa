# tutorial no youtube:
# https://www.youtube.com/watch?v=k7PLSocEREs&list=PLJ8PYFcmwFOxtJS4EZTGEPxMEo4YdbxdQ&index=2

# Exercicio;
# O video acima é parte de uma playlist. 
# Ele inicia um jogo "vazio" com uma tela preta
# O video seguinte, mostra como desenhar um retangulo.
# Assista mais alguns videos e mexa neste arquivo pra tentar desenhar uma casinha tosquinha

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

LARGURA, ALTURA = 1024, 680

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogaço do Thomas')
relogio = pygame.time.Clock()

x = 0
y = 0

while True:
    relogio.tick(30)
    # escuta os eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
   
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20
    if x > LARGURA:
        x = -340
    if x < -340:
        x = LARGURA
    if y > ALTURA:
        y = -280
    if y < -280:
        y = ALTURA

    # desenha a tela
    tela.fill((0, 0, 0))
    # casa = 340 x 280
    pygame.draw.rect(tela, (255,140,0), (x + 20, y + 40,300,220)) # corpo
    pygame.draw.rect(tela, (255,0,0), (x + 140, y + 190,50,70))
    pygame.draw.rect(tela, (0,120,255), (x + 60, y + 150,50,50))
    pygame.draw.rect(tela, (0,120,255), (x + 220, y + 150,50,50))
    pygame.draw.rect(tela, (135,40,0), (x, y,340,60))  # teto

    pygame.display.update()
