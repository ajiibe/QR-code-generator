import qrcode

def generate_qr_code(text):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(text)
    qr.make()
    image = qr.make_image()
    image.save("qrcode.png")

if __name__ == "__main__":
    text = "https://github.com/yourusername/qr-code-generator"
    generate_qr_code(text)
