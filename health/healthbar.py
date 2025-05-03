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
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w, self.h))

health_bar = HealthBar(250, 200, 300, 40, 100)

#call upon screen to draw healthbar onto window
    #draw health bar
    #health_bar.draw(screen)