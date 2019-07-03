import tkinter as tk

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

    def say_hi(self):
        print("hi there, everyone!")

    def class_form(self):
        print("filler\n")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
