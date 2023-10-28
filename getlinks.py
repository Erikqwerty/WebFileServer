import os

class Links():
    def __init__(self, Links, Filename, Filesize):
        self.Links = Links
        self.Filename = Filename
        self.Filesize = Filesize
    

def getlinks(uri='ftp/'):
    files = os.listdir(uri)
    file_links = []
    i = 1
    for file in files:
        filename = str(i) + '. ' + file
        fileinfo = os.stat(uri+file)
        filesize = str(fileinfo.st_size) + '  байт.'
        file_links.append(Links(f'/download/{file}', filename, filesize))
        i+=1
    return file_links