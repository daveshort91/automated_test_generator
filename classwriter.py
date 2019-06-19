import requests
import urllib.request

class ClassWriter:
    filename = ""
    filepath = ""
    file = ""
    def __init__(self, filename):
        self.filename = filename

    def createfile(self):
        self.file = open(self.filename + ".cs", "w+")

    def setfilepath(self, filepath):
        self.filepath = filepath

    def writepackages(self):
        self.file.write("using OpenQA.Selenium;\nusing OpenQA.Selenium.Interactions\r\n\n")

    def writeclassheader(self, classname):
        self.file.write("public class " + classname + "{\r\n\n")

    def writemethodhead(self, name):
        self.file.write("public IWebElement get" + name + "(){\r\n");

    def writemethodend(self):
        self.file.write("}\r\n\n")

    def writefindelementbyid(self, id, variable):
        self.file.write("return Driver.FindElement(By.id(\"" + id + "\"));\r\n")

    def writefindelementbycss(self, selector, variable):
        self.file.write("return Driver.FindElement(By.cssSelector(\"" + selector + "\"));\r\n")

    def writefindelementbyxpath(self,path, variable):
        self.file.write("return Driver.FindElement(By.XPath(\"" + path + "\"));\r\n")

    def writefooter(self):
        self.file.write("}\r\n")
        self.file.close()
