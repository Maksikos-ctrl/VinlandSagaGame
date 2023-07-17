import pygame
from conf import *

PLAYER_SPEED = 7
IMAGE_SCALE_FACTOR = 1.8


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacles_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('assets/enemy_vikings.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * IMAGE_SCALE_FACTOR), int(self.image.get_height() * IMAGE_SCALE_FACTOR)))
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26) 
        self.direction = pygame.math.Vector2()
        self.speed = PLAYER_SPEED
        self.obstacles_sprites = obstacles_sprites

    def handle_input(self):
        keys = pygame.key.get_pressed()

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
        self.move()

        
        
      
        
