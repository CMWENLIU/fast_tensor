import os
import glob


def renamef(folder):
	os.chdir(foldername)
	for filename in os.listdir(os.getcwd()):
		print (filename)
		newname = filename.replace(').txt', '.txt')
		newname = newname.replace('business(', 'business')
		os.rename(filename, newname)			

def sep_tr_te(tr, te):
	dirs_tr= os.listdir(tr) # get all files' and folders' names in the directory
	dirs_te= os.listdir(te)
	for di in dirs_tr: # loop through all the files and folders
		current_path = os.path.join(tr, di)
		files = glob.glob(current_path + '/*')
		sep = len(files)//3
		for f in sorted(files)[:sep]:
			os.remove(f)

	for di in dirs_te: # loop through all the files and folders
		current_path = os.path.join(te, di)
		files = glob.glob(current_path + '/*')
		sep = len(files)//3
		for f in sorted(files)[sep:]:
			os.remove(f)

if __name__ == "__main__":
	sep_tr_te('/home/xxliu10/running/KATE/20_newsgroups_training',
	 '/home/xxliu10/running/KATE/20_newsgroups_test')

	
