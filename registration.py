import tkinter
from tkinter import messagebox
from tkinter import *
from newproject import query


class registration:
    def __init__(self):
        self.window = Tk()
        self.window.title("Registration")
        self.window.configure(background='#BDB76B')
        self.window.geometry("600x500+500+200")
        self.window.resizable(False, False)

        self.frame_heading = Frame(self.window)
        self.frame_heading.pack()

        self.label_name = Label(self.frame_heading, bg='#BDB76B', text="Registration", font=('Arial', 20, 'bold'))
        self.label_name.pack()

        self.frame_login = Frame(self.window, bg='#BDB76B')
        self.frame_login.pack()

        self.label_username = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='#BDB76B', text="Username")
        self.label_username.grid(row=0, column=0, pady=10, padx=10, sticky=W)

        self.entry_username = Entry(self.frame_login, font=('arial', 10, 'bold'))
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        self.label_password = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='#BDB76B', text="Password")
        self.label_password.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        self.entry_password = Entry(self.frame_login, show='*', font=('arial', 10, 'bold'))
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.label_n = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='#BDB76B', text="Name")
        self.label_n.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        self.entry_n = Entry(self.frame_login, font=('arial', 10, 'bold'))
        self.entry_n.grid(row=2, column=1, padx=10, pady=10)

        self.label_a = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='#BDB76B', text="Address")
        self.label_a.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        self.entry_a = Entry(self.frame_login, font=('arial', 10, 'bold'))
        self.entry_a.grid(row=3, column=1, padx=10, pady=10)

        self.label_p = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='#BDB76B', text="Phone")
        self.label_p.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        self.entry_p = Entry(self.frame_login, font=('arial', 10, 'bold'))
        self.entry_p.grid(row=4, column=1, padx=10, pady=10)

        self.label_e = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='#BDB76B', text="Email")
        self.label_e.grid(row=5, column=0, padx=10, pady=10, sticky=W)

        self.entry_e = Entry(self.frame_login, font=('arial', 10, 'bold'))
        self.entry_e.grid(row=5, column=1, padx=10, pady=10)

        D_Frame = Frame(self.window, bd=4, relief=RIDGE, bg='#BDB76B')
        D_Frame.place(x=150, y=370, width=300, height=70)

        self.btn_regis = Button(D_Frame, bg='#FFE4C4', command=self.submit, text="Submit",
                                font=('Calibri', 20, 'bold'))
        self.btn_regis.grid(row=0, column=1,padx=10)

        self.btn_back = Button(D_Frame, bg='#FFE4C4', text="Back", command=self.back,
                               font=('Calibri', 20, 'bold'))
        self.btn_back.grid(row=0, column=0)

        self.btn_reset = Button(D_Frame, text='Reset', bg='#FFE4C4', font=('Calibri', 20, 'bold'), fg='black',
                                command=self.reset)
        self.btn_reset.grid(row=0, column=2,padx=7)

        self.window.mainloop()

    def reset(self):
        """reset:
    Resets all the entry boxes """
        try:
            if self.entry_username.get() != '' and self.entry_password.get() != '' and self.entry_n.get() != '' and \
                    self.entry_a.get() != '' and self.entry_p.get() != '' and self.entry_e.get() != '':
                self.entry_username.delete(0, END)
                self.entry_password.delete(0, END)
                self.entry_n.delete(0, END)
                self.entry_a.delete(0, END)
                self.entry_p.delete(0, END)
                self.entry_e.delete(0, END)
            else:
                tkinter.messagebox.showerror('Error', 'Please Fill Out The All Empty Boxes.')
        except Exception as e:
            print(e)
    print('----------------------------------------------Functions of regis window---------------------------------------')
    print(reset.__doc__)

    def back(self):
        """back:
    It helps to go back in login window"""
        try:
            messagebox.showinfo('Back', 'Going To The Sign In ')
            self.window.destroy()
            import login
        except Exception as e:
            print(e)
    print(back.__doc__)

    def clear(self):
        """clear:
    It helps to clear entry boxes after registering"""
        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)
        self.entry_n.delete(0, END)
        self.entry_a.delete(0, END)
        self.entry_p.delete(0, END)
        self.entry_e.delete(0, END)

    def submit(self):
        """submit:
    Stores the user details of the user into the program and opens the signup window for login.
                     """

        try:
            if self.entry_username.get() == '' or self.entry_password.get() == '' or self.entry_n.get() == '' \
                    or self.entry_a.get() == '' or self.entry_p.get() == '' or self.entry_e.get() == '':

                messagebox.showwarning('Error', 'All Fields Are Required')

            else:
                query.student().sign_up(self.entry_username.get(),
                                        self.entry_password.get(), self.entry_n.get(), self.entry_a.get(),
                                        self.entry_p.get(), self.entry_e.get())
                messagebox.showinfo('Success', 'Registered Successfully')
                self.clear()
                self.window.destroy()
                import login
        except Exception as e:
            print(e)

    print(submit.__doc__)

# registration()
