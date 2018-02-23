import glob
import os
import time

def combinefiles(FullPath):
  read_files = glob.glob(FullPath)
  path, file = os.path.split(FullPath)
  filename = 'result.one'
  filename = os.path.join(path, filename)
  with open(filename, "w", encoding = 'utf-8') as outfile:
    for f in read_files:
      with open(f, "r") as infile:
        outfile.write(
infile.readline() + '\n')


def main():
  fullpaths = ['/home/xxliu10/Downloads/aclImdb/test/neg/*.txt',
  '/home/xxliu10/Downloads/aclImdb/test/pos/*.txt',
  '/home/xxliu10/Downloads/aclImdb/train/neg/*.txt',
  '/home/xxliu10/Downloads/aclImdb/train/pos/*.txt',
  '/home/xxliu10/Downloads/aclImdb/train/unsup/*.txt'
  ]

  for fp in fullpaths:
    start = time.time()
    combinefiles(fp)
    print('------  ', fp, 'finished' + '\n' + 'Took:  ' +  str(time.time() - start) + '   seconds ' )  

if __name__ == "__main__":
  main()

