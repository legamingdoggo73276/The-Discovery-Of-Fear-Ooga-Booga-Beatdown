#pip install opencv-python 
import cv2
import sys
import pygame

def play_video(video_path, screen=None):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error", video_path)
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    #If no screen provided, create one
    if screen is None:
        pygame.init()
        screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Video Player")
        cleanup = True
    else:
        cleanup = False  #Use existing game window

    clock = pygame.time.Clock()

    #loop through video frames until the end
    running = True
    while running:
        #ret returns true or false depending on whether the frame was read
        ret, frame = cap.read()
        if not ret:
            break

        #Before rotated video, don't need anymore
        #frame = cv2.rotate(frame, cv2.ROTATE_180)
        #Convert OpenCV BGR to pygame RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #Convert to Pygame surface
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))

        #Scale to match the screen size
        scaled_surface = pygame.transform.scale(frame_surface, screen.get_size())

        #Draw the scaled video frame
        screen.blit(scaled_surface, (0, 0))

        #Close window 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(fps * 4)

    cap.release()
    if cleanup:
        pygame.quit()


###code test
play_video("images/outro1.mp4") 