cd ~
# You can change what anaconda version you want at 
# https://repo.continuum.io/archive/
wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
bash Anaconda3-5.0.1-Linux-x86_64.sh -b -p ~/anaconda
rm Anaconda3-5.0.1-Linux-x86_64.sh
echo 'export PATH="~/anaconda/bin:$PATH"' >> ~/.bashrc 

# Refresh basically
source ~/.bashrc
source ~/.bashrc
source ~/.bashrc

conda update conda
# Refresh for updating
source ~/.bashrc
source ~/.bashrc
source ~/.bashrc
# Install tf-gpu v1.3
conda install -c jjhelmus tensorflow-gpu-base 

#install gensim
conda install gensim
source ~/.bashrc
source ~/.bashrc
source ~/.bashrc
cd

