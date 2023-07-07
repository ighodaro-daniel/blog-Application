from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponse
from .models import Question,Choice
from django.utils import timezone
from django.urls import reverse
from django.contrib import messages
# Create your views here.
def index(request,):
    submitted_title= request.session.pop('submitted_title',None)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context ={'latest_question_list': latest_question_list,'submitted_title':submitted_title}
    messages.get_messages(request)
    return render(request,'blog/index.html',context)


def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {"question":question}
    
    return render(request,"blog/detail.html",context)



def result(request,question_id):
    return HttpResponse('you are looking at question %s'%question_id)


def deleteText(request,question_id):
   question = get_object_or_404(Question,pk=question_id)

   question.delete()
   return redirect('blog:home')


def createText(request):
  if request.method =='POST':
      title = request.POST['title']
      article = request.POST['article']
      question = Question.objects.create(question =title,pub_date =timezone.now())
      choice = Choice.objects.create(question_choice=question, text= article )
      choice.save()
      request.session['submittied_title']=title
      messages.success(request,'Article created succesfully')
      
      return redirect('blog:home')
  else:
        return redirect('blog:home')
    