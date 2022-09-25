from os import path

def createFile(fpath):
    if not (path.isfile(fpath)):
        f = open(fpath, 'w')
        f.write('Hello World!')
        f.close()

createFile('test.txt')
print("File created successfully!")