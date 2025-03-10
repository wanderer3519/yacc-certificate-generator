import cv2
import numpy as np

# Read the base image and the signature image
base_image = cv2.imread('certificate.jpeg')
signature_image = cv2.imread('img.png', cv2.IMREAD_UNCHANGED)

# Check if the signature image has an alpha channel
if signature_image.shape[2] == 4:
    # Signature image has an alpha channel
    signature_resized = signature_image
else:
    # Signature image does not have an alpha channel
    b_channel, g_channel, r_channel = cv2.split(signature_image)
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255  # Create a dummy alpha channel
    signature_resized = cv2.merge([b_channel, g_channel, r_channel, alpha_channel])

# Get dimensions of the base image
(h_base, w_base) = base_image.shape[:2]

# Resize the signature image if needed
signature_resized = cv2.resize(signature_resized, (int(w_base * 0.3), int(h_base * 0.1)))  # Adjust the resizing as needed

# Separate the color and alpha channels from the signature image
(b, g, r, a) = cv2.split(signature_resized)

# Create a mask and inverse mask of the signature image
mask = a
inv_mask = cv2.bitwise_not(mask)

# Determine the position where the signature will be placed
y_offset = h_base - signature_resized.shape[0] - 190  # 10 pixels from the bottom
x_offset = w_base - signature_resized.shape[1] - 170  # 10 pixels from the right

# Get the region of interest (ROI) from the base image
roi = base_image[y_offset:y_offset + signature_resized.shape[0], x_offset:x_offset + signature_resized.shape[1]]

# Black-out the area of the signature in the ROI
base_image_bg = cv2.bitwise_and(roi, roi, mask=inv_mask)

# Take only the region of the signature from the signature image
signature_fg = cv2.bitwise_and(signature_resized, signature_resized, mask=mask[:, :, np.newaxis])

# Add the signature to the ROI and modify the base image
dst = cv2.add(base_image_bg, signature_fg[:, :, :3])
base_image[y_offset:y_offset + signature_resized.shape[0], x_offset:x_offset + signature_resized.shape[1]] = dst

# Save or display the final image
cv2.imwrite('final_image.jpg', base_image)
cv2.imshow('Final Image', base_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#LD_PRELOAD=/lib/x86_64-linux-gnu/libpthread.so.0 python3 your_script.py