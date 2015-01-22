from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
# Create your views here.

from swtrivia.models import Question
def index(request):
  question_list = Question.objects.all()
  template = loader.get_template('swtrivia/index.html')
  context = RequestContext(request, {
    'latest_question_list': question_list,
    })
  
  return HttpResponse(template.render(context))


def question_detail(request,question_id):
  response = "Good luck on the star wars quiz"
  return HttpResponse(response)

def question_results(request,question_id):
  return HttpResponse("Your trying to answer question %s" % question_id)