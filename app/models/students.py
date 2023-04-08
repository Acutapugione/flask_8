from app import db


class Students(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=True)
 