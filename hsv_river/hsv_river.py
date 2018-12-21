
'''
Image-to-HSV-Animation | Psychadelic Fx
Dec 20th, 2018 (post Stats Exam)

	[1] Benjamin Li		ECE		@ben.liiiii

'''

import numpy as np
from PIL import Image


# .... hue shift function  .......................

def hue_shift(img, amount):
	hsv_image = img.convert('HSV')
	hsv = np.array(hsv_image)
	hsv[..., 0] = (hsv[..., 0]+amount) % 360
	new_img = Image.fromarray(hsv, 'HSV')
	return new_img.convert('RGB')

# .... open image ................................

img_address = "" 

if(0): 						# img from CLI
	import argparse
	parser = argparse.ArgumentParser(description = 'type image-file-adrress')
	parser.add_argument("img", help="... image-file", type = String)
	args = parser.parse_args()
	img_address = args.img

else: 							# img from code
	img_address = "regression/regression.jpg"

img = Image.open(img_address)

frames = 30; i = 0;

while(i<frames):
	img = hue_shift(img, i*1)
	file_ = "regression/out%d.jpg" % i
	img.save(file_)
	i+=1