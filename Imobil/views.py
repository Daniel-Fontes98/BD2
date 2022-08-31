from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import pymongo
from django.conf import settings


my_client = pymongo.MongoClient(settings.DB_NAME)

dbname = my_client['Projeto']
collection_name = dbname["auth_user"]
update_data = collection_name.update_one({'id':1}, {'$set':{'username':'Ruben'}})
count = collection_name.count()
print(count)


class PostListView(ListView):
    model = Post
    template_name = 'imobil/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Imobil/home.html', context)

def about(request):
    return render(request, 'Imobil/about.html', {'title': 'About'})


