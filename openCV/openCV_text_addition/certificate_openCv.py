import cv2
# Read the image from file
image = cv2.imread(r'mini projects\certificate_gen\certificate.jpg')
# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")
else:
    width = 600
    height = 400 
    image = cv2.resize(image, (width,height))

    name = "Your Name"
    name_loc_height=218
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

    text = cv2.putText(image,name,(name_loc_width,name_loc_height),font,font_scale,(0,0,255),thickness,cv2.LINE_AA)

    # Display the image in a window
    cv2.imshow('Image', image)
    # Wait for a key press and close the image window
    cv2.waitKey(0)
    cv2.destroyAllWindows()