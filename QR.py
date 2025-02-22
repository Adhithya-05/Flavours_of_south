import qrcode

def generate_qr_code(link, filename="qr_code.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    link = "https://adhithya-05.github.io/Flavours_of_south.github.io/#order"
    generate_qr_code(link)
