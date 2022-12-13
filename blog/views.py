from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import (PostForm, EditForm, CommentForm, AskForm, AnswerForm )
from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
 )


class HomeView(LoginRequiredMixin, ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-id')
    template_name = 'home.html'
    paginate_by = 7
    login_url = 'login'


class PendingQuestionView(LoginRequiredMixin,UserPassesTestMixin, ListView):
    model = Post
    queryset = Post.objects.filter(status=0).order_by('-id')
    template_name = 'pending_questions.html'
    paginate_by = 7
    login_url = 'login'

    def test_func(self):
        return self.request.user.role == 3


class QA_DetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'QA_detail.html'
    login_url = 'login'


class AskQuestionView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Post 
    template_name = 'ask_questions.html'
    form_class = AskForm
    login_url = 'login'

    def test_func(self):
        return self.request.user.role == 2 


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comments.html'
    form_class = CommentForm
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('qa_detail', kwargs={'pk': self.kwargs['pk']})
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'update.html'
    form_class = EditForm
    login_url = 'login'

    def test_func(self):
        return self.request.user.role == 3 


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def test_func(self):
        return self.request.user.role == 3 or self.request.user.role == 1 

class AddQuestionView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post 
    template_name = 'add_questions.html'
    form_class = PostForm
    login_url = 'login'

    def test_func(self):
        return self.request.user.role == 3 


class AnswerQuestionView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'answer_question.html'
    form_class = AnswerForm
    login_url = 'login'

    def test_func(self):
        return self.request.user.role == 3 