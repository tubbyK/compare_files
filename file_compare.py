import string
import hashlib

class cmpfiles():
    def __init__(self, files):
        self.contents = [self.read_file(file) for file in files]
        self.num_files = len(self.contents)
        if self.num_files <2:
            print('Invalid for fewer than 2 files')
            exit()

    def cmpbytes(self):
        # preferred and faster than hashing
        results = []
        for i in range(self.num_files):
            for j in range(i+1, self.num_files):
                results.append(self.contents[i]==self.contents[j])
        return results

    def cmphash(self):
        hashes = [self.hash_file(content) for content in self.contents]
        results = []
        for i in range(self.num_files):
            for j in range(i+1, self.num_files):
                results.append(hashes[i]==hashes[j])
        return results

    def hash_file(self, txt):
        h = hashlib.md5()
        h.update(txt)
        return h.hexdigest()

    def read_file(self, file):
        with open(file, 'rb') as f:
            contents = f.read()
        return contents

if __name__ == '__main__':
    import os
    fld = ''
    files = ['\\'.join([fld,file]) for file in os.listdir(fld)]
    [print(file) for file in files]
    c = cmpfiles(files)
    print(c.cmpbytes())
    print(c.cmphash())