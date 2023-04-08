from app import db


class Lessons(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    teacher =  db.Column(db.String(150), nullable = False)
    
    students = db.relationship('Students', backref='lesson_ref', lazy=True)