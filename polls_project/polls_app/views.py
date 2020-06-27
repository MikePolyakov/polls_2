from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Question, Answer, UserRespond


class IndexView(ListView):
    template_name = 'polls_app/index.html'
    context_object_name = 'latest_questions_list'

    def get_queryset(self):
        """Вернуть 2 последних свежих опроса"""
        return Question.objects.order_by('-date_published')[:2]


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'polls_app/detail.html'


def vote(request, poll_id):
    question = get_object_or_404(Question, pk=poll_id)
    if not question.is_active:
        return HttpResponse('Опрос снят с публикации')
    else:
        if request.POST.get('answer'):
            answer_id = request.POST['answer']
            print('answer id = ', answer_id)
            answer_option = Answer.objects.get(pk=answer_id)
            print(answer_option)

            UserRespond.objects.create(answer_id=answer_option)

            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        else:
            return render(request, 'polls_app/detail.html', {
                'question': question,
                'error_message': "Вы не выбрали ответ.",
            })


class ResultsView(DetailView):
    model = Question
    template_name = 'polls_app/results.html'



