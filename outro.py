#pip install opencv-python 

import cv2

class cell_9(Map):
    #input white screen (image)
    colour = pygame.transform.scale(caveend, (window_width, window_height))
    stage = "blank"
    rects = []
    def __init__(self):
        Map.bg = self.colour
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map()
    
    def blits(self):
        win.blit(self.colour, (0, 0))
        
        if Map.facing == "up":
            win.blit(back, player)
        elif Map.facing == "right":
            win.blit(right, player)
        elif Map.facing == "left":
            win.blit(left, player)
        else:
            win.blit(front, player)


if __name__ == "__main__":

    video_path = "[video name].mp4"

    #use video capture feature
    cap = cv2.VideoCapture(video_path)

    #check if video capture is open
    #if not, send error message
    if not cap.isOpened():
        print("Error")

    while True:
        success, frame = cap.read()

        if not success:
            #another way?
            break

        cv2.imshow("Frame", frame)

        #delay in 1 millisecond
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
