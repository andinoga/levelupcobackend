from flask_sqlalchemy import SQLAlchemy
  
db = SQLAlchemy()

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    #ONE TO MANY RELATIONSHIP
    students = db.relationship("Students")

    def __repr__(self):
        return 'Student: %s' % self.students
        
    def to_dict(self):
        students = []
        for s in self.students:
            students.append(u.to_dict())
        return { 
          "id": self.id, 
          "name": self.name,
          "students": users
        }

#students
class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'))
    grades = db.relationship("Grades")
  
    def __repr__(self):
        return 'Contact: %s' % self.full_name
  
    def to_dict(self):
        groups = []
        for g in self.groups:
            groups.append(g.not_dict())
        return { 
          "id": self.id, 
          "name": self.name,
          "age": self.age,
          "email": self.email,
          "lesson_id": self.lesson_id,
          "grades": self.grades
        }
        
    def not_dict(self):
        groups = []
        for g in self.groups:
            groups.append(g.id)
        return { 
          "id": self.id, 
          "name": self.name,
          "age": self.age,
          "email": self.email,
          "lesson_id": self.lesson_id,
          "grades": self.grades
        }
        
#lessons
class Lessons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    students = db.relationship("Students")
    grades = db.relationship("Grades")
    reading_lessons = db.Column(db.Integer, db.ForeignKey('reading_lessons.id'))
    math_lessons = db.Column(db.Integer, db.ForeignKey('math_lessons.id'))
    
    def __repr__(self):
        return 'Lesson: %s' % (self.name)
  
    def to_dict(self):
        students = []
        for s in self.students:
            students.append(s.to_dict())
        return { 
          "id": self.id, 
          "name": self.name, 
          "students": students 
        }


#grades
class Grades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    students = db.relationship("Students")
    reading_lessons = db.Column(db.Integer,db.ForeignKey('reading_lessons.id'))
    math_lessons = db.Column(db.Integer,db.ForeignKey('math_lessons.id'))
    
    def __repr__(self):
        return 'Grades: %s' % (self.name)
        
    def to_dict(self):
        grades = []
        for g in self.grades:
            grades.append(g.to_dict())
        return { 
          "id": self.id, 
          "reading_lessons": self.reading_lessons, 
          "math_lessons": self.math_lessons 
        }
    def not_dict(self):
        grades = []
        for g in self.grades:
            grades.append(g.not_dict())
        return { 
          "id": self.id, 
          "reading_lessons": self.reading_lessons,
          "math_lessons": self.math_lessons 
        }
    
