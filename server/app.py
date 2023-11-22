from models import Teacher, Student
from flask_restful import Resource, reqparse
from config import app, db



if __name__ == '__main__':
    app.run(port=5555, debug=True)