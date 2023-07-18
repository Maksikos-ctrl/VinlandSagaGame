import pygame



from conf import *
from tileset import Tile
from player import Player
from debug import debug
from support import *
from random import choice

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

        layouts = {
            'boundary': import_csv_layout('maps/ALL/map_FloorBlocks.csv'),
            'grass': import_csv_layout('maps/ALL/map_Grass.csv'),
            'objects': import_csv_layout('maps/ALL/map_LargeObjects.csv'),
        }


        graphics = {
            'grass': import_folder('assets/grass'),
            'objects': import_folder('assets/objects')
        }


       
      

        for style, layout in layouts.items():
            for row, row_tiles in enumerate(layout):
                for col, tile_char in enumerate(row_tiles):
                    if tile_char != '-1':
                    
                        x = col * TILESIZE
                        y = row * TILESIZE
                        

                        #TODO Try to create the obstacle tile by passing the right agruments
                        
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        if style == 'grass':
                            #TODO Cycle through the grass csv and place a Tile with a random grass image

                            random_grass = choice(graphics['grass'])
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'grass', random_grass)
                        if style == 'objects':
                            #TODO Cycle through the objects csv and place a Tile with a random object image
                            surface = graphics['objects'][int(tile_char)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surface)

                            
                        

        #         if tile_char == 'x': 
        #             Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
        #         elif tile_char == 'p':  
                 
        #             self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)

        self.player = Player((2000, 1500), [self.visible_sprites], self.obstacle_sprites)




# sorted sprites by y-coordinate                     
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()


        self.floor_surface = pygame.image.load("maps/ALL/ground.png").convert_alpha()
        self.floor_rect = self.floor_surface.get_rect(topleft=(0,0))

   


    def custom_draw(self, player):

        #TODO # draw the floor and give the camera offset

        # # draw the floor
        # for x in range(0, self.display_surface.get_width(), self.floor_rect.width):
        #     for y in range(0, self.display_surface.get_height(), self.floor_rect.height):
        #         self.display_surface.blit(self.floor_surface, (x, y))


        #drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset

        self.display_surface.blit(self.floor_surface, floor_offset_pos)        
                

        # getting offset    
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y =  player.rect.centery - self.half_height

        # draws all our elems
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_sprite_rect = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_sprite_rect)    


