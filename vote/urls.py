from django.conf.urls import url
from . import views
urlpatterns = [
    #views.py와 연결
    url(r'^(?P<question_id>\d+)/$',views.detail,name='detail'),
    #...vote/index
    url('index',views.index ,name='index'),
    #...vote/result
    url('result',views.result,name='result'),
    #정규식......?
    #http://127.0.0.1:8000/vote/index/( ) 뒤에 오는 숫자들

]
