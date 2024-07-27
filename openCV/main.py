
from openCV_text_addition.certificate_openCv import add_name
import cv2
import numpy as np
from signature_addition.certificate_gen import add_signature

# main template
image = cv2.imread(r'mini projects\certificate_gen\certificate.jpg')

def main(is_sign_added, is_watermark_added, names , startX, startY, endX, endY):

    for name in names:
        if not is_sign_added:   # startX and startY: x_offset, y_offset of first signature image. endX, endY: x_offset and y_offset of second image.
            certificate_path = '../Assets/certificate.jpeg'
            signature_path1 = '../Assets/img.png'
            signature_path2 = '../Assets/img1.png'
            
            # Read the base image using path
            base_image = cv2.imread(certificate_path)
            if base_image is None:
                print(f"Error: Unable to load image from given path: {certificate_path}")
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
                
            # Call add_signature to add the first signature to the base image.
            base_image = add_signature(base_image = base_image, signature_image = signature_image1, x_offset = startX, y_offset = startY, scale_w = 0.3, scale_h = 0.1)

            # Call add_signature to add the second signature to the base image 
            base_image = add_signature(base_image = base_image, signature_image = signature_image2, x_offset = endX, y_offset = endY, scale_w = 0.3,scale_h = 0.1)

            # Save or display the final image
            cv2.imwrite('final_image_with_two_signatures.jpg', base_image)
            cv2.imshow('Final Image with Two Signatures', base_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            # do sth

        if not is_watermark_added:
            pass
            #do sth
    
        else:
            add_name(image,name,startX,startY,endX,endY)
            
# Testing for signature addition            
main(0, 1, [], 150, 602, 720, 604)

            
        




