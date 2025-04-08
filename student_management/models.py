class Student:
    def __init__(self, id=None, name=None, age=None, grade=None):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade
    
    def __str__(self):
        return f"학생 ID: {self.id}, 이름: {self.name}, 나이: {self.age}, 학년: {self.grade}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'grade': self.grade
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            age=data.get('age'),
            grade=data.get('grade')
        ) 