import cv2
import numpy as np

# Read the certificate and logo images
certificate = cv2.imread('/home/anusha/Downloads/certificate.jpeg')
logo = cv2.imread('/home/anusha/Downloads/o.png', cv2.IMREAD_UNCHANGED)

# Get the color of the top rightmost pixel of the logo
top_right_pixel = logo[0, -1]
top_right_pixel_hsv = cv2.cvtColor(np.uint8([[top_right_pixel]]), cv2.COLOR_BGR2HSV)[0][0]

# Define a range for the background color based on the top rightmost pixel
h_range = 10
s_range = 50
v_range = 50

lower_bound = np.array([max(0, top_right_pixel_hsv[0] - h_range), max(0, top_right_pixel_hsv[1] - s_range), max(0, top_right_pixel_hsv[2] - v_range)])
upper_bound = np.array([min(180, top_right_pixel_hsv[0] + h_range), min(255, top_right_pixel_hsv[1] + s_range), min(255, top_right_pixel_hsv[2] + v_range)])

# Create the mask for the background
hsv_logo = cv2.cvtColor(logo, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_logo, lower_bound, upper_bound)
mask_inv = cv2.bitwise_not(mask)

# Extract the foreground using the inverse mask
original_logo_fg = cv2.bitwise_and(logo[:, :, :3], logo[:, :, :3], mask=mask_inv)
original_alpha_channel = mask_inv

# Function to handle mouse events
def select_position(event, x, y, flags, param):
    global x_offset, y_offset, dragging, resizing, logo_fg, alpha_channel
    if event == cv2.EVENT_LBUTTONDOWN:
        if x in range(x_offset + logo_fg.shape[1] - 10, x_offset + logo_fg.shape[1]) and y in range(y_offset + logo_fg.shape[0] - 10, y_offset + logo_fg.shape[0]):
            resizing = True
        else:
            x_offset, y_offset = x, y
            dragging = True
    elif event == cv2.EVENT_MOUSEMOVE and dragging:
        x_offset, y_offset = x, y
    elif event == cv2.EVENT_MOUSEMOVE and resizing:
        new_width = x - x_offset
        new_height = y - y_offset
        if new_width > 10 and new_height > 10:
            # Resize the logo foreground and alpha channel
            logo_fg = cv2.resize(original_logo_fg, (new_width, new_height), interpolation=cv2.INTER_AREA)
            alpha_channel = cv2.resize(original_alpha_channel, (new_width, new_height), interpolation=cv2.INTER_AREA)
    elif event == cv2.EVENT_LBUTTONUP:
        dragging = False
        resizing = False

# Initialize variables
x_offset, y_offset = 0, 0
dragging = False
resizing = False
logo_fg = original_logo_fg.copy()
alpha_channel = original_alpha_channel.copy()

# Create a window and set mouse callback
cv2.namedWindow('Select Position')
cv2.setMouseCallback('Select Position', select_position)

# Display the certificate image and wait for the user to select a position
while True:
    temp_img = certificate.copy()
    
    # Ensure the logo fits within the certificate boundaries
    y1, y2 = max(0, y_offset), min(certificate.shape[0], y_offset + logo_fg.shape[0])
    x1, x2 = max(0, x_offset), min(certificate.shape[1], x_offset + logo_fg.shape[1])

    # Create temporary image with the same size as the logo
    temp_logo_fg = np.zeros((y2 - y1, x2 - x1, 3), dtype=np.uint8)
    temp_alpha_channel = np.zeros((y2 - y1, x2 - x1), dtype=np.uint8)

    # Resize the logo_fg and alpha_channel to fit temp arrays if needed
    resized_logo_fg = cv2.resize(logo_fg, (temp_logo_fg.shape[1], temp_logo_fg.shape[0]), interpolation=cv2.INTER_AREA)
    resized_alpha_channel = cv2.resize(alpha_channel, (temp_alpha_channel.shape[1], temp_alpha_channel.shape[0]), interpolation=cv2.INTER_AREA)
    
    # Place the resized logo and alpha channel in the temporary arrays
    temp_logo_fg[:resized_logo_fg.shape[0], :resized_logo_fg.shape[1]] = resized_logo_fg
    temp_alpha_channel[:resized_alpha_channel.shape[0], :resized_alpha_channel.shape[1]] = resized_alpha_channel

    # Create mask and inverse mask
    mask = temp_alpha_channel / 255.0
    mask_inv = 1.0 - mask

    # Apply the logo on the temporary image using mask
    for c in range(3):
        temp_img[y1:y2, x1:x2, c] = (
            temp_logo_fg[:, :, c] * mask +
            temp_img[y1:y2, x1:x2, c] * mask_inv
        )

    cv2.rectangle(temp_img, (x1, y1), (x2, y2), (0, 255, 0), 1)
    cv2.rectangle(temp_img, (x2 - 10, y2 - 10), (x2, y2), (0, 0, 255), -1)  # Resize handle

    cv2.imshow('Select Position', temp_img)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press 'ESC' to exit
        break

cv2.destroyAllWindows()

# Save the final image
if x_offset > 0 and y_offset > 0:
    # Ensure dimensions are correct before applying
    y1, y2 = max(0, y_offset), min(certificate.shape[0], y_offset + logo_fg.shape[0])
    x1, x2 = max(0, x_offset), min(certificate.shape[1], x_offset + logo_fg.shape[1])

    # Apply the logo on the certificate
    for c in range(3):
        certificate[y1:y2, x1:x2, c] = (
            logo_fg[:, :, c] * (alpha_channel / 255.0) +
            certificate[y1:y2, x1:x2, c] * (1 - alpha_channel / 255.0)
        )

    cv2.imwrite('certificate_with_logo.jpg', certificate)
    cv2.imshow('Certificate with Logo', certificate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No position selected.")
