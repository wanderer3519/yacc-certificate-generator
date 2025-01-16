import cv2
import numpy as np

from openCV_text_addition.certificate_openCv import add_name
from signature_addition.certificate_gen import add_signature

# main template
image_path = '../Assets/Certificate.jpeg'
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


def main(image_path, is_sign_added, names , startX, startY, endX, endY):
    for name in names:
        if not is_sign_added:          
            # Call add_signature to add the first signature to the base image.
            base_image = add_signature(base_image = image_path, signature_image = signature_image1, x_offset = startX, y_offset = startY, scale_w = 0.3, scale_h = 0.1)

            # Call add_signature to add the second signature to the base image 
            base_image = add_signature(base_image = base_image, signature_image = signature_image2, x_offset = endX, y_offset = endY, scale_w = 0.3,scale_h = 0.1)

        add_name(image_path, name, startX, startY, endX, endY)
            

# Testing for signature addition 
if __name__ == '__main__':           
    main(image, False, ['Sri Krishna'], 150, 602, 720, 604)        




