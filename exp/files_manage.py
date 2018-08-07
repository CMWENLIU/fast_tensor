import os


def renamef(folder):
	os.chdir(foldername)
	for filename in os.listdir(os.getcwd()):
		print (filename)
		newname = filename.replace(').txt', '.txt')
		newname = newname.replace('business(', 'business')
		os.rename(filename, newname)			

def sep_tr_te(tr, te):
	directory_list = list()
	for root, dirs, files in os.walk(tr):
		for name in dirs:
			directory_list.append(os.path.join(root, name))
	print (str(len(directory_list)))

if __name__ == "__main__":
	sep_tr_te('~/running/KATE/', '_')


'''to try
import os

filenames= os.listdir (".") # get all files' and folders' names in the current directory

result = []
for filename in filenames: # loop through all the files and folders
    if os.path.isdir(os.path.join(os.path.abspath("."), filename)): # check whether the current object is a folder or not
        result.append(filename)
        
result.sort()

f= open('list.txt','w')
for index,filename in enumerate(result):
    f.write("%s. %s \n"%(index,filename))

f.close()

'''
	
