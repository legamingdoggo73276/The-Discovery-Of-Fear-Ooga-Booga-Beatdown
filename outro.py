#pip install opencv-python 

import cv2

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
