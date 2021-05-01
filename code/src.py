from PIL import Image

im_pre = Image.open("../../image2.jpeg")

FACT = int(input('Input Resize Factor: '))

sym_repeat_fact= int(input('Repeat symbol how many times: '))

im = im_pre.resize((im_pre.size[0]//FACT,im_pre.size[1]//FACT))

size = im.size

print('Pixel Matrix Size: ' + str(size))

pixels = []

for i in range(size[1]):
	pixels.append([])
	for k in range(size[0]):
		pixels[i].append(im.getpixel((k,i)))


for i in range(size[1]):
        for k in range(size[0]):
                pixels[i][k] = round((pixels[i][k][0] + pixels[i][k][1] + pixels[i][k][2])/3)

for i in range(size[1]):
        for k in range(size[0]):
                pixels[i][k] = round((.21 * pixels[i][k][0]) + (.72 * pixels[i][k][1]) + (.07 * pixels[i][k][2]))

for i in range(size[1]):
        for k in range(size[0]):
                pixels[i][k] = round((max(pixels[i][k]) + min(pixels[i][k])) / 2)


asc = '`^\\",:;Il!i~+_-?][}{1)(|\\\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'


for i in range(size[1]):
        for k in range(size[0]):
                pixels[i][k] = asc[round((pixels[i][k] * 64) / 255)] * sym_repeat_fact

for i in range(size[1]):
        print(''.join(pixels[i]))

