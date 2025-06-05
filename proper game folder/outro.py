import pygame
from app import win

def play_outro(win):
    #Gonna be looping through every single photo.. wish me luck
    frame_path = ["outro/1.png", "outro/2.png", "outro/3.png", "outro/4.png", "outro/5.png", 
                "outro/6.png", "outro/7.png", "outro/8.png", "outro/9.png", "outro/10.png",
                "outro/11.png", "outro/12.png", "outro/13.png", "outro/14.png", "outro/15.png", 
                "outro/16.png", "outro/17.png", "outro/18.png", "outro/19.png", "outro/20.png",
                "outro/21.png", "outro/22.png", "outro/23.png", "outro/24.png", "outro/25.png",
                "outro/26.png", "outro/27.png", "outro/28.png", "outro/29.png", "outro/30.png",
                "outro/31.png", "outro/32.png", "outro/33.png", "outro/34.png", "outro/35.png",
                "outro/36.png", "outro/37.png", "outro/38.png", "outro/39.png", "outro/40.png",
                "outro/41.png", "outro/42.png", "outro/43.png", "outro/44.png", "outro/45.png",
                "outro/46.png", "outro/47.png", "outro/48.png", "outro/49.png", "outro/50.png",
                "outro/51.png", "outro/52.png", "outro/53.png", "outro/54.png", "outro/55.png",
                "outro/56.png", "outro/57.png", "outro/58.png", "outro/59.png", "outro/60.png",
                "outro/61.png", "outro/62.png", "outro/63.png", "outro/64.png", "outro/65.png",
                "outro/66.png", "outro/67.png", "outro/68.png", "outro/69.png", "outro/70.png",
                "outro/71.png", "outro/72.png", "outro/73.png", "outro/74.png", "outro/75.png",
                "outro/76.png", "outro/77.png", "outro/78.png", "outro/79.png", "outro/80.png",
                "outro/81.png", "outro/82.png", "outro/83.png", "outro/84.png", "outro/85.png",
                "outro/86.png", "outro/87.png", "outro/88.png", "outro/89.png", "outro/90.png",
                "outro/91.png", "outro/92.png", "outro/93.png", "outro/94.png", "outro/95.png",
                "outro/96.png", "outro/97.png", "outro/98.png", "outro/99.png", "outro/100.png",
                "outro/101.png", "outro/102.png", "outro/103.png", "outro/104.png"]

    for path in frame_path:
        image = pygame.image.load(path).convert_alpha()
        image = pygame.transform.scale(image, (1200, 800))
        win.blit(image, (0, 0))
        pygame.display.update()
        #if the frame rate is weird, change the number here (right now it's half a second per frame)
        pygame.time.wait(500)
