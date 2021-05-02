from PIL import Image

asc = '`^\\",:;Il!i~+_-?][}{1)(|\\\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

# Resizes Image Based on Factor Parameter
def resize_image(im_pre, FACT):	
	return im_pre.resize((im_pre.size[0]//FACT,im_pre.size[1]//FACT))

def get_size(im):
	return im.size


def pic_size():
	print('Pixel Matrix Size: ' + str(size))

# Returns Matrix of Pixel RGB Values
def pixel_matrix(im, size):
	pixels = []
	for i in range(size[1]):
		pixels.append([])
		for k in range(size[0]):
			pixels[i].append(im.getpixel((k,i)))
	return pixels

# Return Matrix of Brightness Values
def brightness_matrix(size, b, matrix):
	pixels = matrix
	if b == 'a':
		for i in range(size[1]):
		        for k in range(size[0]):
		                pixels[i][k] = round((pixels[i][k][0] + pixels[i][k][1] + pixels[i][k][2])/3)
	if b == 'l':	                
		for i in range(size[1]):
		        for k in range(size[0]):
		                pixels[i][k] = round((.21 * pixels[i][k][0]) + (.72 * pixels[i][k][1]) + (.07 * pixels[i][k][2]))
	if b == 'm':	                
		for i in range(size[1]):
		        for k in range(size[0]):
		                pixels[i][k] = round((max(pixels[i][k]) + min(pixels[i][k])) / 2)
	return pixels	                

# Returns Matrix of ASCII Characters
def text_matrix(size, sym_repeat_fact, matrix):
	pixels = matrix
	for i in range(size[1]):
	        for k in range(size[0]):
	                pixels[i][k] = asc[round((pixels[i][k] * 64) / 255)] * sym_repeat_fact
	return pixels

# Prints Joined Matrix of ASCII Characters to the Console
def print_text_console(size, pixels):
	for i in range(size[1]):
		print(''.join(pixels[i]))

# Prints Joined Matrix of ASCII Characters to a .txt File
def print_text_file(size, matrix):
	pixels = matrix
	file1 = open(r"..\..\image.txt", "a")
	for i in range(size[1]):
		file1.write(''.join(pixels[i]) + '\n')
	file1.close()


# Program to be Run if Not Imported
def auto_program():
	im_pre = Image.open("../../image2.jpeg")
	resize_factor = int(input('Input Resize Factor: '))
	text_repeat_factor = int(input('Input Number of Times for Character to Repeat: '))
	im = resize_image(im_pre, resize_factor)
	print(im.size)
	pixel = pixel_matrix(im, im.size)
	bright = brightness_matrix(im.size, 'l', pixel)
	text = text_matrix(im.size, text_repeat_factor, bright)
	print_text_console(im.size, text)
	print_text_file(im.size,text)

if __name__ == '__main__':
	auto_program()