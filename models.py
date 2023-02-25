from flask import Flask,render_template,redirect,jsonify,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
def setupDb():
    db.drop_all()
    db.create_all()
    

class Question(db.Model):
    __tablename__ = "Question"

    id = db.Column(db.Integer,primary_key=True)
    type = db.Column(db.String(),nullable=False)
    question = db.Column(db.String(),nullable=False)
    answers = db.Column(db.String(),nullable=False)
    correct_answer = db.Column(db.String(),nullable=False)
    # [{'1':'Answer 1','2':'Answer 2'}]

    def __init__(self,question,type,answers,correct_answer):
        self.question = question
        self.type = type
        self.answers = answers
        self.correct_answer = correct_answer
        
    def question_format(self):
        return {"id":self.id,"question":self.question,"answers":self.answers,"correct_answer":self.correct_answer}

    def add(self):
        db.session.add(self)
        db.session.commit()
    """
        What type of game is this?


    """
    

