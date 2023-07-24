import pygame
from conf import *
from support import *

PLAYER_SPEED = 7
# IMAGE_SCALE_FACTOR = 1.2


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacles_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('assets/viking.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width()), int(self.image.get_height())))
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.import_player_assets() 
        self.direction = pygame.math.Vector2()
        self.speed = PLAYER_SPEED
        self.baseattacking = False
        self.additionalattacking = False
        self.inventory = False
        self.attackcooldown  = 500
        self.attacktime = None
        self.obstacles_sprites = obstacles_sprites

         

        
    def import_player_assets(self):
        char_path = 'assets/attacks/'
        self.anims = {
            'viking_attack_axe': [],
            'viking_attack_sword': [],
        }

        for anim in self.anims.keys():
            #TODO go through all the images in the folder, create a path and import imgs into self.anims


            for i in range(0, 1):
                path = char_path + anim + str(i) + '.png'
                self.anims[anim] = import_folder(path)           
            print(self.anims)    

    


    def handle_input(self):
        keys = pygame.key.get_pressed()


        #movements    
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0


        #basin attack 
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONDOWN or keys[pygame.K_LCTRL]) and not self.baseattacking:
                self.attacktime = pygame.time.get_ticks()
                self.baseattacking= True
                print("basic attack")


        #super attack(axe)

        if keys[pygame.K_SPACE] and not self.additionalattacking:
            self.additionalattacking = True
            self.attacktime = pygame.time.get_ticks()
            print("axe attack")

         

        #inventory
        if keys[pygame.K_e] and not self.inventory:
            self.inventory = True
            self.attacktime = pygame.time.get_ticks()
            print("inventory")
            
    
            
            


    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * self.speed
        self.collision("horizontal")
        self.hitbox.y += self.direction.y * self.speed
        self.collision("vertical")
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacles_sprites:
                if self.hitbox.colliderect(sprite.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    elif self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == "vertical":
            for sprite in self.obstacles_sprites:
                if self.hitbox.colliderect(sprite.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    elif self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.handle_input()
        self.cooldowns()
        self.move()


    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.baseattacking or self.additionalattacking or self.inventory:
            if current_time - self.attacktime >= self.attackcooldown:
                self.baseattacking = False
                self.additionalattacking = False
                self.inventory = False
                
   
        
        
      
        
