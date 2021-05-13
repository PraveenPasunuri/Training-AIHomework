import requests
import json

def pretty_print_request(request):
    print( '\n{}\n{}\n\n{}\n\n{}\n'.format(
        '-----------Request----------->',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
        request.body)
    )

def pretty_print_response(response):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        response.text)
    )         
    
def test_post_headers_body_json():
    url = 'http://localhost:8080/api/v1/ping'
    
    # Additional headers.
    headers = {'Content-Type': 'application/json' } 

    # Body
    payload = {"url": "http://localhost:8080/api/v1/info"}
    
    # convert dict to json by json.dumps() for body data. 
    resp = requests.post(url, headers=headers, data=json.dumps(payload,indent=4))       
    print("resp.status_code", resp.status_code)
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body.get('response') == {'Receiver': 'Cisco is the best!'}
    
    # print full request and response
    pretty_print_request(resp.request)
    pretty_print_response(resp)
     