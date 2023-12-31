# PHOTOBOOTH
import cv2
import os
import numpy as np

print("\u2764\ufe0f")
# Path to the folder containing the images
folder_path = os.path.join('CaptureImages')

# List all image files in the folder
img_file = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

# Create a new blank image to hold the 4 images.
result = None

# Iterate over the first 4 image files
for i in range(4):
    image = cv2.imread(os.path.join(folder_path, img_file[i]))

    # ImageProcessing Process.
    if i == 0:
        'Image Processing'

    elif i == 1:
        'Image Processing'

    elif i == 2:
        'Image Processing'

    elif i == 3:
        'Image Processing'

    image = cv2.resize(image, (340, 280))
    # Add a inner border around the image
    image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=('color code'))
    # Add the image to the result image
    if result is None:
        result = image
    else:
        result = cv2.hconcat([result, image])
# Add outer borders between the images
result = cv2.copyMakeBorder(result, 40, 40, 70, 40, cv2.BORDER_CONSTANT, value=('color code'))
# save the frame to an image file in the CaptureImages folder
cv2.imwrite('CaptureImages/namePhotoBooth.jpg', result)

# Show the result image
cv2.imshow('PhotoBooth', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
