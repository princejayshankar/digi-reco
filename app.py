from flask import Flask, render_template, request
from PIL import Image
import pytesseract

app = Flask(__name__)

# Function to perform OCR on the image and extract digits
def extract_digits_from_image(image):
    # Perform OCR using pytesseract
    extracted_text = pytesseract.image_to_string(image, config='--psm 6')
    
    # Extract digits from the extracted text
    digits = [int(char) for char in extracted_text if char.isdigit()]
    return digits

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        image = Image.open(file)
        extracted_digits = extract_digits_from_image(image)
        return render_template('result.html', digits=extracted_digits)

if __name__ == '__main__':
    app.run(debug=True)

