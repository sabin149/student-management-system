from cs19b.newproject.Connection import My_Db


class student(My_Db):
    def __init__(self):
        super().__init__()

    def sign_in(self, username, password):
        try:
            qry = "select * from users where username=%s and password=%s"
            values = (username, password)
            self.my_cursor.execute(qry, values)
            data = self.my_cursor.fetchone()
            self.my_connection.close()
            return data
        except Exception as e:
            print(e)

    def sign_up(self, username, password, name, address, phone, email):
        try:
            qry = "INSERT INTO users (username,password,name,address,phone,email)" \
                  " VALUES (%s,%s,%s,%s,%s,%s)"
            values = (username, password, name, address, phone, email)
            self.my_cursor.execute(qry, values)
            self.my_connection.commit()
            return True
        except Exception as e:
            print(e)

    def add_students(self, roll_no, name, email, gender, contact, dob, address):
        try:
            qry = "INSERT INTO students (roll_no, name, email, gender, contact, dob, address)" \
                  " VALUES (%s,%s,%s,%s,%s,%s,%s)"
            values = (roll_no, name, email, gender, contact, dob, address)
            self.my_cursor.execute(qry, values)
            self.my_connection.commit()
            return True
        except Exception as e:
            print(e)

    def update_details(self, name, email, gender, contact, dob, address, roll_no):
        try:
            qry = "Update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s"
            values = (name, email, gender, contact, dob, address, roll_no)
            self.my_cursor.execute(qry, values)
            self.my_connection.commit()
            return True
        except Exception as e:
            print(e)

    def fetch_student(self):
        try:
            qry = 'select * from students order by name'
            self.my_cursor.execute(qry)
            data = self.my_cursor.fetchall()
            self.my_connection.close()
            return data
        except Exception as e:
            print(e)

    def delete_student(self, roll_no):
        try:
            qry = 'delete from students where roll_no=%s'
            values = (roll_no,)
            self.my_cursor.execute(qry, values)
            self.my_connection.commit()
            self.my_connection.close()
            return True
        except Exception as e:
            print(e)

    def search(self, search_by, search):
        try:
            qry = ("select * from students where " + search_by + "  like '" + search + "%' ")
            self.my_cursor.execute(qry)
            self.my_connection.close()
            data = self.my_cursor.fetchall()
            return data
        except Exception as e:
            print(e)


s = student()
