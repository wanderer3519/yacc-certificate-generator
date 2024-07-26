# from signature_addition import ...
from openCV_text_addition.certificate_openCv import add_name

# main template
import cv2
image = cv2.imread(r'mini projects\certificate_gen\certificate.jpg')

def main(is_sign_added, is_watermark_added, names , startX, startY, endX, endY):

    for name in names:
        if not is_sign_added:
            pass
            # do sth

        if not is_watermark_added:
            pass
            #do sth
    
        else:
            add_name(image,name,startX,startY,endX,endY)

            
        




