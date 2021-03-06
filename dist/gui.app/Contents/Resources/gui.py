import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from page import Page
from simpletestwriter import SimpleTestWriter


class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x300")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        instruct = tk.Label(self, text="Click the button to create a new element getter class.\n1. Capitalize the first letter of the class name.\n2. Select a directory within your project to save the class file.\n3. Enter a url with the \"https://\" prefix.\n4. Select a language.\n")
        instruct.pack()
        self.new_class = tk.Button(self)
        self.new_class["text"] = "New Class"
        self.new_class["command"] = self.class_form
        self.new_class.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def class_form(self):
        self.v = tk.IntVar()
        
        self.classForm = tk.Toplevel(root)
        display = tk.Label(self.classForm, text="New Class Form")
        display.grid(row=0)
        #Name
        classNameLabel = tk.Label(self.classForm, text="Class Name")
        classNameLabel.grid(row=1, column=0)
        self.className = tk.Entry(self.classForm)
        self.className.grid(row=1, column=1)
        #File Destination
        fileLocation = tk.Button(self.classForm, text="Choose Destination")
        fileLocation["command"] = self.get_directory
        fileLocation.grid(row=2, column=0)
        self.directoryPath = tk.Entry(self.classForm)
        self.directoryPath.grid(row=2, column=1)
        #URL fields
        urlLabel = tk.Label(self.classForm, text="URL")
        urlLabel.grid(row=3, column=0)
        self.url = tk.Entry(self.classForm)
        self.url.grid(row=3, column=1)
        #Language Radio Button
        languageLabel = tk.Label(self.classForm, text="Language")
        languageLabel.grid(row=4,column=0)
        self.languageCsharp = tk.Radiobutton(self.classForm, text="C#", variable=self.v, value=1).grid(row=4, column=1)
        self.languageJava = tk.Radiobutton(self.classForm, text="Java", variable=self.v, value=2).grid(row=4, column=2)
        #Submit Button
        submitButton = tk.Button(self.classForm, text="Submit")
        submitButton["command"] = self.submit_form
        submitButton.grid(row=6, column=3)
        
    
        
    def incomplete_form(self):
        self.incompleteFormError = tk.Toplevel(root)
        incompleteLabel = tk.Label(self.incompleteFormError, text="Review instructions and fill out all fields before submitting")
        incompleteLabel.pack()
        closeButton = tk.Button(self.incompleteFormError, text="Close",fg="red")
        closeButton["command"] = self.close_alert
        closeButton.pack()

    def close_alert(self):
        self.incompleteFormError.destroy()
        
    def submit_form(self):
        className = self.className.get()
        directory = self.directoryPath.get()
        language = self.v.get()
        fullPath = directory + '/' + className.lower()
        url = self.url.get()
        urlPre = url[0:7]
        fChar = ""
        if (className != ""):
            fChar = className[0]    
        if (url != "" and className != "" and language != 0 and urlPre == "https://" and fChar.isUpper()):
            newClass = Page(url, fullPath, language, className)
            if (language == 2):
                simpleTest = SimpleTestWriter(directory)  
            self.classForm.destroy()
        else:
            self.incomplete_form()         
            
        
    def get_directory(self):
        directoryName = askdirectory()
        self.directoryPath.insert(0, directoryName)


root = tk.Tk()
root.title("TestMinion")
app = Application(master=root)
app.mainloop()
