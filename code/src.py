from PIL import Image
import colorama
from colorama import Fore, Back
import copy

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

def invert_brightness_matrix(size, matrix):
	inv_bright = matrix
	for i in range(size[1]):
		for k in range(size[0]):
			inv_bright[i][k] = ((inv_bright[i][k])*-1) + 255
	return inv_bright


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
	filename = input('Please type name for output txt file(include .txt extension): ')
	if filename == '':
		filename = 'image.txt'
	file1 = open((r'..\..\\' + filename), 'a')
	for i in range(size[1]):
		file1.write(''.join(pixels[i]) + '\n')
	file1.close()

def print_color_console(size, pixels, fore_color = None, back_color = None):
	if fore_color:
		text_color = fore_color.upper()
		print(text_color_choice(text_color))
	if back_color:
		background_color = back_color.upper()
		print(background_color_choice(background_color))
	for i in range(size[1]):
		print(''.join(pixels[i]))
	print('\033[39m')

def background_color_choice(color):
	color_choice = None
	if color == 'BLACK':
		color_choice = Back.BLACK
	if color == 'RED':
		color_choice = Back.RED
	if color == 'GREEN':
		color_choice = Back.GREEN
	if color == 'YELLOW':
		color_choice = Back.YELLOW
	if color == 'BLUE':
		color_choice = Back.BLUE
	if color == 'MAGENTA':
		color_choice = Back.MAGENTA
	if color == 'CYAN':
		color_choice = Back.CYAN
	if color == 'WHITE':
		color_choice = Back.WHITE
	return color_choice

def text_color_choice(color):
	color_choice = None
	if color == 'BLACK':
		color_choice = Fore.BLACK
	if color == 'RED':
		color_choice = Fore.RED
	if color == 'GREEN':
		color_choice = Fore.GREEN
	if color == 'YELLOW':
		color_choice = Fore.YELLOW
	if color == 'BLUE':
		color_choice = Fore.BLUE
	if color == 'MAGENTA':
		color_choice = Fore.MAGENTA
	if color == 'CYAN':
		color_choice = Fore.CYAN
	if color == 'WHITE':
		color_choice = Fore.WHITE
	return color_choice

# Program to be Run if Not Imported
def auto_program():
	filename = input("input image filename(place file two directories above): ")
	im_pre = Image.open("../../" + filename)
	resize_factor = int(input('Input Resize Factor: '))
	text_repeat_factor = int(input('Input Number of Times for Character to Repeat: '))
	text_color_option = int(input('Would you like text color (1 for yes, 2 for no): '))
# Color Options
	if text_color_option == 1:
		colorama.init()
		text_color_select = input('Please type in a color: ')
	else:
		text_color_select = None
	background_color_option = int(input('Would you like background color (1 for yes, 2 for no): '))
	if background_color_option == 1:
		if text_color_select == 2:
			colorama.init()
		background_color_select = input('Please type in a color: ')
	else:
		background_color_select = None

	im = resize_image(im_pre, resize_factor)
	pixel = pixel_matrix(im, im.size)
	bright = brightness_matrix(im.size, 'l', pixel)
	bright_copy = copy.deepcopy(bright)
	text = text_matrix(im.size, text_repeat_factor, bright)

#txt file options
	txt_file_option = int(input("Would you like a txt file copy?(Press 1 for yes, 2 for no): "))
	invert_textfile_option = int(input("Would you like to invert the txt file copy?(Press 1 for yes, 2 for no): "))
	if txt_file_option == 1 and invert_textfile_option == 1:
		inverted = invert_brightness_matrix(im.size, bright_copy)
		invert_text = text_matrix(im.size, text_repeat_factor, inverted)
		print_text_file(im.size, invert_text)
	if txt_file_option == 1 and invert_textfile_option != 1:
		print_text_file(im.size,text)
		
	if text_color_select or background_color_select:
		print_color_console(im.size, text, text_color_select, background_color_select)
	else: 
		print_text_console(im.size, text)


if __name__ == '__main__':
	auto_program()