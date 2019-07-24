class SimpleTestWriter:
    filename = ""
    className = ""
    file = ""
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.create_file()
        self.write_packages()
        self.write_class_header()
        self.write_class_constructor()
        self.write_class_footer()
        
    def create_file(self):
        self.file = open(self.fileName + "/linkTest.java", "w+")

    def write_packages(self):
        self.file.write("import java.io.IOException;\nimport java.net.HttpURLConnection;\nimport java.net.MalformedURLException;\nimport java.net.URL;\nimport java.util.Iterator;\nimport java.util.List;\nimport org.openqa.selenium.By;\nimport org.openqa.selenium.WebDriver;\nimport org.openqa.selenium.WebElement;\nimport org.openqa.selenium.chrome.ChromeDriver;\r\n\n")
#Selenium code taken from:
#How to Find All/Broken links using Selenium Webdriver. (n.d.). Retrieved from https://www.guru99.com/find-broken-links-selenium-webdriver.html      
    def write_class_header(self):
        self.file.write("public class LinkTest {\r\n\n")
        self.file.write("\tprivate static WebDriver driver = null;\n\n")

    def write_class_constructor(self):
        self.file.write("\tpublic LinkTest(WebDriver webdriver){\r\n\n\t\tdriver = webdriver;\n\n");
        self.file.write("\t\tList<WebElement> links = driver.findElements(By.tagName(\"a\"));\n\n");
        self.file.write("\t\tIterator<WebElement> it = links.iterator();\n\n");
        self.file.write("\t\turl = it.next().getAttribute(\"href\");\n\n");
        self.file.write("\t\tif(url == null || url.isEmpty()){\n\t\t\tSystem.out.println(\"URL is either not configured for anchor tag or it is empty\");\n\t\t\tcontinue;\n\t\t}\n\n");
        self.file.write("\t\thuc = (HttpURLConnection)(new URL(url).openConnection());\n\n");
        self.file.write("\t\thuc.setRequestMethod(\"HEAD\");\n\n");
        self.file.write("\t\thuc.connect();\n\n");
        self.file.write("\t\trespCode = huc.getResponseCode();\n\n");
        self.file.write("\t\tif(respCode >= 400){\n\t\t\tSystem.out.println(url+\" is a broken link\");\n\t\t}\n\t\telse{\n\t\t\tSystem.out.println(url+\" is a valid link\");\n\t\t}\n");
        self.file.write("\t}\r\n");

    def write_class_footer(self):
        self.file.write("}\n")
        self.file.close()

        
        
