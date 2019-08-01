
# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 
  
  
# String which represent the QR code 
s = b'c2MAAoDuu0N4xjoIvLllVZtqAqbQbpxMxOnet1cCs00mj9NlJhm/RVVJD4oEY9F2LCcSsuuQixpQj8MVQfAoQZwR2efDNWTYYnueCUhA'
  
# Generate QR code 
url = pyqrcode.create(s)

  
# Create and save the png file naming "myqr.png" 
#url.eps("myqr.eps", scale = 1) 
url.png("45AQ955WES.png", scale = 5) 
