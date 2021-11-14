from django.http import JsonResponse
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import coreapi, json, requests

def index(request):
    
    example = {
        "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
        "category": "page interaction",
        "name": "pageview",
        "data": {
            "host": "www.consumeraffairs.com",
            "path": "/",
        },
        "timestamp": "2021-01-01 09:15:27.243860"
    }
    response = {
        'Event' : {
            'Actions': {
                'GET': {
                    'Detail': 'GET http://127.0.0.1:8000/client/events/id',
                    'List': 'GET http://127.0.0.1:8000/client/events/',
                    'Query params': {
                        'Options': ['session_id', 'category', 'timeframe_init', 'timeframe_end'],
                        'Examples': {
                            'session_id': 'e2085be5-9137-4e4e-80b5-f1ffddc25424',
                            'category': 'page interaction',
                            'timeframe_init': '2020-01-01',
                            'timeframe_end': '2021-01-01T09:15:27.243860-04:00'
                        }
                    }
                },
                'POST': {
                    'Disclaimer': "Make sure you've created a user with username admin and password admin before testing",
                    'Create': 'POST http://127.0.0.1:8000/client/events/',
                    'Body Example': example
                },
                'Authentication': {
                    'Auth Type': 'Basic Auth',
                    'Example': {
                        'username': 'admin',
                        'password': 'admin'
                    }
                }
            }
        }
    }
    return JsonResponse(response)

def detail_event(request, pk):
    client = coreapi.Client()
    response = client.get(f'http://127.0.0.1:8000/api/events/{pk}')    

    return JsonResponse(response)

@csrf_exempt
def events(request):
    if request.method == 'GET':
        client = coreapi.Client()
        response = client.get('http://127.0.0.1:8000/api/events/')

    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        response = requests.post('http://127.0.0.1:8000/api/events/', json=body, auth=('admin', 'admin'))
        
        if response.status_code is '201':
            return JsonResponse(body)
        
        return JsonResponse({'Error': 'Did you forget to create the user?'})

