from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

people = {
    'Victor': {
        'age': 20,
        'gender': 'male'
    },
    'Ana Luisa': {
        'age': 21,
        'gender': 'female'
    }
}


class HelloWorld(Resource):
    def get(self, name):
        return {name: people[name]}

    def post(self):
        return {"message": "Hello World"}


api.add_resource(HelloWorld, "/hello-world/<string:name>")

if __name__ == '__main__':
    app.run(debug=True)