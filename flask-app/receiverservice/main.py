import re
import json
import requests
from flask import Flask, request
from flask_restx  import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/api/v1/info', methods=['GET'])
class InfoCheck(Resource):
    def get(self):
        return { "Receiver": "Cisco is the best!" }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')