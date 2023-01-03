from tkinter import *
from tkinter import messagebox

class serviceGUI:

    def createGUI(self, i, client):

        def exit():
            window.destroy()

        def withdrawalOnClick():
            
            def withdrawal():
                reply = bank_client.service.withdrawal(id, amountEntry.get())
                if reply == "Balance is not enough!":
                    messagebox.showerror("Simple Bank", reply)
                else:
                    messagebox.showinfo("Simple Bank", reply)
                top.destroy()
            
            top = Toplevel()
            top.geometry("200x80")
            top.resizable(0, 0)

            Label(top,text="Enter Amount: ").pack()
            amountEntry = Entry(top)
            amountEntry.pack()
            okBtn = Button(top, text="OK",padx=20, command=withdrawal, bg="green", fg="white")
            okBtn.pack()
        
        def depositOnClick():
            
            def deposit():
                reply = bank_client.service.deposit(id, amountEntry.get())
                messagebox.showinfo("Simple Bank", reply)
                top.destroy()

            top = Toplevel()
            top.geometry("200x80")
            top.resizable(0, 0)

            Label(top,text="Enter Amount: ").pack()
            amountEntry = Entry(top)
            amountEntry.pack()
            okBtn = Button(top, text="OK",padx=20, command=deposit, bg="green", fg="white")
            okBtn.pack()

        def showBalance():
            reply = bank_client.service.showBalance(id)
            messagebox.showinfo("Simple Bank", reply)

        bank_client = client
        id = i

        window = Tk()
        window.title("SimpleBank")
        window.geometry("400x200")
        window.resizable(0, 0)

        middle_frame1 = Frame(window, width=200, height=100)
        middle_frame1.grid(row=1, column=0, sticky=W)

        middle_frame2 = Frame(window, width=200, height=100)
        middle_frame2.grid(row=1, column=1, sticky=W)

        bottom_frame1 = Frame(window, width=200, height=100)
        bottom_frame1.grid(row=2,column=0)

        bottom_frame2 = Frame(window, width=200, height=100)
        bottom_frame2.grid(row=2,column=1)


        withdrawalBtn = Button(window,text="Withdrawal", padx=45, pady=20, command= withdrawalOnClick, bg="green", fg="white")
        withdrawalBtn.grid(row = 1, column = 0)

        depositBtn = Button(window,text="Deposit", padx=50, pady=20, command= depositOnClick, bg="green", fg="white")
        depositBtn.grid(row = 1, column = 1)

        showBalanceBtn = Button(window,text="Show Balance", padx=40, pady=20, command= showBalance, bg="green", fg="white")
        showBalanceBtn.grid(row = 2, column = 0)

        exitBtn = Button(window, text="Exit", padx=60, pady=20, command=exit, bg="red", fg="white")
        exitBtn.grid(row=2, column=1)

        window.mainloop()