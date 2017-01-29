import os

print os
print os.listdir("C:\\Users\\Graham\\music")
dirname = "C:\\"
print os.listdir(dirname)

print [f for f in os.listdir(dirname) if
os.path.isfile(os.path.join(dirname, f))]

print [f for f in os.listdir(dirname) if
os.path.isdir(os.path.join(dirname, f))]

print os.getcwd()

def listDirectory(directory, fileExtList):
    "get list of file info objects for files of particular extensions"
    fileList = [os.path.normcase(f)
                for f in os.listdir(directory)]
    fileList = [os.path.join(directory, f)
                for f in fileList
                if os.path.splitext(f)[1] in fileExtList]