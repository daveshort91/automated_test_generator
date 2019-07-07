import tkinter as tk
from tkinter.filedialog import askdirectory

class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x500")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.new_class = tk.Button(self)
        self.new_class["text"] = "New Class"
        self.new_class["command"] = self.class_form
        self.new_class.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def class_form(self):
        classForm = tk.Toplevel(root)
        display = tk.Label(classForm, text="New Class Form")
        display.grid(row=0)
        classNameLabel = tk.Label(classForm, text="Name")
        classNameLabel.grid(row=1, column=0)
        className = tk.Entry(classForm)
        className.grid(row=1, column=1)
        fileLocation = tk.Button(classForm, text="Choose Destination")
        fileLocation["command"] = self.get_directory
        fileLocation.grid(row=2, column=0)
        self.directoryPath = tk.Entry(classForm)
        self.directoryPath.grid(row=2, column=1)
        
        
    def get_directory(self):
        directoryName = askdirectory()
        self.directoryPath.insert(0, directoryName)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
