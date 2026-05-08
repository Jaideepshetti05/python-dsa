
from PIL import Image

img = Image.open("sample.jpg")
img = img.resize((100, 50))
img = img.convert("L")

chars = "@#S%?*+;:,."

for y in range(img.height):
    for x in range(img.width):
        pixel = img.getpixel((x, y))
        print(chars[pixel // 25], end="")
    print()