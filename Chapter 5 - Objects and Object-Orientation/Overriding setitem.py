import fileinfo

def __setitem__(sef, key, item):
    if key == "name" and item:
        self.parse(item)
    FileInfo.__setitem__(self, key, item)
