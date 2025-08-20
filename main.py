class Student:
    def __init__(self, username, phone, email, password):
        self.username = username
        self.phone = phone
        self.email = email
        self.password = password
        self.is_student = True
        self.is_teacher = False
        self.is_admin = False
        self.homeworks = []  # o'qituvchi bergan uyga vazifalar
        self.grades = {}     # fan nomi: baho




class Teacher:
    def __init__(self, username, phone, email, password):
        self.username = username
        self.phone = phone
        self.email = email
        self.password = password
        self.is_student = False
        self.is_teacher = True
        self.is_admin = False
        self.students = []  # o'z guruhidagi o'quvchilar



class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_student = False
        self.is_teacher = False
        self.is_admin = True
