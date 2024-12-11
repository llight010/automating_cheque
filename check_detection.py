import cv2

# Function to detect and isolate checks from an image
def detect_checks(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert to grayscale and apply edge detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    
    # Find contours (likely corresponding to checks)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    checks = []  # Store the full checks
    
    for contour in contours:
        # Approximate the contour to a polygon (filtering for rectangular contours)
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        
        # Check if it's a rectangle (likely a check)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            
            # Filter out small contours based on area
            if w > 100 and h > 100:  # Adjust the thresholds as per your check size
                check_image = image[y:y + h, x:x + w]
                checks.append((check_image, x, y))  # Save the cropped check image along with its position
    
    # Save the full check images and remove small or unwanted checks
    for i, (check_image, x, y) in enumerate(checks):
        check_image_path = f"{image_path.split('.')[0]}_check_{x}_{y}.png"
        
        # Save only the full checks
        cv2.imwrite(check_image_path, check_image)
    
    # If no checks found, print a message
    if len(checks) == 0:
        print(f"No checks detected for {image_path}")
    else:
        print(f"Checks detected and saved for {image_path}")

# Example usage
detect_checks("path_to_your_image.png")  # Replace with your actual image path
