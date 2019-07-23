import requests
import urllib.request

class ClassWriter:
    filename = ""
    filepath = ""
    file = ""
    def __init__(self, filename, lang):
        self.filename = filename
        self.lang = lang

    def create_file(self):
        if (self.lang == 1):
            self.file = open(self.filename + ".cs", "w+")
        elif (self.lang == 2):
            self.file = open(self.filename + ".java", "w+")

    def set_file_path(self, filepath):
        self.filepath = filepath

    def write_packages(self):
        if (self.lang == 1):
            self.file.write("using OpenQA.Selenium;\nusing OpenQA.Selenium.Interactions\r\n\n")
        elif (self.lang == 2):
            self.file.write("import org.openqa.selenium.By;\nimport org.openqa.selenium.WebDriver;\nimport org.openqa.selenium.WebElement;\nimport org.openqa.selenium.FindBy;\r\n\n")
            
    def write_class_header(self, classname):
        self.file.write("public class " + classname + " {\r\n\n")
        if (self.lang == 1):
            self.file.write("\tprivate IWebDriver Driver;\n\n")
        elif (self.lang == 2):
            self.file.write("\tprivate WebDriver driver;\n\n")
            
    def write_class_constructor(self, classname):
        if (self.lang == 1):
            self.file.write("\tpublic " + classname + "(IWebDriver driver){\r\n\t\tDriver = driver;\n\t}\r\n")
        elif (self.lang == 2):
            self.file.write("\tpublic " + classname + "(WebDriver webdriver){\r\n\t\tdriver = webdriver;\n\t}\r\n")
        
    def write_method_head(self, name):
        if (self.lang == 1):
            self.file.write("\tpublic IWebElement " + name.lower() + "(){\r\n")
        elif (self.lang == 2):
            self.file.write("\tpublic WebElement " + name.lower() + "(){\r\n")
            
    def write_method_end(self):
            self.file.write("\t}\r\n\n")
            
    def write_find_element_by_id(self, idName):
        if (self.lang == 1):
            self.file.write("\t\treturn Driver.FindElement(By.id(\"" + idName + "\"));\r\n")
        elif (self.lang == 2):
            self.file.write("\t\treturn driver.findElement(By.id(\"" + idName + "\"));\r\n")
            
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
            
