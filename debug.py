import pygame
from colors import *
from font import font
pygame.init()


def debug(info, y=10, x=10):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, WHITE)
    debug_rec = debug_surf.get_rect(topleft=(x, y))
    pygame.draw.rect(display_surface, BLACK, debug_rec)
    display_surface.blit(debug_surf, debug_rec)