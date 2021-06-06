# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 09:17:19 2021

@author: yashesh
"""
from PIL import Image
from pytesseract import pytesseract

# Defining paths to tesseract.exe
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# and the image we would be using
image_path = r"ocrimg4.jpg"

# Opening the image & storing it in an image object
img = Image.open(image_path)

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)
print(text[:-1])

"""

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open('textimage.png')))

# List of available languages
print(pytesseract.get_languages(config=''))

# French text image to string
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

# In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# NOTE: In this case you should provide tesseract supported images or tesseract will return error
print(pytesseract.image_to_string('textimage.png'))

# Batch processing with a single file containing the list of multiple image file paths
print(pytesseract.image_to_string('images.txt'))

# Timeout/terminate the tesseract job after a period of time
try:
    print(pytesseract.image_to_string('textimage.jpg', timeout=2)) # Timeout after 2 seconds
    print(pytesseract.image_to_string('textimage.jpg', timeout=0.5)) # Timeout after half a second
except RuntimeError as timeout_error:
    # Tesseract processing is terminated
    pass

# Get bounding box estimates
print(pytesseract.image_to_boxes(Image.open('textimage.png')))

# Get verbose data including boxes, confidences, line and page numbers
print(pytesseract.image_to_data(Image.open('textimage.png')))

# Get information about orientation and script detection
print(pytesseract.image_to_osd(Image.open('textimage.png')))

# Get a searchable PDF
pdf = pytesseract.image_to_pdf_or_hocr('textimage.png', extension='pdf')
with open('textimage.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default

# Get HOCR output
hocr = pytesseract.image_to_pdf_or_hocr('textimage.png', extension='hocr')

# Get ALTO XML output
xml = pytesseract.image_to_alto_xml('textimage.png')"""