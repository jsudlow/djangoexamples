from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from pprint import pprint
# Create your views here.

from swtrivia.models import Question
def index(request):
  question_list = Question.objects.all()
  context = {'latest_question_list':question_list}

  return render(request, 'swtrivia/index.html',context)


def question_detail(request,question_id):
  question = get_object_or_404(Question,pk=question_id)
  return render(request, 'swtrivia/detail.html', {'question': question})
  

def question_results(request,question_id):
  choice = int(request.POST['choice'])
  question = get_object_or_404(Question, pk=question_id)
  c = question.answer_set.filter(is_correct=True)
  response = ''

  if c[0].id == choice:
    response += "Correct"
  else:
    response += "Incorrect"


  return HttpResponse("You Answered %s" % response)