# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:29:42 2021

@author: emilien 
"""
import pygame 
from random import *

def aleatoire(max_width, max_height):
    """Fonction qui permet d'avoir une position aléatoire"""
    
    x = randint(0,max_width)
    y = randint(0,max_height)
    
    return (x,y)

pygame.init()


pygame.display.set_caption("CMI-INFO")


ball = pygame.image.load("franc.png")
Corridor_size = 100
window_size = window_width,window_height = 800,600
screen = pygame.display.set_mode(window_size,pygame.RESIZABLE)
pygame.display.set_caption("Points")
clock = pygame.time.Clock()
fps = 60
#game = Game()

running = True

while running :
    
    # afficher l'arrière plan
    #screen.blit(background,(0,0))
    
    #mettre à jour l'écran 
    pygame.display.flip()
    
    screen.blit(ball,(aleatoire(window_width,window_height)))
    # fermeture
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
    clock.tick(fps)
    pygame.display.update()
   
    