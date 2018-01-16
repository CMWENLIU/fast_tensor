How to add prefix for all fils in a folder in linux:
for f in * ; do mv "$f" "PRE_$f" ; done

How to set Ununtu system to input chinese:
1 system settings from right up corner, lunguage support -> install remove lunguage and make chinese checked.
2 system settings text entry -> unchek show corrent input source in the menu bar 
3 hit '+' and choose pinyin (chinese) or wubi(chinese)  -> Done
------------------------------------------------- 
running records on KATE:
python train.py -i outdir/train.corpus  -nv 9000 --noise gs  -ctype kcomp -nd 2000
python pred.py -i bbcdata_prepare/train.corpus  -lm model  -o output/training.txt -e tr_embedding.txt
python pred.py -i bbcdata_prepare/test.corpus  -lm model  -o output/test.txt -e te_embedding.txt
python run_classifier.py output/training.txt bbcdata_prepare/train.labels output/test.txt bbcdata_prepare/test.labels -nv 200 -cv 5
------------------------------------------------
python train.py -i outdir/train.corpus  -nv 5000 --noise gs  -ctype kcomp -nd 300
python pred.py -i bbcdata_prepare/train.corpus  -lm model  -o output/training.txt 
python pred.py -i bbcdata_prepare/test.corpus  -lm model  -o output/test.txt 
python run_classifier.py output/training.txt bbcdata_prepare/train.labels output/test.txt bbcdata_prepare/test.labels -nv 200 -cv 5
----------
python train.py -i outdir/train.corpus  -nv 500  -ctype kcomp
python pred.py -i outdir/test.corpus -lm model  -o output/a.txt
python run_classifier.py output/tr.txt outdir/train.labels output/te.txt outdir/test.labels -nv 300 -cv 10
------------------------------------------------
How to list all my system space left and usage:
df -h
how to list all subfolders of a directory
du -h -d 1
d means depth of recursive 
---------------------------------------------------
How to rename all subfolders in a folder via shell script:
for x in *new*; do mv "$x" "${x//new/hpc}"; done
above command select all subfolders contain 'new' 
and replace 'new' with hpc for all folder names
--------------------------------------------------
How to connect hpc server and view files from linux file system:
click connect to server then input the following:
ssh://username@servername.example.com/
--------------------------------------------------
How to rename all files in shell script:
This rename *.txt to *.txt.new
for x in *.txt; do mv "$x" "${x%.txt}.txt.new"; done
--------------------------------------------------
How to set up, install and use stemmer from snow ball:
read this website : http://www.nltk.org/howto/stem.html
Install NLTK 
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
wordnew = stemmer.stem(word)
------------------------------------------------------------------------------------
How to launch jupyter notebook on server side and
view in brower of loal machine?
This is the page for refer: https://coderwall.com/p/ohk6cg/remote-access-to-ipython-notebooks-via-ssh
q1 on remote server: remote_user@remote_host$ ipython notebook --no-browser --port=8889
2 on local machine: local_user@local_host$ ssh -N -f -L localhost:8888:localhost:8889 remote_user@remote_host
3 view in local machine browser: localhost:8888
4 jupyter notebook list command on server will list all running notebooks
--------------------------------------------
This works for me to install tensorflow on hpc 

through anaconda:
conda install -c anaconda tensorflow 
--------------------------------------------
How to find my files by key words in name:
find . -name '*New R*'
-----------------------------------------
How to use SVMLight and SVMlight multiclasses?
Just download from site: https://www.cs.cornell.edu/people/tj/svm_light/svm_multiclass.html
Down load the Linux (64-bit): http://download.joachims.org/svm_multiclass/current/svm_multiclass_linux64.tar.gz
Then unzip, then tar -xvf filename.
Then make file executable, then use command to do tasks
svm_multiclass_learn -c 5000 example4/train.dat example4/model 
svm_multiclass_classify example4/test.dat example4/model example4/predictions
That's it!
------------------------------------------
How to solve the problem of import numpy as np failure?
Delete token.py in your machine, and then reinsatll Anaconda agin
to use numpy, 
don't need to install numpy in anaconda, since it is already installed
when you install anaconda, and can be seen use 'conda list'
Read this link for details 'https://bugs.python.org/issue21924'
-------------------------------------------
How to debug the problem of 'utf-8' 
first make sure all files are in utf-8, if not, use 'Utfcast Express'
to convert in Windows 
Second, if you try to reading a file which is being created, will lead to 
this kind of problem also.
  

