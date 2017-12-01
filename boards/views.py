from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import HttpResponse, Http404
from django.db.models import Count
from django.contrib.auth.models import User
from .models import Board, Topic, Post
from django.views.generic import View, UpdateView, ListView
from .forms import NewTopicForm, PostForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.



def index(request):
    boards = Board.objects.all()

    return render(request, 'indexBoard.html', {'boards': boards})

def board_topics(request, board_id):
    try:
        board = Board.objects.get(pk=board_id)

    except Board.DoesNotExist:
        raise Http404("The board doesn't exist !!!")
    queryset = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)

    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 5)
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)

    except EmptyPage:
        topics = paginator.page(paginator.num_pages)


    return render(request, 'topicsBoard.html', {'board': board, 'topics': topics})


@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.boards = board
            topic.starter = request.user
            topic.save()
            Post.objects.create(
                message = form.cleaned_data.get('message'),
                topic = topic,
                created_by = request.user
            )
            return redirect('boards:topic_posts', board_id=board.pk, topic_id=topic.pk)

    else:
        form = NewTopicForm()

    return render(request, 'newTopic.html', {'board': board, 'form': form})

# def topic_posts(request, board_id, topic_id):
#     topic = get_object_or_404(Topic, boards__pk=board_id, pk=topic_id)
#     topic.views += 1
#     topic.save()
#     return render(request, 'topic_posts.html', {'topic': topic})
#

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'topic_posts.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        session_key = 'view_topic_{}'.format(self.topic.pk)
        if not self.request.session.get(session_key, False):
            self.topic.views += 1
            self.topic.save()
            self.request.session[session_key] =True

        kwargs['topic'] = self.topic
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.topic = get_object_or_404(Topic, boards__pk=self.kwargs.get('board_id'), pk=self.kwargs.get('topic_id'))
        queryset = self.topic.posts.order_by('created_at')
        return queryset

@login_required
def reply_topic(request, board_id, topic_id):
    topic = get_object_or_404(Topic, boards__pk=board_id, pk=topic_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            topic.last_updated = timezone.now()
            topic.save()

            topic_url = reverse('boards:topic_posts', kwargs={'board_id': board_id, 'topic_id': topic_id})
            topic_post_url = '{url}?page={page}'.format(
                url=topic_url,
                # id=post.pk,
                page=topic.get_page_count()

            )
            return redirect(topic_post_url)
    else:
        form = PostForm()

    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ('message', )
    template_name = 'edit_post.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('boards:topic_posts', board_id=post.topic.boards.pk, topic_id=post.topic.pk)