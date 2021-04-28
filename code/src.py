from PIL import Image

im = Image.open("../../image.jpeg")

print('Pixel Matrix Size: ' + str(im.size))

pixels = []

for i in range(1600):
	pixels.append([])
	for k in range(900):
		pixels[i].append(im.getpixel((k,i)))


for i in range(1600):
        for k in range(900):
                pixels[i][k] = int((pixels[i][k][0] + pixels[i][k][1] + pixels[i][k][2])/3)


asc = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

for i in range(1600):
        for k in range(900):
                pixels[i][k] = asc[round((pixels[i][k] * 64) / 255)]

for i in range(1600):
        print(''.join(pixels[i]))

