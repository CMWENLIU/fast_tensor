import os
import numpy as np

def calculate(FullPath):
  with open(FullPath, 'r') as input:
    path, file = os.path.split(FullPath)
    allLines = input.readlines()
    needLines = [l[:-1] for l in allLines[-225:]]
    listnumbers = []
    for i in needLines:
      if ' acc ' and ', learning_rate' in i:
        start = i.index(' acc ') + 4
        end = i.index(', learning_rate')
        listnumbers.append(float(i[start : end]))
    print('----- For the result of: ' + FullPath )
    print('Training acc is: ', np.mean(listnumbers), ' for last ', len(listnumbers), ' average')

def main():
  calculate('/home/xxliu10/copiedrepos/tweets/vec300test.out')
if __name__ == '__main__':
  main()
