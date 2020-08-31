import os
import random
from tkinter import *
from tkinter import messagebox, ttk
import pymysql


class bill:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1300x700+50+20")
        self.window.title("Billing")
        self.title = Label(self.window, text="Student Bills", bd=12, bg="#BDB76B", font=("arial", 15, "bold"), pady=2)
        self.title.pack(fill=X)

        self.window.resizable(False, False)

        Frame_1 = Frame(self.window, bg="#BDB76B")
        Frame_1.place(x=0, y=50, height=10, width=1400)

        show_list = []
        self.admission = IntVar()
        self.annual = IntVar()
        self.eca = IntVar()
        self.sem1 = IntVar()
        self.sem2 = IntVar()
        self.univ = IntVar()

        self.name = StringVar()
        self.course = StringVar()
        self.roll = StringVar()

        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search = StringVar()

        self.totals = StringVar()

        #  details frame
        L1 = LabelFrame(self.window, text="Fee Details", bg="#BDB76B",
                        font=("arial", 15, "bold"))
        L1.place(x=0, y=80, width=1290)

        lbl_name = Label(L1, text="Name", bg='#BDB76B', font=("arial", 12, "bold"))
        lbl_name.grid(row=0, column=0, padx=20, pady=5)

        ent_name = ttk.Combobox(L1, width=15, textvariable=self.name, state='readonly', font=("arial", 15, "bold"))
        ent_name.grid(row=0, column=1, pady=5, padx=10)

        self.con = pymysql.connect(host='localhost', user='root', password='', database='stm')
        self.cursor = self.con.cursor()
        self.listData = self.cursor.execute("select * from students")
        self.bill = self.cursor.fetchall()

        for i in self.bill:
            show_list.append((i[1]))
            ent_name['values'] = show_list

        lbl_id = Label(L1, text="Student Id", bg="#BDB76B", font=("arial", 12, "bold"))
        lbl_id.grid(row=0, column=2, padx=20, pady=5)

        ent_id = Entry(L1, width=12, textvariable=self.roll, font=("arial", 15, "bold"))
        ent_id.grid(row=0, column=3, pady=5, padx=10)

        lbl_course = Label(L1, text="Course", bg="#BDB76B", font=("arial", 12, "bold"))
        lbl_course.grid(row=0, column=4, padx=20, pady=5)

        ent_courses = ttk.Combobox(L1, width=15, textvariable=self.course, state='readonly', font=("arial", 15, "bold"))
        ent_courses['values'] = (' BSc(Hons)Computing  ', 'BSc(Hons)Ethical Hacking and CyberSecurity')
        ent_courses.grid(row=0, column=5, pady=5, padx=10)

        lbl_search = Label(L1, text="Bill no", bg="#BDB76B", font=("arial", 12, "bold"))
        lbl_search.grid(row=0, column=6, padx=20, pady=5)

        ent_search = Entry(L1, width=12, textvariable=self.bill_no, font=("arial", 15, "bold"))
        ent_search.grid(row=0, column=7, pady=5, padx=10)

        # BUTTON
        search_btn = Button(L1, text="Search", command=self.find_bill, bg='#FFE4C4', width=9,
                            font=("arial", 15, "bold"))
        search_btn.grid(row=0, column=8)

        # FRAME
        L2 = LabelFrame(self.window, bg="#BDB76B", fg="black", font=("arial", 15, "bold"))
        L2.place(x=5, y=170, width=440, height=380)

        lbl_admission = Label(L2, text="Admission Fee", font=("arial", 12, "bold"), bg="#BDB76B", fg="black", )
        lbl_admission.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        ent_admission = Entry(L2, font=("arial", 12), textvariable=self.admission, fg="black", relief=GROOVE)
        ent_admission.grid(row=0, column=1, padx=10, pady=10)

        lbl_annual = Label(L2, text="Annual Fee", font=("arial", 12, "bold"), bg="#BDB76B")
        lbl_annual.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        ent_annual = Entry(L2, font=("arial", 12), textvariable=self.annual, fg="black", relief=GROOVE)
        ent_annual.grid(row=1, column=1, padx=10, pady=10)

        lbl_eca = Label(L2, text="Extra Curricular Fee", font=("arial", 12, "bold"), bg="#BDB76B", fg="black")
        lbl_eca.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        ent_eca = Entry(L2, font=("arial", 12), textvariable=self.eca, fg="black", relief=GROOVE)
        ent_eca.grid(row=2, column=1, padx=10, pady=10)

        lbl_sem1 = Label(L2, text="Semester-1 Fee", font=("arial", 12, "bold"), bg="#BDB76B", fg="black")
        lbl_sem1.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        ent_sem1 = Entry(L2, font=("arial", 12), fg="black", textvariable=self.sem1, relief=GROOVE)
        ent_sem1.grid(row=3, column=1, padx=10, pady=10)

        lbl_sem2 = Label(L2, text="Semester-2 Fee", font=("arial", 12, "bold"), bg="#BDB76B", fg="black")
        lbl_sem2.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        ent_sem2 = Entry(L2, font=("arial", 12), fg="black", textvariable=self.sem2, relief=GROOVE)
        ent_sem2.grid(row=4, column=1, padx=10, pady=10)

        lbl_univ = Label(L2, text="University Registration Fee", font=("arial", 12, "bold"), bg="#BDB76B", fg="black")
        lbl_univ.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        ent_univ = Entry(L2, font=("arial", 12), fg="black", textvariable=self.univ, relief=GROOVE)
        ent_univ.grid(row=5, column=1, padx=10, pady=10)

        # bill area
        L3 = LabelFrame(self.window, bg="#BDB76B", fg="black", font=("arial", 15, "bold"))
        L3.place(x=450, y=170, width=840, height=380)

        bill_title = Label(L3, font=("arial", 15, "bold"))
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(L3, orient=VERTICAL)
        self.textarea = Text(L3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # button frame
        L4 = LabelFrame(self.window, bg="#BDB76B", fg="black",
                        font=("arial", 15, "bold"))
        L4.place(x=5, y=570, width=1285, height=100)

        Frame_b = Frame(L4, bg="#BDB76B")
        Frame_b.place(x=0, y=80, height=10, width=180)

        lbl_total = Label(L4, text="Total bill in Rs.", bg="#BDB76B", fg="black", font=("arial", 20, "bold"))
        lbl_total.grid(row=0, column=0, pady=1, sticky="w")

        ent_total = Entry(L4, width=18, textvariable=self.totals,state='readonly', font=("arial", 15, "bold"))
        ent_total.grid(row=0, column=1, padx=10, pady=1)

        L5 = Frame(L4, bg="#BDB76B")
        L5.place(x=650, y=0, width=580, height=80)

        tot_btn = Button(L5, text="Total", command=self.total, width=8, bg='#FFE4C4', font=("arial", 15, "bold"))
        tot_btn.grid(row=0, column=0, padx=15, pady=15)

        bil_btn = Button(L5, text="Generate Bill", command=self.particulars, bg='#FFE4C4', width=12,
                         font=("arial", 15, "bold"))
        bil_btn.grid(row=0, column=1, padx=15, pady=15)

        clr_btn = Button(L5, text="Clear", command=self.clear_ent, bg='#FFE4C4', width=8, font=("arial", 15, "bold"))
        clr_btn.grid(row=0, column=2, padx=15, pady=15)

        ext_btn = Button(L5, text="Close", command=self.close, bg='#FFE4C4', width=8, font=("arial", 15, "bold"))
        ext_btn.grid(row=0, column=3, padx=15, pady=15)

        self.welcome()
        self.window.mainloop()

    def total(self):
        """
    total:
    It helps to add all the integer values of the entry boxes.
        """
        try:
            self.admission_fee = self.admission.get()
            self.annual_fee = self.annual.get()
            self.eca_fee = self.eca.get()
            self.sem1_fee = self.sem1.get()
            self.sem2_fee = self.sem2.get()
            self.univ_fee = self.univ.get()

            self.total_fee = (
                    self.admission_fee +
                    self.annual_fee +
                    self.eca_fee +
                    self.sem1_fee +
                    self.sem2_fee +
                    self.univ_fee)

            self.total_tot = self.total_fee
            self.totals.set("Rs." + str(self.total_tot))
        except Exception as e:
            print(e)

    def welcome(self):
        """welcome:
    It helps to show the student id, course name, student name, and bill no in the bill area. """
        try:
            self.textarea.delete('1.0', END)
            self.textarea.insert(
                END, "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSTUDENT`S BILL PORTAL")
            self.textarea.insert(END, f"\n Student Id.:{self.roll.get()}")
            self.textarea.insert(END, f"\t\t\t\t\t\tCourse:{self.course.get()}")
            self.textarea.insert(END, f"\n Student Name:{self.name.get()}")
            self.textarea.insert(END, f"\t\t\t\t\t\tBill No.:{self.bill_no.get()}")
            self.textarea.insert(END,
                                 f"\n=====================================================================================================")

            self.textarea.insert(END, f"\n PARTICULARS\t\t\t\t\t\t\t\t\t\t\tAMOUNT")

            self.textarea.insert(END,
                                 f"\n=====================================================================================================")
        except Exception as e:
            print(e)

    def particulars(self):
        """particulars:
    It helps to get all the entry boxes values in the bill area.
        """
        try:
            if self.name.get() == "" or self.roll.get() == "" or self.course.get() == "":
                messagebox.showerror("ERROR", "Enter Fee Details")

            else:
                self.welcome()
                if self.admission.get() != 0:
                    self.textarea.insert(END, f"\nAdmission Fee\t\t\t\t\t\t\t\t\t\t\tRs.{self.admission_fee}")

                if self.annual.get() != 0:
                    self.textarea.insert(END, f"\nAnnual Fee\t\t\t\t\t\t\t\t\t\t\tRs.{self.annual_fee}")

                if self.eca.get() != 0:
                    self.textarea.insert(END, f"\nExtra Curricular Fee\t\t\t\t\t\t\t\t\t\t\tRs.{self.eca_fee}")

                if self.sem1.get() != 0:
                    self.textarea.insert(END, f"\nSemester-1 Fee\t\t\t\t\t\t\t\t\t\t\tRs.{self.sem1_fee}")

                if self.sem2.get() != 0:
                    self.textarea.insert(END, f"\nSemester-2 Fee\t\t\t\t\t\t\t\t\t\t\tRs.{self.sem2_fee}")

                if self.univ.get() != 0:
                    self.textarea.insert(END, f"\nUniversity Registration Fee\t\t\t\t\t\t\t\t\t\t\tRs.{self.univ_fee}")

                ######################
                self.textarea.insert(END,
                                     f"\n=====================================================================================================")

                self.textarea.insert(END, f"\nTotal Amount\t\t\t\t\t\t\t\t\t\t\tRs.{str(self.total_fee)}")

                self.textarea.insert(END,
                                     f"\n=================================****THANK YOU****===================================================")

                self.save_bill()
        except Exception as e:
            print(e)

    def save_bill(self):
        """save_bill:
    It asks user to save in any location of the computer."""
        try:
            op = messagebox.askyesno("Save Bill", "Do You Want TO Save The Bill?")
            if op > 0:
                self.bill_data = self.textarea.get('1.0', END)
                f = open("bills/" + str(self.bill_no.get()) + ".ent", "w")
                f.write(self.bill_data)
                f.close()
                messagebox.showinfo("Success", f"\nYour bill {self.bill_no.get()} has been saved successfully")
            else:
                return False
        except Exception as e:
            print(e)
    print("----------------------------------------------Functions of bills window---------------------------------------")
    print(save_bill.__doc__)

    def find_bill(self):
        """find_bill:
    This function helps to find the bill of the student."""
        try:
            present = "no"
            for i in os.listdir("BILLS/"):
                if i.split('.')[0] == self.bill_no.get():
                    f = open(f"BILLS/{i}", "r")
                    self.textarea.delete("1.0", END)
                    for d in f:
                        self.textarea.insert(END, d)
                    f.close()
                    present = "yes"
            if present == "no":
                messagebox.showerror("Error", "Bill Not Found!")
        except Exception as e:
            print(e)

    print(find_bill.__doc__)

    def clear_ent(self):
        """clear_ent:
    It clears all the entry boxes and bill area."""
        try:
            op = messagebox.askyesno("Clear", "Do you want to clear data?")
            if op > 0:
                self.sem1.set(0)
                self.annual.set(0)
                self.univ.set(0)
                self.eca.set(0)
                self.admission.set(0)
                self.sem2.set(0)

                self.name.set("")
                self.roll.set('')

                self.bill_no.set("")
                x = random.randint(1000, 9999)
                self.bill_no.set(str(x))

                self.course.set('')
                self.search.set("")

                self.totals.set("")

                self.welcome()
        except Exception as e:
            print(e)

    print(clear_ent.__doc__)

    def close(self):
        """close:
    It closes the bills window.
    """

        try:
            ob = messagebox.askyesno("Exit", "Do you want to exit?")
            if ob > 0:
                self.window.destroy()
        except Exception as e:
            print(e)

    print(close.__doc__)

# bill()
