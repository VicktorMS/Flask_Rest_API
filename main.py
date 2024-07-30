from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser() # serve para definir argumentos obrigatórios para serem enviados
video_put_args.add_argument(
    'title', type=str, # tipo de argumento
    help='Title of the video is required', # um espécie de mensagem de erro
)
video_put_args.add_argument(
    'views', type=int, default=0
)
video_put_args.add_argument(
    'likes', type=int, default=0
)

videos = {}


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        return {video_id: args}
        

api.add_resource(Video, '/video/<int:video_id>')



if __name__ == '__main__':
    app.run(debug=True)