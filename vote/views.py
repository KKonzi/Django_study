from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Question
from django.template import loader #로딩해주는 역할
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:]
    '''
    #페이지 디자인 하드 코딩
    output='.'.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
    '''
    template = loader.get_template('vote/index.html')
    context={
        'latest_question_list':latest_question_list,
    } #context라는 놈을 html에게 넘겨줌, html에서 context의 인자들 사용 가능!
    return HttpResponse(template.render(context,request))

def result(request):
    return HttpResponse("We are result page")

def detail(request,question_id):
    #예외 처리 할 필요 없이 아니면 바로 404발생
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'vote/detail.html',{'question':question})