import urllib.request
import zbarlight
from PIL import Image

with urllib.request.urlopen("https://freess.cx/images/servers/us01.png") as url:
    s=url.read()
print(s)
# 上面s是什么数据类型？是utf-8?
# code=zbarlight.qr_code_scanner(s,328,328)

# print('QR code: %s' %code.decode())
