# from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
import requests
# import simplejson as json
import json

auth_id = "MAY2E3MTFIZGJMYZMXNT"
auth_token = "YTMwYTBlMjlkNDIwOTIxOGMzMjU4YWJmY2I2YzU0"
url = 'https://api.plivo.com'.rstrip('/') + '/' + 'v1'
api = url + '/Account/%s' % auth_id


@csrf_protect
@csrf_exempt
def sample_sender(request):
	response = {}
	
	src_no = request.POST['src']
	dst_no = request.POST['dst']
	msg = request.POST['msg']
	s_url = request.POST['s_url']
	headers = {'content-type': 'application/json'}
	# import pdb;pdb.set_trace()

	params = {
    'src': src_no,
    'dst' : dst_no,
    'text' : msg,
    'url' : s_url
	}
	headers.update(headers)
	response['msg'] = 'volla done the things!!'
	# import pdb;pdb.set_trace()
    # return _request('POST', params)
    # path = '/Message/'
	# respons = _request(path,params)
	# response['code'] = respons[0]
	# response['response'] = respons[1]
	# return JsonResponse(response)

    
@csrf_protect
@csrf_exempt
def call_no(request):
    response = {}
    import pdb;pdb.set_trace()
    from_no = request.POST['from_no']
    to_no = request.POST['to_no']
    answer_url = request.POST['answer_url']
    # headers = {'content-type': 'application/json'}
    path = '/Call/'


    params = {
    'from': from_no,
    'to' : to_no,
    'answer_url' : 'http://5db33dae.ngrok.com/answer'#answer_url#"http://morning-ocean-4669.herokuapp.com/report/",
    }
    respons = _request(path,params)
    response['code'] = respons[0]
    response['response'] = respons[1]
    return JsonResponse(response)

@csrf_protect
@csrf_exempt
def answer_url(request):
    import pdb;pdb.set_trace()
    pass

def _request(path,data):

    path = path.rstrip('/') + '/'
    headers = {'content-type': 'application/json'}
    headers.update(headers)
    import pdb;pdb.set_trace()
    r = requests.post(api + path, headers=headers,
                      auth=(auth_id, auth_token),
                      data=json.dumps(data))
    content = r.content
    if content:
        try:
            response = json.loads(content)
        except ValueError:
            response = content
    else:
        response = content
    return (r.status_code, response)