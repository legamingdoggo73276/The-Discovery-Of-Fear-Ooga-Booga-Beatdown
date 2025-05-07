import pygame

pygame.init()

#1200 x 800
screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Health Bar')

class HealthBar():
    #for the actual health bar visual
    # # x, y coordinates, width and height (of the health bar rectangle)
    def __init__(self, x, y, w, h, max_hp): 
        self.x = x
        self.y = y 
        self. w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self, surface):
        #calculate health ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "black", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w * ratio, self.h))

#health_bar = HealthBar(250, 200, 300, 40, 100)   original
health_bar = HealthBar(980, 50, 200, 30, 100)

#call upon screen to draw health bar onto window
    #draw health bar
    #health_bar.draw(screen)

run = True
while run:
    screen.fill("indigo")
    
    health_bar.hp = 50
    health_bar.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()

pygame.quit()
