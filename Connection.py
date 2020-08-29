import mysql.connector


class My_Db:
    def __init__(self):
        self.my_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='stm')

        self.my_cursor = self.my_connection.cursor()
