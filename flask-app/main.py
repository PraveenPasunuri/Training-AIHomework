import re
import json
import requests
from flask import Flask, request
from flask_restx  import fields, Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

ping_params = api.model(
    "params",
    {
        "url": fields.String(description="cust ID", required=True),
    },
)

def is_valid_url(url):
    # print(re.match(regex, "http://www.example.com") is not None) # True
    # print(re.match(regex, "example.com") is not None)            # False
    regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None
    


@api.route('/api/v1/ping', methods=['POST'])
class Ping(Resource):
    @api.expect(ping_params)
    def post(self):
        url = request.json.get('url')
        status = None
        if is_valid_url(url):
            try:
                r = requests.get(url)
                status = r.status_code
                response_data = json.loads(r.text)

            except:
                response_data = r.text 
        return {'url_received': url, 'status': status,
                'response': response_data}


@api.route('/api/v1/info', methods=['GET'])
class InfoCheck(Resource):
    def get(self):
        return { "Receiver": "Cisco is the best!" }


@api.route('/health', methods=['GET'])
class Health(Resource):
    def get(self):
        return { 'success': True, 'message': "healthy" }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')