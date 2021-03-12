import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk, filedialog
import pandas

import Marksheet
import bills
import query
import sorting



class Student:
    def __init__(self, window):
        self.window = window
        self.window.title("Student Management System")
        self.window.geometry('1350x780+100+0')
        self.window.config(bg='#BDB76B')
        self.window.resizable(False, False)

        title = Label(self.window, text='Student Management System', relief=GROOVE, font=('arial', 40, 'bold'),
                      bg='#BDB76B', fg='black')
        title.pack(side=TOP, fill=X)

        self.Roll_No = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.dob = StringVar()
        self.address = StringVar()
        self.search_by = StringVar()
        self.ent_search = StringVar()

        # Manage Frame
        Manage_Frame = Frame(self.window, bd=4, relief=RIDGE, bg='#BDB76B')
        Manage_Frame.place(x=20, y=100, width=450, height=680)

        m_title = Label(Manage_Frame, text='Students Details', bg='#BDB76B', fg='black', font=('arial', 20, 'bold'))
        m_title.grid(row=0, column=1, columnspan=2, pady=20)

        lbl_roll = Label(Manage_Frame, text='Roll No.', bg='#BDB76B', fg='black', font=('arial', 20, 'bold'))
        lbl_roll.grid(row=1, column=0, pady=20, padx=10, sticky=W)

        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No, font=('arial', 15, 'bold'), bd=5, relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=20, padx=10, sticky=W)

        lbl_name = Label(Manage_Frame, text='Name', bg='#BDB76B', fg='black', font=('arial', 20, 'bold'))
        lbl_name.grid(row=2, column=0, pady=20, padx=10, sticky=W)

        txt_name = Entry(Manage_Frame, textvariable=self.name, font=('arial', 15, 'bold'), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=20, padx=10, sticky=W)

        lbl_DOB = Label(Manage_Frame, text='D.O.B', bg='#BDB76B', fg='black', font=('arial', 20, 'bold'))
        lbl_DOB.grid(row=3, column=0, pady=20, padx=10, sticky=W)

        txt_DOB = Entry(Manage_Frame, textvariable=self.dob, font=('arial', 15, 'bold'), bd=5, relief=GROOVE)
        txt_DOB.grid(row=3, column=1, pady=20, padx=10, sticky=W)

        lbl_Gender = Label(Manage_Frame, text='Gender', bg='#BDB76B', fg='black', font=('arial', 20, 'bold'))
        lbl_Gender.grid(row=4, column=0, pady=20, padx=10, sticky=W)

        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender, font=('times new roman', 14, 'bold'),
                                    state='readonly')
        combo_gender['values'] = ('Male', 'Female', 'Other')
        combo_gender.grid(row=4, column=1, padx=10, pady=20)

        lbl_Contact = Label(Manage_Frame, text='Contact', bg='#BDB76B', fg='black', font=('arial', 20, 'bold'))
        lbl_Contact.grid(row=5, column=0, pady=20, padx=10, sticky=W)

        txt_Contact = Entry(Manage_Frame, textvariable=self.contact, font=('arial', 15, 'bold'), bd=5,
                            relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=20, padx=10, sticky=W)

        lbl_email = Label(Manage_Frame, text='Email', bg='#BDB76B', fg='black', font=('arial', 20, 'bold'))
        lbl_email.grid(row=6, column=0, pady=20, padx=10, sticky=W)

        txt_email = Entry(Manage_Frame, textvariable=self.email, font=('arial', 15, 'bold'), bd=5, relief=GROOVE)
        txt_email.grid(row=6, column=1, pady=20, padx=10, sticky=W)

        lbl_address = Label(Manage_Frame, text='Address', bg='#BDB76B', fg='black', font=('arial', 20, 'bold'))
        lbl_address.grid(row=7, column=0, pady=20, padx=10, sticky=W)

        lbl_Address = Entry(Manage_Frame, textvariable=self.address, font=('arial', 15, 'bold'), bd=5,
                            relief=GROOVE)
        lbl_Address.grid(row=7, column=1, pady=20, padx=10, sticky=W)
        # buttons
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg='#BDB76B')
        btn_Frame.place(x=10, y=610, width=430)

        self.Add_btn = Button(btn_Frame, bg='#FFE4C4', text='Add', width=8,
                              command=self.add_student).grid(row=0, column=0, padx=10, pady=10)
        self.Update_btn = Button(btn_Frame, bg='#FFE4C4', text='Update', width=8,
                                 command=self.update_data).grid(row=0, column=1, padx=10, pady=10)

        self.Delete_btn = Button(btn_Frame, bg='#FFE4C4', text='Delete', width=8,
                                 command=self.delete__student_data).grid(row=0, column=2, padx=10, pady=10)

        self.Clear_btn = Button(btn_Frame, bg='#FFE4C4', text='Clear', width=8,
                                command=self.clear_datas).grid(row=0, column=3, padx=10, pady=10)

        self.Close_btn = Button(btn_Frame, bg='#FFE4C4', text='Close', width=8, command=self.close).grid(row=0,
                                                                                                         column=4,
                                                                                                         padx=10,
                                                                                                         pady=10)

        # detail  Frame
        Detail_Frame = Frame(self.window, bd=4, relief=RIDGE, bg='#BDB76B')
        Detail_Frame.place(x=500, y=100, width=800, height=680)

        lbl_Search = Label(Detail_Frame, text='Search By', bg='#BDB76B', fg='black', font=('arial', 20, 'bold'))
        lbl_Search.grid(row=0, column=0, pady=10, padx=20, sticky=W)

        combo_search = ttk.Combobox(Detail_Frame, width=10, textvariable=self.search_by,
                                    font=('times new roman', 13, 'bold'), state='readonly')
        combo_search['values'] = ('Roll_no', 'Name', 'Contact', 'Gender')
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_Search = Entry(Detail_Frame, width=20, textvariable=self.ent_search, font=('arial', 10, 'bold'), bd=5,
                           relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=20, padx=10, sticky=W)

        self.search_btn = Button(Detail_Frame, bg='#FFE4C4', text='Search', width=10,
                                 command=self.search_data_student, pady=5).grid(row=0, column=3, padx=10, pady=10)

        self.show_all_btn = Button(Detail_Frame, bg='#FFE4C4', text='Show All', width=10, pady=5,
                                   command=self.fetch).grid(row=0, column=4, padx=10, pady=10)

        self.reset_btn = Button(Detail_Frame, bg='#FFE4C4', text='Reset', width=10, pady=5,
                                command=self.reset).grid(row=0, column=5, pady=10)

        self.export_btn = Button(Detail_Frame, bg='#FFE4C4', text='Export', font=('arial', 10, 'bold'),
                                 command=self.export_student
                                 ).place(x=10, y=620, width=240)
        self.mark_btn = Button(Detail_Frame, bg='#FFE4C4', text='Mark sheet', font=('arial', 10, 'bold'),
                                 command=self.marksheet
                                 ).place(x=270, y=620, width=240)

        self.bill_btn = Button(window, bg='#FFE4C4', text='Student Bill', font=('arial', 10, 'bold'),
                               command=self.student_bill
                               ).place(x=1035, y=725, width=240)

        # table frame
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg='black')
        Table_Frame.place(x=10, y=70, width=760, height=550)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,
                                          columns=('roll', 'name', 'email', 'gender', 'contact', 'dob', 'Address'),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading('roll', text='Roll No.')
        self.Student_table.heading('name', text='Name')
        self.Student_table.heading('email', text='Email')
        self.Student_table.heading('gender', text='Gender')
        self.Student_table.heading('contact', text='Contact')
        self.Student_table.heading('dob', text='D.O.B')
        self.Student_table.heading('Address', text='Address')
        self.Student_table['show'] = 'headings'
        self.Student_table.column('roll', width=50)
        self.Student_table.column('name', width=100)
        self.Student_table.column('email', width=200)
        self.Student_table.column('gender', width=80)
        self.Student_table.column('contact', width=100)
        self.Student_table.column('dob', width=90)
        self.Student_table.column('Address', width=150)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind('<ButtonRelease-1>', self.cursor)

        self.fetch()
        self.window.mainloop()

    def add_student(self):
        """add_student:
    It helps to add students data."""
        try:
            if self.Roll_No.get() != '' and self.name.get() != '' and self.email.get() != '' and \
                    self.gender.get() != '' and self.contact.get() != '' and self.dob.get() != '' and self.address.get() != '':
                if query.student().add_students(self.Roll_No.get(), self.name.get(),
                                                self.email.get(), self.gender.get(),
                                                self.contact.get(), self.dob.get(),
                                                self.address.get()):
                    messagebox.showinfo('Success', 'Student Details Added')
                    self.fetch()
                    self.clearing()

            else:
                tkinter.messagebox.showerror('Empty', 'Please fill out all the boxes.')
        except Exception as e:
            print(e)
            return False

    print(
        "----------------------------------------------Functions of sms window---------------------------------------")
    print(add_student.__doc__)

    def update_data(self):
        """update_student:
    It helps to update students data."""
        try:
            if self.Roll_No.get() != '' and self.name.get() != '' and self.email.get() != '' and \
                    self.gender.get() != '' and self.contact.get() != '' and self.dob.get() != '' and self.address.get() != '':

                if query.student().update_details(self.name.get(), self.email.get(),
                                                  self.gender.get(), self.contact.get(),
                                                  self.dob.get(), self.address.get(),
                                                  self.Roll_No.get()):
                    messagebox.showinfo('Success', 'Updated Successfully')

                self.fetch()
                self.clearing()
            else:
                tkinter.messagebox.showerror('Empty', 'Please fill out all the boxes.')
        except Exception as e:
            print(e)

    print(update_data.__doc__)

    def fetch(self):
        """fetch:
    It helps to fetch all the students data from database"""
        try:
            self.Student_table.delete(*self.Student_table.get_children())
            data = sorting.sorting_data(query.student().fetch_student())
            for i in data:
                self.Student_table.insert("", "end", text=i[0], value=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        except Exception as e:
            print(e)

    print(fetch.__doc__)

    def clearing(self):
        """clearing:
    It helps to clear all the entry boxes after adding or updating or deleting data."""
        try:
            if self.Roll_No.get() != '' and self.name.get() != '' and self.email.get() != '' and \
                    self.gender.get() != '' and self.contact.get() != '' and self.dob.get() != '' and self.address.get() != '':
                self.Roll_No.set('')
                self.name.set('')
                self.email.set('')
                self.gender.set('')
                self.contact.set('')
                self.dob.set('')
                self.address.set('')
            else:
                return False
        except Exception as e:
            print(e)

    print(clearing.__doc__)

    def clear_datas(self):
        """clear_datas:
    It helps to clear all the entry boxes."""
        try:
            if self.Roll_No.get() != '' and self.name.get() != '' and self.email.get() != '' and \
                    self.gender.get() != '' and self.contact.get() != '' and self.dob.get() != '' and self.address.get() != '':
                self.Roll_No.set('')
                self.name.set('')
                self.email.set('')
                self.gender.set('')
                self.contact.set('')
                self.dob.set('')
                self.address.set('')
            else:
                tkinter.messagebox.showwarning('Fill something', 'Fill Something To Clear.')
        except Exception as e:
            print(e)

    print(clear_datas.__doc__)

    def cursor(self, event):
        """cursor:
    It helps retrieve data from tree view one row at a time """
        try:
            cursor_row = self.Student_table.focus()
            content = self.Student_table.item(cursor_row)
            row = content['values']
            self.Roll_No.set(row[0])
            self.name.set(row[1])
            self.email.set(row[2])
            self.gender.set(row[3])
            self.contact.set(row[4])
            self.dob.set(row[5])
            self.address.set(row[6])
            return True
        except Exception as e:
            print(e)
            return False

    print(cursor.__doc__)

    def delete__student_data(self):
        """delete_student:
    It helps to delete student data"""
        try:
            if self.Roll_No.get() != '' and self.name.get() != '' and self.email.get() != '' and \
                    self.gender.get() != '' and self.contact.get() != '' and self.dob.get() != '' and self.address.get() != '':
                query.student().delete_student(self.Roll_No.get())
                messagebox.showinfo('Success', 'Deleted Successfully')
                self.clearing()
                self.fetch()
            else:
                messagebox.showerror('Error', 'Select The Details First')
        except Exception as e:
            print(e)

    print(delete__student_data.__doc__)

    def search_data_student(self):
        """search_data:
    It helps to search student """
        try:
            if self.ent_search.get() != '':
                da = query.student().search(self.search_by.get(), self.ent_search.get())
                if len(da) != 0:
                    self.Student_table.delete(*self.Student_table.get_children())
                    for row in da:
                        self.Student_table.insert('', END, values=row)
                else:
                    messagebox.showinfo('Not Found', 'Put Student Details Correctly')
            else:
                tkinter.messagebox.showwarning('Empty', 'It  Cannot Be Empty')
        except Exception as e:
            print(e)

    print(search_data_student.__doc__)

    def close(self):
        """close:
    It exits the sms window"""
        try:
            ob = messagebox.askyesno("Close", "Do You Want To Exit The Application?")
            if ob > 0:
                self.window.destroy()
                return True
        except Exception as e:
            print(e)

    print(close.__doc__)

    def reset(self):
        """reset:
    It helps to reset the tree view"""
        self.Student_table.delete(*self.Student_table.get_children())

    print(reset.__doc__)

    def export_student(self):
        """export_student:
    It helps to export all the data of student from the tree view into excel."""
        try:
            ob = messagebox.askyesno("Save", "Do you want to Save?")
            if ob > 0:
                ff = filedialog.asksaveasfilename()
                gg = self.Student_table.get_children()
                roll, name, email, gender, contact, dob, Address = [], [], [], [], [], [], []
                for i in gg:
                    content = self.Student_table.item(i)
                    pp = content['values']
                    roll.append(pp[0]), name.append(pp[1]), email.append(pp[2]), gender.append(pp[3]), contact.append(
                        pp[5]), dob.append(pp[4]), Address.append(pp[6])
                dd = ['Roll No.', 'Name', 'Email', 'Gender', 'Contact', 'D.O.B', 'Address']
                df = pandas.DataFrame(list(zip(roll, name, email, gender, dob, contact, Address)), columns=dd)
                paths = r'{}.csv'.format(ff)
                df.to_csv(paths, index=False)
                messagebox.showinfo('Saved', 'Student Data Is Saved '.format(paths))
            else:
                return False
        except Exception as e:
            print(e)

    print(export_student.__doc__)

    def student_bill(self):
        """student_bill:
    It takes user to bills window.
        """

        try:
            ob = messagebox.askyesno("Bill", "Do You Want TO  Go To Student Bill?")
            if ob > 0:
                self.window.destroy()
                bills.bill()
            else:
                return True
        except Exception as e:
            print(e)

    print(student_bill.__doc__)

    def marksheet(self):
        """student_bill:
           It takes user to bills window.
               """

        try:
            ob = messagebox.askyesno("Mark sheet", "Do You Want TO  Go To Student mark sheet?")
            if ob > 0:
                self.window.destroy()
                Marksheet.student_mark_sheet()
            else:
                return True
        except Exception as e:
            print(e)

    print(marksheet.__doc__)


# root = Tk()
# iv = Student(root)
