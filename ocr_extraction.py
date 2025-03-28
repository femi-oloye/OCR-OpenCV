import cv2
import pytesseract
import matplotlib.pyplot as plt

# Load the image
image_path = "ocr-img.png"
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to preprocess for OCR
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the processed image
plt.figure(figsize=(10, 5))
plt.imshow(thresh, cmap='gray')
plt.title("Preprocessed Image for OCR")
plt.axis("off")
plt.show()

# Configure Tesseract (optional, depending on system)
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"  # Adjust if needed

# Perform OCR
extracted_text = pytesseract.image_to_string(thresh)

# Print extracted text
print("\nExtracted Text:\n")
print(extracted_text)

# Save extracted text to a file
output_file = "extracted_text.txt"
with open(output_file, "w") as file:
    file.write(extracted_text)

print(f"\nExtracted text saved to {output_file}")
