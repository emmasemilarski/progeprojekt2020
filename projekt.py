import pygame

pygame.init()

mängulaud = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Trips-traps-trull")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()