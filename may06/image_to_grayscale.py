from PIL import Image

img = Image.open("photo.jpg")

gray = img.convert("L")

gray.save("gray_photo.jpg")

print("Converted to grayscale")