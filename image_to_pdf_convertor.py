#creating pdf 
try:
	from PIL import Image
except:
	input('\nPillow library will be installed on your machine, press enter to continue \n')
	from pip._internal import main as pipmain
	pipmain(['install', 'pillow'])
	try:
		from PIL import Image
	except:
		input("\nPillow library not installed. May be there is no internet connection, try again with active connection or manually install by running 'pip install pillow' command in Command Prompt.\nPress enter to exit and run script again.")
		quit()
import os
imagenamelist=os.listdir('input_images')
for i in range(len(imagenamelist)):
	if(imagenamelist[i].split(".")[1]=='txt'):
		continue
	image1 = Image.open('input_images/'+imagenamelist[i])
	im1 = image1.convert('RGB')
	im1.save('pdf_files/'+imagenamelist[i].split('.')[0]+'.pdf')
input('***\nConversion done successfully, pdf files saved in "pdf_files" folder press enter to close program\n***')