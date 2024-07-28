import cv2

def add_name(image,name,startX,startY,endX,endY):
    name_loc_height=startY
    font_scale = 1
    thickness = 1

    font = cv2.FONT_HERSHEY_COMPLEX_SMALL

    # Get the text size
    (text_width, text_height), baseline = cv2.getTextSize(name, font, font_scale, thickness)

    # Add the baseline to the height to get the total height
    total_height = text_height + baseline

    # print(f"Text width: {text_width}")
    # print(f"Text height: {total_height}")

    name_loc_width = (startX + endX)//2 - (text_width//2)

    text = cv2.putText(image,name,(name_loc_width,name_loc_height),font,font_scale,(0,0,255),thickness,cv2.LINE_AA)

