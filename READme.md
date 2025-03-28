# OCR with OpenCV & Tesseract

## 📌 Project Overview
This project demonstrates Optical Character Recognition (OCR) using OpenCV and Tesseract. It processes an image, extracts text, and saves the output to a file.

## 🛠️ Technologies Used
- **Python**
- **OpenCV** (for image processing)
- **Tesseract-OCR** (for text extraction)
- **Matplotlib** (for visualization)

## 🚀 How to Run the Project

1. **Install Dependencies:**
    ```bash
    pip install opencv-python pytesseract numpy matplotlib
2. **Run the OCR Script:**
    ```bash
    python ocr_extraction.py
3. **Extracted Text Output**
    The script extracts text from an image and saves it to extracted_text.txt.

## Sample output
### Extracted text from an example image:
PHONE VALIDATOR FREE RESULTS

FAKE NUMBER FOUND!

Number has too many digits. 447512977697 cannot be successfully called or texted.

## 📂 Project Structure
📂 OCR-Project
 ├── sample_text.jpg         # Input image
 ├── ocr_extraction.py       # OCR script
 ├── extracted_text.txt      # Output text file
 ├── README.md               # Project documentation

## next steps
improve OCR accuracy with better image preprocessing.

Implement OCR for multiple images in a folder.

Extend project to extract text from PDFs.