import qrcode

img = qrcode.make("https://openai.com")
img.save("qrcode.png")

print("QR Code Generated")