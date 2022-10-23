import pygame

LARGURA, ALTURA = 1024, 680

class Casa():
    x = 0
    y = 0

    def __init__(self, tela):
        self.tela = tela
    
    def constroi_tiro(self):
        tiro = Tiro(self.tela)
        tiro.x = self.x + 210
        tiro.y = self.y + 175
        return tiro

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        if self.x > LARGURA:
            self.x = -340
        if self.x < -340:
            self.x = LARGURA
        if self.y > ALTURA:
            self.y = -280
        if self.y < -280:
            self.y = ALTURA
    
    def desenha(self):
        # casa = 340 x 280
        pygame.draw.rect(self.tela, (255,140,0), (self.x + 20, self.y + 40,300,220)) # corpo
        pygame.draw.rect(self.tela, (255,0,0), (self.x + 140, self.y + 190,50,70))
        pygame.draw.rect(self.tela, (0,120,255), (self.x + 60, self.y + 150,50,50))
        pygame.draw.rect(self.tela, (0,120,255), (self.x + 220, self.y + 150,50,50))
        pygame.draw.rect(self.tela, (135,40,0), (self.x, self.y, 340, 60))  # teto


class Tiro():
    x = 100
    y = 100

    def __init__(self, tela):
        self.tela = tela
    
    def move(self):
        self.x += 35

    def desenha(self):
        pygame.draw.circle(self.tela, (191,64,191), (self.x, self.y), 15)
