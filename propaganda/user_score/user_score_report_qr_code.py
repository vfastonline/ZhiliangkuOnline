# encoding: utf-8

import qrcode

img = qrcode.make("http://www.zhiliangku.com/q/")
img.save("./score_qr_code.png")
