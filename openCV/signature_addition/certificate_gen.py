import cv2
import numpy as np

# Paths to the certificate and signature images
certificate_path = '../Assets/Certificate.jpeg'
signature_path1 = '../Assets/img.png'
signature_path2 = '../Assets/img1.png'

# Read the base image
base_image = cv2.imread(certificate_path)
if base_image is None:
    print(f"Error: Unable to load image from path: {certificate_path}")
    exit()

# Read the first signature image
signature_image1 = cv2.imread(signature_path1, cv2.IMREAD_UNCHANGED)
if signature_image1 is None:
    print(f"Error: Unable to load image from path: {signature_path1}")
    exit()

# Read the second signature image
signature_image2 = cv2.imread(signature_path2, cv2.IMREAD_UNCHANGED)
if signature_image2 is None:
    print(f"Error: Unable to load image from path: {signature_path2}")
    exit()

# Function to add a signature to the base image
def add_signature(base_image, signature_image, x_offset, y_offset, scale_w, scale_h):
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
    signature_resized = cv2.resize(signature_resized, (int(w_base * scale_w), int(h_base * scale_h)))  # Adjust the resizing as needed

    # Separate the color and alpha channels from the signature image
    (b, g, r, a) = cv2.split(signature_resized)

    # Create a mask and inverse mask of the signature image
    mask = a
    inv_mask = cv2.bitwise_not(mask)

    # Get the region of interest (ROI) from the base image
    roi = base_image[y_offset:y_offset + signature_resized.shape[0], x_offset:x_offset + signature_resized.shape[1]]

    # Black-out the area of the signature in the ROI
    base_image_bg = cv2.bitwise_and(roi, roi, mask=inv_mask)

    # Take only the region of the signature from the signature image
    signature_fg = cv2.bitwise_and(signature_resized, signature_resized, mask=mask[:, :, np.newaxis])

    # Add the signature to the ROI and modify the base image
    dst = cv2.add(base_image_bg, signature_fg[:, :, :3])
    base_image[y_offset:y_offset + signature_resized.shape[0], x_offset:x_offset + signature_resized.shape[1]] = dst

    return base_image

# Add the first signature to the base image
base_image = add_signature(
    base_image=base_image,
    signature_image=signature_image1,
    x_offset=150,
    y_offset=602,
    scale_w=0.3,
    scale_h=0.1
)

# Calculate y_offset for the second signature
y_offset_second_signature = base_image.shape[0] - int(base_image.shape[0] * 0.1) - 210

# Add the second signature to the base image (example position: bottom left corner)
base_image = add_signature(
    base_image=base_image,
    signature_image=signature_image2,
    x_offset=720,
    y_offset=y_offset_second_signature,
    scale_w=0.3,
    scale_h=0.1
)

# Save or display the final image
""" cv2.imwrite('final_image_with_two_signatures.jpg', base_image)
cv2.imshow('Final Image with Two Signatures', base_image)
cv2.waitKey(0)
cv2.destroyAllWindows() """
