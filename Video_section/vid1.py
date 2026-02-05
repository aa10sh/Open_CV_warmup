import cv2
cap=cv2.VideoCapture(0)

while True:
    ret, frame =cap.read() 
    # ret   → bool
    #  frame → MatLike (numpy image)
    
    if not ret:
        print("Video can't be start..")
        break

    cv2.imshow("Webcam Screen", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

cap.release()
cv2.destroyAllWindows()     