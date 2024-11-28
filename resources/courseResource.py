from flask_restful import Resource
from flask import request
import json

# Sample data for courses
courses = [
    {"id": 1, "title": "Mathematics", "professor": "Preeti Singh", "credit": 3},
    {"id": 2, "title": "Physics", "professor": "Preeti Singh", "credit": 4}
]

class CoursesGETResource(Resource):
    def get(self):
        return courses

class CourseGETResource(Resource):
    def get(self, id):
        for course in courses:
            if course["id"] == id:
                return course
        return None

class CoursePOSTResource(Resource):
    def post(self):
        course = json.loads(request.data)
        new_id = max(course["id"] for course in courses) + 1
        course["id"] = new_id
        courses.append(course)
        return course

class CoursePUTResource(Resource):
    def put(self, id):
        course = json.loads(request.data)
        for _course in courses:
            if _course["id"] == id:
                _course.update(course)
                return _course

class CourseDELETEResource(Resource):
    def delete(self, id):
        global courses
        courses = [course for course in courses if course["id"] != id]
        return "", 204
