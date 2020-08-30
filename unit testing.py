import unittest
from cs19b.newproject.stm_query import student


class MyTest(unittest.TestCase):

    def test_add_student(self):
        a = student()
        actual_result = a.add_students('119', 'ram rai', 'ram@gmail.com', 'Male', '87885555', '2019/02/07', 'ktm')
        self.assertTrue(actual_result)

    def test_update_student(self):
        b = student()
        actual_result = b.update_details('Sam rai', 'ram@gmail.com', 'Male', '87885555', '2019/02/07', 'ktm', '119')
        self.assertTrue(actual_result)

    def test_fetch_student(self):
        c = student()
        actual_result = c.fetch_student()
        self.assertTrue(actual_result)

    def test_login(self):
        d = student()
        actual_result = d.sign_in('q', 'q')
        self.assertTrue(actual_result)

    def test_register(self):
        e = student()
        actual_result = e.sign_up('r', 'r', 'r', 'ktm', '9874857825', 'ihfwqh@gmail.com')
        self.assertTrue(actual_result)

    def test_delete(self):
        e = student()
        actual_result = e.delete_student('roll_no')
        self.assertTrue(actual_result)


