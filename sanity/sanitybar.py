import pygame

pygame.init()

#The basics of the sanity bar is basically the same as the health bar

#1200 x 800
screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sanity Bar')

class SanityBar():
    #for the actual health bar visual
    # # x, y coordinates, width and height (of the health bar rectangle)
    def __init__(self, x, y, w, h, max_sanity): 
        self.x = x
        self.y = y 
        self. w = w
        self.h = h
        self.sanity = max_sanity
        self.max_sanity = max_sanity

    def draw(self, surface):
        #calculate health ratio
        ratio = self.sanity / self.max_sanity
        pygame.draw.rect(surface, "black", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, colour, (self.x, self.y, self.w * ratio, self.h))

#health_bar = HealthBar(250, 200, 300, 40, 100)   original
sanity_bar = SanityBar(980, 50, 200, 30, 100)

run = True
while run:
    screen.fill("indigo")
    
    sanity_bar.sanity = 40

    #sanity bar is a different color, depending on the number
    if sanity_bar.sanity <= 25:
        colour = "red"
    elif sanity_bar.sanity <= 50 and sanity_bar.sanity > 25:
        colour = "yellow"
    else:
        colour = "green"

    sanity_bar.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()

pygame.quit()
