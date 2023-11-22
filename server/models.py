from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from config import db

class Student(db.Model, SerializerMixin):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    teacher_id = db.Column(db.Integer, db.ForiegnKey('teacher.id'))
    teacher = db.relationship('Teacher', back_populates="student")


class Teacher(db.Model, SerializerMixin):
    __tablename__ = 'teacher'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    student = db.relationship('Student', back_populates="teacher")
