import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data("bitcoin:1P2JcDruZRQaFmxmygjLpjn4mCAiKt53Cg")
qr.make(fit=True)

img = qr.make_image()

img.save("jpcxxoo.png")
