import cv2

img_path=input(str("Enter image path wants to read: "))
image=cv2.imread(img_path)

if image is not None:
   cv2.imshow(img_path, image)
   print("Image showing...")
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   print("image closed")
else:
    print("Error: image didn't loaded")  


if image is not None:
    output_image=input(str("Enter name of output image you wants to save(add .png at end): "))
    cv2.imwrite(output_image, image)
    print(f"image saved successfully as {output_image}")
else:
    print("Error: Image can't save")    

move=input(str("do you want to convert it into grayscale..?\n Yes/No : "))   

if move=="Yes":
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Image successfuly converted to Grayscale!!")
    print("Gray scale image showing..")
    cv2.imshow(img_path, gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("grayscale image closed.")
    if gray is not None:
        gray_output_image=input(str("Enter name of grayscale output image(add .png): "))
        cv2.imwrite(gray_output_image, gray)
        print(f"grayscale image saved successfully as {gray_output_image}")
else:
    print("Okay, as you wish.")



  