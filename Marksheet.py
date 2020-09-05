import os
from tkinter import *
from tkinter import messagebox, ttk
import pymysql


class student_mark_sheet:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1350x700+50+20")
        self.window.title("Billing")
        self.title = Label(self.window, text="Student Mark sheet", bd=12, bg="#BDB76B", font=("arial", 15, "bold"),
                           pady=2)
        self.title.pack(fill=X)

        self.window.resizable(False, False)

        Frame_1 = Frame(self.window, bg="#BDB76B")
        Frame_1.place(x=0, y=50, height=10, width=1400)

        show_list = []
        self.enterprise = StringVar()
        self.usability = StringVar()
        self.intercultural = StringVar()
        self.algorithm = StringVar()

        self.name = StringVar()
        self.course = StringVar()
        self.roll = StringVar()

        self.search = StringVar()
        self.ref_no = StringVar()
        self.totals = StringVar()
        self.grade = StringVar()

        #  details frame
        L1 = LabelFrame(self.window,text='Courses', bg="#BDB76B",
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

        lbl_search = Label(L1, text="Ref No.", bg="#BDB76B", font=("arial", 12, "bold"))
        lbl_search.grid(row=0, column=6, padx=20, pady=5)

        ent_search =Entry(L1, width=12, textvariable=self.ref_no, font=("arial", 15, "bold"))
        ent_search.grid(row=0, column=7, pady=5, padx=10)

        # BUTTON
        search_btn = Button(L1, text="Search", command=self.find_bill, bg='#FFE4C4', width=9,
                            font=("arial", 15, "bold"))
        search_btn.grid(row=0, column=8)

        # FRAME
        L2 = LabelFrame(self.window, bg="#BDB76B", fg="black", font=("arial", 15, "bold"))
        L2.place(x=5, y=170, width=440, height=380)

        lbl_enterprise = Label(L2, text="Enterprise", font=("arial", 12, "bold"), bg="#BDB76B", fg="black", )
        lbl_enterprise.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        ent_enterprise = Entry(L2, font=("arial", 12), textvariable=self.enterprise, fg="black", relief=GROOVE)
        ent_enterprise.grid(row=0, column=1, padx=10, pady=10)

        lbl_usability = Label(L2, text="Usability", font=("arial", 12, "bold"), bg="#BDB76B")
        lbl_usability.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        ent_usability = Entry(L2, font=("arial", 12), textvariable=self.usability, fg="black", relief=GROOVE)
        ent_usability.grid(row=1, column=1, padx=10, pady=10)

        lbl_intercultural = Label(L2, text="Intercultural", font=("arial", 12, "bold"), bg="#BDB76B", fg="black")
        lbl_intercultural.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        ent_intercultural = Entry(L2, font=("arial", 12), textvariable=self.intercultural, fg="black", relief=GROOVE)
        ent_intercultural.grid(row=2, column=1, padx=10, pady=10)

        lbl_algorithm = Label(L2, text="Algorithm", font=("arial", 12, "bold"), bg="#BDB76B", fg="black")
        lbl_algorithm.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        ent_algorithm = Entry(L2, font=("arial", 12), fg="black", textvariable=self.algorithm, relief=GROOVE)
        ent_algorithm.grid(row=3, column=1, padx=10, pady=10)

        # bill area
        L3 = LabelFrame(self.window, bg="#BDB76B", fg="black", font=("arial", 15, "bold"))
        L3.place(x=450, y=170, width=840, height=380)

        title = Label(L3, font=("arial", 15, "bold"))
        title.pack(fill=X)
        scroll_y = Scrollbar(L3, orient=VERTICAL)
        self.textarea = Text(L3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # button frame
        L4 = LabelFrame(self.window, bg="#BDB76B", fg="black",
                        font=("arial", 15, "bold"))
        L4.place(x=5, y=570, width=1285, height=100)

        lbl_total = Label(L4, text="Total Marks", bg="#BDB76B", fg="black", font=("arial", 20, "bold"))
        lbl_total.grid(row=0, column=0, pady=1, sticky="w")

        ent_total = Entry(L4, width=18, textvariable=self.totals, state='readonly', font=("arial", 15, "bold"))
        ent_total.grid(row=0, column=1, padx=10, pady=1)

        lbl_grade = Label(L4, text="Grade", bg="#BDB76B", fg="black", font=("arial", 20, "bold"))
        lbl_grade.grid(row=2, column=0, pady=1, sticky="w")

        ent_grade = Entry(L4, width=18, textvariable=self.grade, state='readonly', font=("arial", 15, "bold"))
        ent_grade.grid(row=2, column=1, padx=10, pady=1)

        L5 = Frame(L4, bg="#BDB76B")
        L5.place(x=650, y=0, width=580, height=80)

        tot_btn = Button(L5, text="Total", command=self.total, width=8, bg='#FFE4C4', font=("arial", 15, "bold"))
        tot_btn.grid(row=0, column=0, padx=15, pady=15)

        mark_btn = Button(L5, text="Generate Bill", command=self.particulars, bg='#FFE4C4', width=12,
                          font=("arial", 15, "bold"))
        mark_btn.grid(row=0, column=1, padx=15, pady=15)

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
            self.enterprise_e = int(self.enterprise.get())
            self.usability_u = int(self.usability.get())
            self.intercultural_i = int(self.intercultural.get())
            self.algorithm_a = int(self.algorithm.get())

            self.total_marks = (
                    self.enterprise_e +
                    self.usability_u +
                    self.intercultural_i +
                    self.algorithm_a)

            self.total_tot = self.total_marks
            self.totals.set(self.total_tot)
            self.total_grade = self.total_marks * 0.25
            self.grade.set(str(self.total_grade)+'%')

        except Exception as e:
            print(e)

    def grade_student(self):
        pass

    def welcome(self):
        """welcome:
    It helps to show the student id, course name, student name, and ref no in the text area. """
        try:
            self.textarea.delete('1.0', END)
            self.textarea.insert(
                END, "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSTUDENT`S MARK SHEET")
            self.textarea.insert(END, f"\n Student Id.:{self.roll.get()}")
            self.textarea.insert(END, f"\t\t\t\t\t\tCourse:{self.course.get()}")
            self.textarea.insert(END, f"\n Student Name:{self.name.get()}")
            self.textarea.insert(END, f"\t\t\t\t\t\tRef No.:{self.ref_no.get()}")
            self.textarea.insert(END,
                                 f"\n=====================================================================================================")

            self.textarea.insert(END, f"\n COURSES\t\t\t\t\t\t\t\t\t\t\tMARKS")

            self.textarea.insert(END,
                                 f"\n=====================================================================================================")
        except Exception as e:
            print(e)

    def particulars(self):
        """particulars:
    It helps to get all the entry boxes values in the mark sheet area.
        """
        try:
            if self.name.get() == "" or self.roll.get() == "" or self.course.get() == "" or self.ref_no.get() == '':
                messagebox.showerror("ERROR", "Enter marks Details")

            else:
                self.welcome()
                if self.enterprise.get() != 0:
                    self.textarea.insert(END,
                                         f"\nSTW104KM-Enterprise Information Systems-M20\t\t\t\t\t\t\t\t\t\t\t{self.enterprise_e}")

                if self.usability.get() != 0:
                    self.textarea.insert(END,
                                         f"\nSTW106CR-Designing for Usability-I-M20\t\t\t\t\t\t\t\t\t\t\t{self.usability_u}")

                if self.intercultural.get() != 0:
                    self.textarea.insert(END,
                                         f"\nSTWA101FN-International Cultural Communication Skills-M20\t\t\t\t\t\t\t\t\t\t\t{self.intercultural_i}")

                if self.algorithm.get() != 0:
                    self.textarea.insert(END,
                                         f"\nSTW122COM-Introduction to Algorithms-M20\t\t\t\t\t\t\t\t\t\t\t{self.algorithm_a}")

                ######################
                self.textarea.insert(END,
                                     f"\n=====================================================================================================")

                self.textarea.insert(END, f"\nTotal Marks\t\t\t\t\t\t\t\t\t\t\t{str(self.total_marks)}")
                self.textarea.insert(END, f"\nGrade\t\t\t\t\t\t\t\t\t\t\t{str(self.total_grade)+'%'}")

                self.textarea.insert(END,
                                     f"\n=================================****THANK YOU****===================================================")

                self.save()
        except Exception as e:
            print(e)

    def marksheet(self):
        """save_bill:
    It asks user to save in any location of the computer."""
        try:
            op = messagebox.askyesno("Save Bill", "Do You Want TO Save The Mark sheet?")
            if op > 0:
                self.marksheet_data = self.textarea.get('1.0', END)
                f = open("bills/" + ".ent", "w")
                f.write(self.marksheet_data)
                f.close()
                messagebox.showinfo("Success", f"\nStudent Mark sheet has been saved successfully")
            else:
                return False
        except Exception as e:
            print(e)

    def find_bill(self):
        """
    This function helps to find the mark sheet of the student."""
        try:
            present = "no"
            for i in os.listdir("Mark sheet/"):
                if i.split('.')[0] == self.ref_no.get():
                    f = open(f"Mark sheet/{i}", "r")
                    self.textarea.delete("1.0", END)
                    for d in f:
                        self.textarea.insert(END, d)
                    f.close()
                    present = "yes"
            if present == "no":
                messagebox.showerror("Error", "Mark Sheet Not Found!")
        except Exception as e:
            print(e)

    def clear_ent(self):
        """clear_ent:
    It clears all the entry boxes and text area."""
        try:
            op = messagebox.askyesno("Clear", "Do you want to clear data?")
            if op > 0:
                self.algorithm.set(0)
                self.usability.set(0)
                self.intercultural.set(0)
                self.enterprise.set(0)

                self.name.set("")
                self.roll.set('')

                self.course.set('')
                self.search.set("")

                self.totals.set("")

                self.welcome()
        except Exception as e:
            print(e)

    def save(self):
        """save_mark sheet:
    It asks user to save in any location of the computer."""
        try:
            op = messagebox.askyesno("Save Mark Sheet", "Do You Want TO Save The mark sheet?")
            if op > 0:
                self.bill_data = self.textarea.get('1.0', END)
                f = open("Mark sheet/" + str(self.ref_no.get()) + ".ent", "w")
                f.write(self.bill_data)
                f.close()
                messagebox.showinfo("Success", f"\nYour bill {self.ref_no.get()} has been saved successfully")
            else:
                return False
        except Exception as e:
            print(e)

    def close(self):
        """close:
    It closes the this window.
    """

        try:
            ob = messagebox.askyesno("Exit", "Do you want to exit?")
            if ob > 0:
                self.window.destroy()
        except Exception as e:
            print(e)


# student_mark_sheet()
