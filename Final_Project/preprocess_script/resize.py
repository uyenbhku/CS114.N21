import os
import constants
import numpy as np
import cv2
from PIL import Image
import pillow_heif


def resize(image, dim1, dim2):
	return cv2.resize(image, (dim1, dim2), interpolation=cv2.INTER_CUBIC)

def fileWalk(directory, destPath):
	try: 
		os.makedirs(destPath)
	except OSError:
		if not os.path.isdir(destPath):
			raise

	for subdir, dirs, files in os.walk(directory):
		for file in files:
			file = file.lower()
			filename = file.rsplit('.')[0] 
			if len(file) <= 4 or file[-4:] != '.jpg':
				## read heif file because iPhone has this format
				heif_file = pillow_heif.open_heif(os.path.join(subdir, file), convert_hdr_to_8bit=False, bgr_mode=True)
				pic = np.asarray(heif_file)
			else: 
				pic = cv2.imread(os.path.join(subdir, file))
			
			dim1 = len(pic)
			dim2 = len(pic[0])
			if dim1 > dim2:
				pic = np.rot90(pic)

			## Modify picture size here or can change DIM1 and DIM2 in constants.py
			picResized = resize(pic,constants.DIM1, constants.DIM2)
			cv2.imwrite(os.path.join(destPath, f'{filename}.jpg'), picResized)
		

def main():
	FOLDER_NAME = input('Type in folder name')
	prepath = os.path.join(os.getcwd(), FOLDER_NAME)
	glassDir = os.path.join(prepath, 'glass')
	paperDir = os.path.join(prepath, 'paper')
	cardboardDir = os.path.join(prepath, 'cardboard')
	plasticDir = os.path.join(prepath, 'plastic')
	metalDir = os.path.join(prepath, 'metal')
	trashDir = os.path.join(prepath, 'trash')
	compostDir = os.path.join(prepath, 'compost')

	destPath = os.path.join(os.getcwd(), f'{FOLDER_NAME}-resized')
	try: 
		os.makedirs(destPath)
	except OSError:
		if not os.path.isdir(destPath):
			raise

	#GLASS
	fileWalk(glassDir, os.path.join(destPath, 'glass'))

	#PAPER
	fileWalk(paperDir, os.path.join(destPath, 'paper'))

	#CARDBOARD
	fileWalk(cardboardDir, os.path.join(destPath, 'cardboard'))

	#PLASTIC
	fileWalk(plasticDir, os.path.join(destPath, 'plastic'))

	#METAL
	fileWalk(metalDir, os.path.join(destPath, 'metal'))

	#TRASH
	fileWalk(trashDir, os.path.join(destPath, 'trash'))  
    
    #COMPOST
	fileWalk(compostDir, os.path.join(destPath, 'compost'))  

if __name__ == '__main__':
    main()