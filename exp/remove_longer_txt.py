import glob
import os
import time

def removelongertxt(FullPath):
  read_files = glob.glob(FullPath)
  #path, file = os.path.split(FullPath)
  #filename = 'result.one'
  #filename = os.path.join(path, filename)
  #with open(filename, "w", encoding = 'utf-8') as outfile:
  count = 0
  for f in read_files:
    with open(f, "r") as infile:
      filename = f + '.new'
      with open (filename, 'w', encoding = 'utf-8') as outfile:
        for line in infile:
          if len(line) < 1000:
            outfile.write(line)
            count += 1
      print('------  ', f, 'finished!!' )
  print('------ total has: ', str(count), 'left for new files')

def main():
  fullpaths = ['/home/xxliu10/bigdata/largemovirerdata/*.txt'
  ]

  for fp in fullpaths:
    removelongertxt(fp) 

if __name__ == "__main__":
  main()

