from openCV_text_addition.certificate_openCv import add_name
import cv2
import numpy as np
from signature_addition.certificate_gen import add_signature

# main template
image_path = r'../Assets/Certificate.jpeg'
signature_path1 = '../Assets/img.png'
signature_path2 = '../Assets/img1.png'

image = cv2.imread('../Assets/Certificate.jpeg')
if image is None:
    print(f"Error: Unable to load image from given path: {image_path}")
    exit()

# Read the first signature image using path
signature_image1 = cv2.imread(signature_path1, cv2.IMREAD_UNCHANGED)

if signature_image1 is None:
    print(f"Error: Unable to load image from given path: {signature_path1}")
    exit()

# Read the second signature image using path
signature_image2 = cv2.imread(signature_path2, cv2.IMREAD_UNCHANGED)
if signature_image2 is None:
    print(f"Error: Unable to load image from given path: {signature_path2}")
    exit()


def main(is_sign_added, is_watermark_added, names , startX, startY, endX, endY):

    for name in names:
        if not is_sign_added:          
                
            # Call add_signature to add the first signature to the base image.
            base_image = add_signature(base_image = image, signature_image = signature_image1, x_offset = startX, y_offset = startY, scale_w = 0.3, scale_h = 0.1)

            # Call add_signature to add the second signature to the base image 
            base_image = add_signature(base_image = base_image, signature_image = signature_image2, x_offset = endX, y_offset = endY, scale_w = 0.3,scale_h = 0.1)
    
        elif not is_watermark_added:
            pass
            #do sth
    
        else:
            add_name(image, name, startX, startY, endX, endY)
            
            

# Testing for signature addition 
if __name__ == '__main__':           
    main(True, True, ['121'], 150, 602, 720, 604)

""" 
    cv2.imwrite('final_image_with_two_signatures.jpg', base_image)
    cv2.imshow('Final Image with Two Signatures', base_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
"""

cv2.imshow('Test', image)
cv2.waitKey(6000) # time in ms
# exit()
# cv2.destroyAllWindows()
        




