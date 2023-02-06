"""
QR code encoder/ decoder --> using the python qrcode library
QR CODE will have the data that is encoded
   can then decode the data
# maybe do qr code to my githubs account
# to decode -->pyzbar python module and pillow package
"""
import os
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

BASE_DIR = os.path.dirname(__file__)

def generate_qrcode(data):
   qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4
   )
   qr.add_data(data)
   qr.make(fit=True)
   img = qr.make_image(fill_color='blue', back_color='white')
   image_path = f"{BASE_DIR}/link_data.png"
   img.save(image_path)
   return image_path

## Import data from qr
def decode_qr(image_path):
   open_image = Image.open(image_path)
   decoded_data = decode(open_image)
   clean_data = str(decoded_data[0].data).split("'")[1]
   print(clean_data)

if __name__ == '__main__':
   link_data = 'https://github.com/TobiAdeleke1'
   image_path = generate_qrcode(link_data)
   decode_qr(image_path)

