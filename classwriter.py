import requests
import urllib.request

class ClassWriter:
    filename = ""
    filepath = ""
    file = ""
    def __init__(self, filename):
        self.filename = filename

    def create_file(self):
        self.file = open(self.filename + ".cs", "w+")

    def set_file_path(self, filepath):
        self.filepath = filepath

    def write_packages(self):
        self.file.write("using OpenQA.Selenium;\nusing OpenQA.Selenium.Interactions\r\n\n")

    def write_class_header(self, classname):
        self.file.write("public class " + classname + "{\r\n\n")

    def write_method_head(self, name):
        self.file.write("\tpublic IWebElement " + name + "(){\r\n");

    def write_method_end(self):
        self.file.write("\t}\r\n\n")

    def write_find_element_by_id(self, idName):
        self.file.write("\t\treturn Driver.FindElement(By.id(\"" + idName + "\"));\r\n")

    def write_find(self, name, element):
        self.write_method_head(name)
        self.write_find_element_by_id(element)
        self.write_method_end()

    def format_buttons(self, buttons):
        for button in buttons:
            name = button + "_button"
            self.write_find(name, button)

    def format_radio_buttons(self, buttons):
        for button in buttons:
            name = button + "_radio"
            self.write_find(name, button)

    def format_text_fields(self, textFields):
        for field in textFields:
            name = field + "_text"
            self.write_find(name, field)

    def format_submit_buttons(self, submitButtons):
        for button in submitButtons:
            name = button + "_submit"
            self.write_find(name, button)

    def writefindelementbycss(self, selector, variable):
        self.file.write("return Driver.FindElement(By.cssSelector(\"" + selector + "\"));\r\n")

    def writefindelementbyxpath(self,path, variable):
        self.file.write("return Driver.FindElement(By.XPath(\"" + path + "\"));\r\n")

    def write_footer(self):
        self.file.write("}\r\n")
        self.file.close()
