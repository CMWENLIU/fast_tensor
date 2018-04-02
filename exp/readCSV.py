import csv

def readcsvfile(filepath):
  with open(filepath) as csvDataFile:
    negfile = filepath + '.neg.txt'
    posfile = filepath + '.pos.txt'
    with open(negfile, 'w', encoding = 'utf-8') as neg:
      with open(posfile, 'w', encoding = 'utf-8') as pos:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
          try:
            score = int(row[6])
            if score < 3:
              neg.write(row[9] + '\n')
            if score > 3:
              pos.write(row[9] + '\n')          
          except ValueError:
            pass
def main():
  fullpath = '/home/xxliu10/Downloads/Reviews.csv'
  readcsvfile(fullpath)
if __name__ == "__main__":
  main()

