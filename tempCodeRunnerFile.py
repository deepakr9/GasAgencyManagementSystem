import csv

with open("file.csv", 'w') as f:
  for i in range(5):
    res = input()
    f.write(res)