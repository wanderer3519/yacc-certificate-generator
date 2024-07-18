from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
# Read the image from file
image = cv2.imread(r"C:\Users\Hp\OneDrive\Desktop\OpenCV\mini projects\certificate_gen\certificate.jpg")
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

def create_text_image(text, font_path, font_size, image_size, text_color ,cv2_image):
    
    cv2_image_rgb = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)

    # Convert the image to a PIL Image
    image = Image.fromarray(cv2_image_rgb)
    draw = ImageDraw.Draw(image)
    
    # Load a font
    font = ImageFont.truetype(font_path, font_size)
    
    # Calculate the size of the text
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # Calculate the position to center the text
    position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)
    
    # Draw the text on the image
    draw.text(position, text, font=font, fill=text_color)
    # # Calculate text size and position
    # text_size = draw.textsize(text, font=font)
    # text_x = (image_size[0] - text_size[0]) // 2
    # text_y = (image_size[1] - text_size[1]) // 2
    
    # # Draw the text on the image
    # draw.text((text_x, text_y), text, font=font, fill=text_color)
    
    return image

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

                font_path =   'C:\Users\Hp\OneDrive\Desktop\OpenCV\mini projects\certificate_gen\Oswald-VariableFont_wght.ttf'  # Update with the path to your font file
                image_size = (width,height)
                font_size = 24
                
                output = create_text_image(name, font_path, font_size, image_size, (255,0,0) ,clone2)
                # # Get the text size
                # (text_width, text_height), baseline = cv2.getTextSize(name, font, font_scale, thickness)

                # # Add the baseline to the height to get the total height
                # total_height = text_height + baseline

                # print(f"Text width: {text_width}")
                # print(f"Text height: {total_height}")

                # name_loc_width = width//2 - (text_width//2)

                #text = cv2.putText(clone2,name,(name_loc_width,name_loc_height),font,font_scale,(0,0,255),thickness,cv2.LINE_AA)


                # # Display the image in a window
                # cv2.imshow('Image', clone2)
                output.show()

                # Wait for a key press and close the image window
                cv2.waitKey(0)
                cv2.destroyAllWindows()