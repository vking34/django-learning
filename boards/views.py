from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from .models import Board, Topic, Post
from .forms import NewTopicForm
# Create your views here.

def index(request):
    boards = Board.objects.all()

    return render(request, 'indexBoard.html', {'boards': boards})

def board_topics(request, board_id):
    try:
        board = Board.objects.get(pk=board_id)
    except Board.DoesNotExist:
        raise Http404("The board doesn't exist !!!")

    return render(request, 'topicsBoard.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            user = User.objects.last()
            topic = form.save(commit=False)
            topic.boards = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message = form.cleaned_data.get('message'),
                topic = topic,
                created_by = user
            )
            return redirect('boards:board_topics', board_id=board.pk)

    else:
        form = NewTopicForm()

    return render(request, 'newTopic.html', {'board': board, 'form': form})