import cv2

# Read the color image
color_img = cv2.imread('color_image.jpg')

# Extract the pixel values in red, green, and blue dimensions
red_values = color_img[:,:,2]
green_values = color_img[:,:,1]
blue_values = color_img[:,:,0]

# Display the pixel values for the first pixel
print(f"Red: {red_values[0,0]}, Green: {green_values[0,0]}, Blue: {blue_values[0,0]}")
