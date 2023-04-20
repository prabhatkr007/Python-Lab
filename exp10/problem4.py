import cv2

# Read the gray image
gray_img = cv2.imread('gray_image.jpg', cv2.IMREAD_GRAYSCALE)

# Define the threshold value
threshold_value = 127

# Convert the gray image to binary image using thresholding
ret, binary_img = cv2.threshold(gray_img, threshold_value, 255, cv2.THRESH_BINARY)

# Write both images
cv2.imwrite('gray_image.jpg', gray_img)
cv2.imwrite('binary_image.jpg', binary_img)
