from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

# If you're on Windows, you may need to tell Python where Tesseract is installed:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load an image (e.g., scanned ID or document photo)
img = Image.open("data/real/sample.jpg")

img = Image.open("data/real/sample.jpg") 

img = img.convert("L")  # Grayscale
img = ImageEnhance.Contrast(img).enhance(2)  # Boost contrast
img = img.filter(ImageFilter.SHARPEN)

text = pytesseract.image_to_string(img)
print(text)
