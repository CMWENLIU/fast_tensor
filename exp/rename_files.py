import os
		
foldername = 'test/pred_business'
if __name__ == "__main__":
	os.chdir(foldername)
	for filename in os.listdir(os.getcwd()):
		print (filename)
		newname = filename.replace(').txt', '.txt')
		newname = newname.replace('business(', 'business')
		os.rename(filename, newname)