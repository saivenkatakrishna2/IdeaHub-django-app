from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-posted_date']


class DetailedIdeaView(DetailView):
    model = Post
    template_name = 'detailed_idea.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

