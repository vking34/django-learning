from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Question, Choice


def index(request):
    try:
        questions = Question.objects.all()
    except Question.DoesNotExist:
        raise Http404("There's no question !!!")

    return render(request, 'index.html', {'latest_question_list': questions})


# class indexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')[:5]

def detail(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")


    return render(request, 'detailPolls.html', {'question': question})

# class detailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'


def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)

    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'resultsPolls.html', {'question': question})

# class resultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'



def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detailPolls.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



