import json
import pyqrcode
data = "http://192.168.42.186:8000/info","c2MAAoDuu0N4xjoIvLllVZtqAqbQbpxMxOnet1cCs00mj9NlJhm/RVVJD4oEY9F2LCcSsuuQixpQj8MVQfAoQZwR2efDNWTYYnueCUhA"
jsondata = json.dumps(data)
qr = pyqrcode.create(jsondata)
qr.png('url&enqrid.png', scale=5)
