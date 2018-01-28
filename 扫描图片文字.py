# USAGE
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
# Include the above line, if you don't have tesseract executable in your PATH
# Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

# print(pytesseract.image_to_string(Image.open('a.png')))
# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))
# Add the following config, if you have tessdata error like: “Error opening data file…”

tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# It's important to add double quotes around the dir path.

print(pytesseract.image_to_string(Image.open('a.png'), lang='chi_sim', config=tessdata_dir_config))
