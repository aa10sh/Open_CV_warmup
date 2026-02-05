import cv2

camera=cv2.VideoCapture(0)
print("here we record videos")
frame_width  = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Learning: camera frames have their own size.
# If sizes don’t match → video file becomes corrupted / blank.

save_it = input("Do you want to save this video? Type 'yes' or 'no': ")


if save_it =="yes":
   file_type = input("Enter codec type (MJPG / MP4V / XVID): ")
   codec=cv2.VideoWriter_fourcc(*file_type)
   file_name=input("Enter saving file name(e.g. xyz.avi): ")
   recorder=cv2.VideoWriter(file_name, codec, 30,(frame_width, frame_height))
else:
   recorder=None

print("You can press 'q' to turn off the camera.")
   
while True:
 ret, frames= camera.read()

 if ret is None:
    print(" Unable to start camera.")
    break
 
 cv2.imshow("Live screen",frames)

 if save_it == 'yes':
    recorder.write(frames)

 if cv2.waitKey(1) & 0xFF == ord('q'):
    break

camera.release()
if recorder is not None:
   recorder.release()

cv2.destroyAllWindows()

   





