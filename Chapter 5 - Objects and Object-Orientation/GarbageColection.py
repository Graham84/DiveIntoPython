import fileinfo

def leakman():
    f = fileinfo.FileInfo("/music/_singles/kairo.mp3")

for i in range(100):
    leakman()