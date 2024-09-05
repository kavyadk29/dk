import cv2
import numpy as np

# Create a blank image with a white background
width, height = 500, 500
logo = np.ones((height, width, 3), dtype="uint8") * 255

# Define font properties
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 5
thickness = 10

# Add the letter 'D' to the image
text_D = "D"
color_D = (0, 0, 255)  # Red color in BGR format
text_size_D = cv2.getTextSize(text_D, font, font_scale, thickness)[0]
text_x_D = width // 4 - text_size_D[0] // 2
text_y_D = height // 2 + text_size_D[1] // 2
cv2.putText(logo, text_D, (text_x_D, text_y_D), font, font_scale, color_D, thickness)

# Add the letter 'K' to the image
text_K = "K"
color_K = (0, 0, 255)  # Red color in BGR format
text_size_K = cv2.getTextSize(text_K, font, font_scale, thickness)[0]
text_x_K = 3 * width // 4 - text_size_K[0] // 2
text_y_K = height // 2 + text_size_K[1] // 2
cv2.putText(logo, text_K, (text_x_K, text_y_K), font, font_scale, color_K, thickness)

# Draw a connecting arc between 'D' and 'K' for design purposes
center_coordinates = (width // 2, height // 2)
axesLength = (180, 180)
angle = 0
startAngle = 0
endAngle = 180
color_arc = (0, 255, 0)  # Green color in BGR format
thickness_arc = 10
cv2.ellipse(logo, center_coordinates, axesLength, angle, startAngle, endAngle, color_arc, thickness_arc)

# Draw a circle around the 'DK' combination
circle_center = (width // 2, height // 2)
circle_radius = 200
circle_color = (255, 0, 0)  # Blue color in BGR format
circle_thickness = 10
cv2.circle(logo, circle_center, circle_radius, circle_color, circle_thickness)

# Add a smaller inner circle for emphasis
inner_circle_radius = 50
inner_circle_color = (0, 255, 255)  # Yellow color in BGR format
cv2.circle(logo, circle_center, inner_circle_radius, inner_circle_color, -1)  # Filled circle

# Show the logo
cv2.imshow("DK Logo", logo)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the logo as an image file
cv2.imwrite("dk_logo.png", logo)
