# import cv2
# import numpy as np

# from openCV_text_addition.certificate_openCv import add_name
# from signature_addition.certificate_gen import add_signature

# # main template
# """ image_path = '../Assets/Certificate.jpeg'
# signature_path1 = '../Assets/img.png'
# signature_path2 = '../Assets/img1.png'

# image = cv2.imread('../Assets/Certificate.jpeg')
# if image is None:
#     print(f"Error: Unable to load image from given path: {image_path}")
#     exit()

# # Read the first signature image using path
# signature_image1 = cv2.imread(signature_path1, cv2.IMREAD_UNCHANGED)

# if signature_image1 is None:
#     print(f"Error: Unable to load image from given path: {signature_path1}")
#     exit()

# # Read the second signature image using path
# signature_image2 = cv2.imread(signature_path2, cv2.IMREAD_UNCHANGED)
# if signature_image2 is None:
#     print(f"Error: Unable to load image from given path: {signature_path2}")
#     exit()
#  """

# # start = (startx, starty)
# # end = (endx, endy)
# # signs = (signature_image1, signature_image)

# def main(image_path, is_sign_added, names, start, end, signs = ()):
#     if signs:
#         signature_image1 = signs[0] 
#         signature_image2 = signs[1]
#     else:
#         print("No proper images. Couldn't be loaded")
#         exit()

#     startX = start[0]
#     startY = start[1]

#     endX = end[0]
#     endY = end[1]

#     for name in names:
#         if not is_sign_added:          
#             # Call add_signature to add the first signature to the base image.
#             base_image = add_signature(base_image = image_path, signature_image = signature_image1, x_offset = startX, y_offset = startY, scale_w = 0.3, scale_h = 0.1)

#             # Call add_signature to add the second signature to the base image 
#             base_image = add_signature(base_image = base_image, signature_image = signature_image2, x_offset = endX, y_offset = endY, scale_w = 0.3,scale_h = 0.1)

#         add_name(image_path, name, startX, startY, endX, endY)
            

# # Testing for signature addition 
# # if __name__ == '__main__':           
# #     main(image, False, ['Sri Krishna'], 150, 602, 720, 604)        


import cv2
import numpy as np

from openCV_text_addition.certificate_openCv import add_name
from signature_addition.certificate_gen import add_signature

def main(image_path, is_sign_added, names, start, end, signs=()):
    # Load the base image
    base_image = cv2.imread(image_path)
    if base_image is None:
        print(f"Error: Unable to load image from given path: {image_path}")
        return None

    if signs:
        signature_image1 = signs[0]
        signature_image2 = signs[1]
    else:
        print("No proper signature images provided. Exiting.")
        return None

    # Extract start and end coordinates
    startX, startY = start
    endX, endY = end

    # Process each name
    for name in names:
        # Add signatures if the flag is set
        if is_sign_added:
            base_image = add_signature(
                base_image=base_image,
                signature_image=signature_image1,
                x_offset=startX,
                y_offset=startY,
                scale_w=0.3,
                scale_h=0.1
            )
            base_image = add_signature(
                base_image=base_image,
                signature_image=signature_image2,
                x_offset=endX,
                y_offset=endY,
                scale_w=0.3,
                scale_h=0.1
            )

        # Add the name to the image
        base_image = add_name(
            base_image=base_image,
            name=name,
            startX=startX,
            startY=startY,
            endX=endX,
            endY=endY
        )

    # Return the modified image
    return base_image

