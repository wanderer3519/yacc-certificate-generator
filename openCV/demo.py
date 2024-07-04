import cv2
#from PIL import Image, ImageDraw, ImageFont


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
  
image_path=r"D:\COLLEGE\B.Tech 5th SEM\yacc_project\certificate_generator\certificate_gen2.jpg"
# load the image
image = cv2.imread(image_path)
clone = image.copy()
cv2.namedWindow("image")
# setting the mouse callback function
names=['AA_BB_CC_DD_EE1', 'AA_BB_CC_DD_EE2', 'AA_BB_CC_DD_EE3', 'AA_BB_CC_DD_EE4', 'AA_BB_CC_DD_EE5']
  
while True:
    cv2.imshow("image", image)
    cv2.setMouseCallback("image", shape_selection)
    # display the image and wait for a keypress
    key = cv2.waitKey(1) & 0xFF
  
    # if the 'c' key is pressed
    if key == ord("c"):
        # font 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        
        # org 
        org = point[0] 
        
        # fontScale 
        fontScale = 1
        
        # Blue color in BGR 
        color = (255, 0, 0) 
        
        # Line thickness of 2 px 
        thickness = 2
        
        # Using cv2.putText() method 
        image = cv2.putText(image, 'OpenCV', org, font,  
                        fontScale, color, thickness, cv2.LINE_AA) 
        cv2.imshow("Text entered", image)
        cv2.waitKey(0)
            
        # close all open windows
        cv2.destroyAllWindows()
        image=clone.copy()
        continue
