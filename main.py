import os
import gzip

def check(f, file):
    index = 0
    for line in f:
        index += 1
        if keyword.lower() in line.lower():
            print(f'{keyword} was found in {str(file)} on line {index}\n{line}')

def runSearch():
    for root, dirs, files in os.walk('Files/'):
        for file in files:
            if str(file).endswith('.gz'):
                with gzip.open('Files/' + file, 'rt') as f:
                    check(f, file)
            else:
                with open('Files/' + file, 'r') as f:   
                    check(f, file)

while True:
    print(f'Input keyword, what are we searching for?')
    keyword = input('')
    runSearch()