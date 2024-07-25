import cv2
import numpy as np

# Load the certificate image
certificate = cv2.imread('/home/anusha/Downloads/certificate.jpeg')

# Read the watermark text from a file
with open('/home/anusha/Downloads/watermark.txt', 'r') as file:
    watermark_text = file.read().strip()

# Define the font
font = cv2.FONT_HERSHEY_SIMPLEX

# Get the dimensions of the certificate image
(h, w) = certificate.shape[:2]

# Initial size and position for the watermark
font_scale = 4
font_thickness = 2
(text_w, text_h), _ = cv2.getTextSize(watermark_text, font, font_scale, font_thickness)
x = (w - text_w) // 2
y = (h - text_h) // 2

# Variables to store the position and scaling state
position = (x, y)
dragging = False
resizing = False
initial_y = 0

# Function to handle mouse events
def update_watermark(event, x, y, flags, param):
    global position, dragging, resizing, initial_y, font_scale, text_w, text_h

    if event == cv2.EVENT_LBUTTONDOWN:
        if x in range(position[0] + text_w - 10, position[0] + text_w) and y in range(position[1] + text_h - 10, position[1] + text_h):
            resizing = True
            initial_y = y
        else:
            position = (x, y)
            dragging = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if dragging:
            position = (x, y)
        elif resizing:
            dy = y - initial_y
            font_scale = max(1, font_scale + dy * 0.01)
            initial_y = y
            text_w, text_h = cv2.getTextSize(watermark_text, font, font_scale, font_thickness)[0]
    elif event == cv2.EVENT_LBUTTONUP:
        dragging = False
        resizing = False

# Create a window and set a mouse callback
cv2.namedWindow('Watermarked Certificate')
cv2.setMouseCallback('Watermarked Certificate', update_watermark)

while True:
    # Create a transparent overlay
    overlay = certificate.copy()
    
    # Add the watermark text to the overlay at the updated position and size
    text_size, _ = cv2.getTextSize(watermark_text, font, font_scale, font_thickness)
    text_w, text_h = text_size
    cv2.putText(overlay, watermark_text, (position[0], position[1] + text_h), font, font_scale, (255, 0, 0), font_thickness, cv2.LINE_AA)
    
    # Blend the overlay with the certificate image
    alpha = 0.2  # Transparency factor
    watermarked_certificate = cv2.addWeighted(overlay, alpha, certificate, 1 - alpha, 0)
    
    # Display the watermark area and resize handle
    cv2.rectangle(watermarked_certificate, (position[0], position[1]), (position[0] + text_w, position[1] + text_h), (0, 255, 0), 1)
    cv2.rectangle(watermarked_certificate, (position[0] + text_w - 10, position[1] + text_h - 10), (position[0] + text_w, position[1] + text_h), (0, 0, 255), -1)  # Resize handle
    
    # Display the watermarked certificate
    cv2.imshow('Watermarked Certificate', watermarked_certificate)
    
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press 'ESC' to exit
        break

# Save the final watermarked certificate
cv2.imwrite('watermarked_certificate.jpg', watermarked_certificate)
cv2.destroyAllWindows()

