from PIL import Image
import pytesseract

def textConverter(image):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image = Image.open(image)
    text = pytesseract.image_to_string(image, lang = 'eng')
    return text
