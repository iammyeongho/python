import json
from models import Student

class Database:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = {}
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.students = {
                    int(id): Student.from_dict(student_data)
                    for id, student_data in data.items()
                }
        except FileNotFoundError:
            self.students = {}
    
    def save_data(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            data = {
                str(id): student.to_dict()
                for id, student in self.students.items()
            }
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def create_student(self, name, age, grade):
        # 새로운 ID 생성
        new_id = max(self.students.keys(), default=0) + 1
        student = Student(id=new_id, name=name, age=age, grade=grade)
        self.students[new_id] = student
        self.save_data()
        return student
    
    def get_student(self, student_id):
        return self.students.get(student_id)
    
    def get_all_students(self):
        return list(self.students.values())
    
    def update_student(self, student_id, name=None, age=None, grade=None):
        student = self.students.get(student_id)
        if student:
            if name is not None:
                student.name = name
            if age is not None:
                student.age = age
            if grade is not None:
                student.grade = grade
            self.save_data()
            return student
        return None
    
    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            self.save_data()
            return True
        return False 