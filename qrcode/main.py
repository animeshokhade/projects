from pyzbar.pyzbar import decode
from PIL import Image
import qrcode

data = "Don't forget to subscribe"

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

qr.add_data(data)
qr.make(fit = True)

img = qr.make_image(fill_color = 'teal', back_color = 'white') 

img.save('/Users/animesh/Documents/sde/projects/qrcode/myqr.png')

img = Image.open('/Users/animesh/Documents/sde/projects/qrcode/myqr.png')

result = decode(img) 
print(result)