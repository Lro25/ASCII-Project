from PIL import Image

im = Image.open("../image.jpg")

print(im.format, im.size, im.mode)