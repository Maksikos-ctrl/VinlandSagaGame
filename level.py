import pygame

from conf import *
from tileset import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()

 
        self.visible_sprites =  YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()


    def run(self):
        #updating game here
        # TODO add code here to update the game state 
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
       


    def create_map(self):
        for row, row_tiles in enumerate(WORLD_MAP):
            for col, tile_char in enumerate(row_tiles):
                x = col * TILESIZE
                y = row * TILESIZE

                if tile_char == 'x': 
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                elif tile_char == 'p':  
                 
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)



# sorted sprites by y-coordinate                     
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()


    def custom_draw(self, player):

        # getting offset    
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y =  player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_sprite_rect = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_sprite_rect)    


