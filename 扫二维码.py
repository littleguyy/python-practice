#from PIL import Image
#import zbarlight

#file_path = 'i:/jpcxxoo.png'
#with open(file_path, 'rb') as image_file:
#    image = Image.open(image_file)
#    image.load()

#codes = zbarlight.scan_codes('qrcode', image)
#print('QR codes: %s' % codes)

from PIL import Image
import zbarlight

file_path = 'i:/jpcxxoo.png'
with open(file_path, 'rb') as image_file:
    image = Image.open(image_file)
    image.load()
converted_image = image.convert('L')  # Convert image to gray scale (8 bits per pixel).
image.close()

raw = converted_image.tobytes()  # Get image data.
print(raw)
width, height = converted_image.size  # Get image size.
code = zbarlight.qr_code_scanner(raw, width, height)

print('QR code: %s' %code.decode())
