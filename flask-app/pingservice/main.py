import re
import json
import requests
from flask import Flask, request
from flask_restx  import fields, Resource, Api

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
    
# Post api that pings any rest api url and returns json output
@api.route('/api/v1/ping', methods=['POST'])
class Ping(Resource):
    @api.expect(ping_params)
    def post(self):
        status = None
        try:
            url = request.json.get('url')
        except:
            response_data = json.loads(request.json)
            url = response_data.get('url')
        if is_valid_url(url):
            try:
                r = requests.get(url)
                status = r.status_code
                response_data = json.loads(r.text)

            except:
                response_data = r.text 
        return {'url_received': url, 'status': status,
                'response': response_data}

# Get api that returns json output {"Receiver": "Cisco is the best!"}
@api.route('/api/v1/info', methods=['GET'])
class InfoCheck(Resource):
    def get(self):
        return { "Receiver": "Cisco is the best!" }

# Get api that checks docker health status
@api.route('/health', methods=['GET'])
class Health(Resource):
    def get(self):
        return { 'success': True, 'message': "healthy" }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')