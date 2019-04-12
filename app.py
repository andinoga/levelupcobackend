import os
import sqlalchemy
from models import db, Students, Lessons, Grades
from flask_migrate import Migrate
from flask import Flask, jsonify, request
from sqlalchemy import desc 
  
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/levelup.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


#endpoints
@app.route('/', methods=['GET'])
def test(): 
    return ("TEST")
    
#signup
@app.route('/signup', methods=['GET'])
def boo(): 
    return("Signup")
    
#forgotpassword
@app.route('/forgotpassword', methods=['GET'])
def square(): 
    return("Forgot_password")    
    
@app.route('/')
def list():
    students = Students.query.all()
    response = []
    for s in students:
        response.append("%s" % i)
    
    return jsonify(response)    
    
    
@app.route('/Lessons')
def less():
    lessons = Lessons.query.all()
    response = []
    for l in lessons:
        lesson = l.to_dict()
        response.append(course)
    
    return jsonify({"data": response})
    
    
@app.route('/allLessons')
def all():
    lessons = Lessons.query.all()
    response = []
    for s in lessons:
        response.append("%s" % i)
    
    return jsonify(response)        
    
@app.route('/Grades')
def grad():
    grades = Grades.query.all()
    response = []
    for g in grades:
        grade = g.to_dict()
        response.append(grades)
    
    return jsonify({"data": response})
    
@app.route('/allGrades')
def too():
    lessons = Lessons.query.all()
    response = []
    for s in lessons:
        response.append("%s" % i)
    
    return jsonify(response)     

  
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
