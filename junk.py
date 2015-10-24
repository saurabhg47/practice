# from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse, Http404
# from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from . import models
import requests


# without using shortcut render
# def index(request):
#     latest_question_list = models.Question.objects.order_by('-pub_dt')[:5]
#     template = loader.get_template('polls/index.html')
#     context = RequestContext(request, {'latest_question_list':latest_question_list,})
#     # output = ','.join([p.question_test for p in latest_question_list])
#     # return HttpResponse(output)
#     return HttpResponse(template.render(context))


# def detail(request, question_id):
#     try:
#         question = models.Question.objects.get(pk=question_id)
#     except models.Question.DoesNotExist:
#         raise Http404("Question Does Not Exist")
#     return render(request, 'polls/detail.html', {'question':question})

# Starting of django with poll app basics
# def index(request):
#     return HttpResponse('Hi This is my first temp')

# def detail(request, question_id):
#     return HttpResponse('You r luking for question %s' % question_id)

# def results(request, question_id):
#     response = 'You r luking for question %s'
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse('You r voting for question %s' % question_id)


"""
# practice for plivo API

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
    params = {
    'src': src_no,
    'dst' : dst_no,
    'text' : msg,
    'url' : s_url
    }
    headers.update(headers)
    response['msg'] = 'volla done the things!!'
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
    pass

def _request(path,data):

    path = path.rstrip('/') + '/'
    headers = {'content-type': 'application/json'}
    headers.update(headers)
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
    return (r.status_code, response)"""