from django.conf.urls import url, patterns
from swtrivia import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<question_id>\d+)/$', views.question_detail, name = 'question_detail'),
  url(r'^results/(?P<question_id>\d+)/$', views.question_results, name="question_results"),
  )