from models import Teacher, Student
from flask_restful import Resource, reqparse
from config import app, db, api


class Teachers(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return {"message": "No input data provided"}, 400
        try:
            new_teacher = Teacher(name=name, age=age)
        except ValueError as e:
            return {"message": f"Error creating teacher: {e}"}, 400

        db.session.add(new_teacher)
        db.session.commit()

        return new_teacher.to_dict(), 201


api.add_resource(Teachers, '/teacher')


if __name__ == '__main__':
    app.run(port=5555, debug=True)