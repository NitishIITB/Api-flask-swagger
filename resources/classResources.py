from flask_restful import Resource, reqparse

# Mock data store
courses = []
parser = reqparse.RequestParser()
parser.add_argument("title", type=str, required=True, help="Title cannot be blank")
parser.add_argument("description", type=str, required=True, help="Description cannot be blank")


class ClassResource(Resource):
    def get(self):
        """Get all courses"""
        return {"courses": courses}, 200

    def post(self):
        """Create a new course"""
        args = parser.parse_args()
        course_id = len(courses) + 1
        course = {
            "id": course_id,
            "title": args["title"],
            "description": args["description"]
        }
        courses.append(course)
        return course, 201


class SingleClassResource(Resource):
    def get(self, id):
        """Get course by ID"""
        course = next((course for course in courses if course["id"] == id), None)
        if not course:
            return {"message": "Course not found"}, 404
        return course, 200

    def put(self, id):
        """Update a course by ID"""
        course = next((course for course in courses if course["id"] == id), None)
        if not course:
            return {"message": "Course not found"}, 404

        args = parser.parse_args()
        course["title"] = args["title"]
        course["description"] = args["description"]
        return course, 200

    def delete(self, id):
        """Delete a course by ID"""
        global courses
        courses = [course for course in courses if course["id"] != id]
        return {"message": "Course deleted"}, 204
