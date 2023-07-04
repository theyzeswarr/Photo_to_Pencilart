import cv2

# Load the image
image = cv2.imread("profile.png")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted_image = cv2.bitwise_not(gray_image)

# Apply Gaussian blur to the inverted image
blurred_image = cv2.GaussianBlur(inverted_image, (111, 111), 0)

# Blend the grayscale image with the blurred image using the "color dodge" blending mode
blended_image = cv2.divide(gray_image, 255 - blurred_image, scale=256.0)

# Save the pencil drawing image
cv2.imwrite("pencil_drawing.jpg", blended_image)

# Display the pencil drawing image
cv2.imshow("Pencil Drawing", blended_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
