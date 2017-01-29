import fileinfo


# getitem

def __getitem__(self, key): return self.data[key]

f = fileinfo.FileInfo("/music/_singles/kairo.mp3")

print f

print f.__getitem__("name")

print f["name"]


# setitem

def __setitem__(self, key, item): self.data[key] = item

f.__setitem__("genre", 31)

print f

f["genre"] = 32

print f
