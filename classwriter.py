import requests
import urllib.request

class ClassWriter:
    filename = ""
    filepath = ""
    file = ""
    def __init__(self, filename):
        self.filename = filename

    def createfile():
        self.file = open(self.filename, "w+")

    def setfilepath(filepath):
        self.filepath = filepath

    def writeheader(classname):
        file.write("public class " + classname + "{\r\n")

    def writefooter():
        file.write("}\r\n")
        file.close()

    
