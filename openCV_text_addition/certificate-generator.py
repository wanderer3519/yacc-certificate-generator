
import cv2
# Read the image from file
image = cv2.imread("certificate.jpeg")
width = 600
height = 400 
image = cv2.resize(image, (width,height))
clone1=image.copy()
# Check if the image was loaded successfully
namelst=["Yourname","asdfg",'dvbdfgh']


point = []
crop = False
  
def shape_selection(event, x, y, flags, param):
   # grab references to the global variables
   global point, crop
   
   # Record the starting(x, y) coordinates when the left mouse button was clicked
   if event == cv2.EVENT_LBUTTONDOWN:
      point = [(x, y)]
   
   # check to see if the left mouse button was released
   elif event == cv2.EVENT_LBUTTONUP:
      # record the ending (x, y) coordinates 
      point.append((x, y))

     # d1 = ImageDraw.Draw(image)
     # d1.text(point[0], "Sample text", fill =(255, 0, 0),font=myFont)
      # draw a rectangle
      cv2.rectangle(image, point[0], point[1], (0, 255, 0), 2)
     #   image.show()

if image is None:
    print("Error: Could not load image.")
else:
    while True:
        
        cv2.imshow("image", image)
        cv2.setMouseCallback("image", shape_selection)
        key = cv2.waitKey(1) & 0xFF
        #  if the 'c' key is pressed
        if key == ord("c"):

            for name in namelst:
                clone2=clone1.copy()
                name_loc_height=point[0][0]
                print(name_loc_height)
                font_scale = 1
                thickness = 1

                font = cv2.FONT_HERSHEY_COMPLEX_SMALL

                # Get the text size
                (text_width, text_height), baseline = cv2.getTextSize(name, font, font_scale, thickness)

                # Add the baseline to the height to get the total height
                total_height = text_height + baseline

                print(f"Text width: {text_width}")
                print(f"Text height: {total_height}")

                name_loc_width = width//2 - (text_width//2)

                text = cv2.putText(clone2,name,(name_loc_width,name_loc_height),font,font_scale,(0,0,255),thickness,cv2.LINE_AA)

                # Display the image in a window
                cv2.imshow('Image', clone2)
                # Wait for a key press and close the image window
                cv2.waitKey(0)
                cv2.destroyAllWindows()