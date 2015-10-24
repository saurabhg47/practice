from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse, Http404
# from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from . import models
import requests


def index(request):
    latest_question_list = models.Question.objects.order_by('-pub_dt')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})