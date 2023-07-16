import pygame, sys

from conf import *
from colors import *
from debug import debug
from font import font
from level import Level


bg = pygame.image.load('assets/banner.png')
bg = pygame.transform.scale(bg, (bg.get_width() * 1.8, bg.get_height() * 1.8))


clock = pygame.time.Clock()

class Game:
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Vinland Saga game')
        
        self.clock = pygame.time.Clock()
        self.button_rect = pygame.Rect(250, 250, 300, 100)
        self.button_text = font.render("START", True, WHITE)
        self.info = pygame.image.load('assets/info.png')
        self.info = pygame.transform.scale(self.info, (self.info.get_width() / 13,  self.info.get_height() / 13))
        self.info_rect = self.info.get_rect()
        self.info_rect.bottomright = self.screen.get_rect().bottomright
        self.button_hovered_color = BANANA
        self.button_color = BLUE
        self.button_x = 200  
        self.button_y = 350


        self.level = Level()

        self.button_active = True 


    def run(self):
        running = True
        show_level = False
        while running:
            dt = clock.tick(FPS)
            fps = int(clock.get_fps())

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and self.button_active:
                    if self.button_rect.collidepoint(event.pos):
                        print("Im working")
                        show_level = not show_level  
                        self.button_active = False

                mouse_pos = pygame.mouse.get_pos()
                if self.button_rect.collidepoint(mouse_pos):
                    self.button_color = self.button_hovered_color
                else:
                    self.button_color = BLUE            

            if not show_level:
                self.screen.fill(WHITE)
                self.screen.blit(bg, (0, 0))

              
              

                self.button_rect.topleft = (self.button_x, self.button_y)
                pygame.draw.rect(self.screen, self.button_color, self.button_rect, border_radius=35)
                self.screen.blit(self.button_text, self.button_text.get_rect(center=self.button_rect.center))

                self.screen.blit(self.info, self.info_rect)

                self.button_active = True
            else:
                self.screen.fill(BLACK)
                self.level.run()  # Render the level content when show_level is True
                pygame.display.update()
                self.clock.tick(FPS)

            pygame.display.update()
            self.clock.tick(FPS)

               
            


if __name__ == "__main__":
    game = Game()
    game.run()                  
               



