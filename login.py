from tkinter import *
from tkinter import messagebox

from cs19b.newproject import regis, stm_query
from cs19b.newproject.sms import Student


class LoginView:
    def __init__(self):

        self.window = Tk()
        self.window.title("User Login")
        self.window.configure(background='#BDB76B')
        self.window.geometry("400x300+500+200")
        self.window.resizable(False, False)

        self.frame_heading = Frame(self.window)
        self.frame_heading.pack()

        self.label_name = Label(self.frame_heading, bg='#BDB76B', text="User Login", font=('Arial', 20, 'bold'))
        self.label_name.pack()

        self.frame_login = Frame(self.window, bg='#BDB76B')
        self.frame_login.pack()

        self.label_un = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='#BDB76B', text="Username")
        self.label_un.grid(row=0, column=0, pady=10, padx=10, sticky=W)

        self.entry_un = Entry(self.frame_login, font=('arial', 10, 'bold'))
        self.entry_un.grid(row=0, column=1, padx=10, pady=10)

        self.label_pw = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='#BDB76B', text="Password")
        self.label_pw.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        self.entry_pw = Entry(self.frame_login, show='*', font=('arial', 10, 'bold'))
        self.entry_pw.grid(row=1, column=1, padx=10, pady=10)

        self.btn_login = Button(self.frame_login, bg='#FFE4C4', text="Log In", font=('Calibri', 20, 'bold'),
                                command=self.on_login_click)
        self.btn_login.grid(row=2, column=0)

        self.btn_regis = Button(self.frame_login, bg='#FFE4C4', text="Sign Up", font=('Calibri', 20, 'bold'),
                                command=self.signup)
        self.btn_regis.grid(row=2, column=1)

        self.window.mainloop()

    def on_login_click(self):
        if self.entry_un.get() == '' or self.entry_pw.get() == '':
            messagebox.showwarning('Error', 'All Fields Are Required')
        else:
            try:
                user = stm_query.student().sign_in(self.entry_un.get(), self.entry_pw.get())
                if user:
                    messagebox.showinfo('Success', 'Welcome')
                    self.window.destroy()
                    root = Tk()
                    iv = Student(root)
                else:
                    messagebox.showerror('Error', 'Invalid Id Or Password')

            except Exception as e:
                print(e)
                return False

    def signup(self):
        try:
            op = messagebox.askyesno("Registration Form", "Do You Want TO  Go To Registration Form?")
            if op > 0:
                self.window.destroy()
                regis.registration()
            else:
                return False
        except Exception as e:
            print(e)


LoginView()
