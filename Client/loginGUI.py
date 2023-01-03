from tkinter import *

class loginGUI:
    
    id = -1
    
    
    def createGUI(self, client):
        
        def login():
            self.id = bank_client.service.login(usernameEntry.get(), passwordEntry.get())
            if self.id != -1: loginWindow.destroy()

        bank_client = client
        
        loginWindow = Tk()

        loginWindow.title("SimpleBank")
        loginWindow.geometry("300x150")
        loginWindow.resizable(0, 0)

        loginWindow.columnconfigure(1, weight=2)
        loginWindow.columnconfigure(2, weight=1)

        Label(text = "Login", width = 40).grid(row = 0, column = 1)

        Label(text = "Username").grid(row = 1, column = 0)
        usernameEntry = Entry()
        usernameEntry.grid(row = 1, column = 1)

        Label(text = "Password").grid(row = 2, column = 0)
        passwordEntry = Entry(show="*")
        passwordEntry.grid(row = 2, column = 1)

        loginBtn = Button(loginWindow, text = "Login", command= login, bg="green", fg="white")
        loginBtn.grid(row = 3, column = 1)

        loginWindow.mainloop()
    
    def getID(self):
        return self.id
