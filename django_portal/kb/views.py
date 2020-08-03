from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import ArticleCreateForm, RawArticleCreateForm, RawLoginForm
from .models import Article
from django.views import View
from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
)
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.postgres.search import SearchVector
from taggit.models import Tag


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article_create.html'
    form_class = ArticleCreateForm
    queryset = Article.objects.all()
    login_url = '/login/'
    redirect_field_name = ''


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'article_create.html'
    form_class = ArticleCreateForm
    queryset = Article.objects.all()
    login_url = '/login/'
    redirect_field_name = ''
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)


class ArticleListView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        tags = Tag.objects.all()
        tags_cloud = {}
        for tag in tags:
            counter = 0
            for article in articles:
                if tag.name in article.tags.names():
                    counter+=1
            if counter !=0:
                tags_cloud[tag.name] = counter
        print(tags_cloud)
        tags_cloud_sorted = {k: v for k, v in sorted(tags_cloud.items(), key=lambda item: item[1],reverse=True)}
        context = {'articles': articles,
        'tags': tags,
        'tags_cloud':tags_cloud_sorted}
        return render(request, "articles_list.html", context) 


class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = 'article.html'
    queryset = Article.objects.all()
    login_url = '/login/'
    redirect_field_name = ''


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'article_delete.html'
    login_url = '/login/'
    redirect_field_name = ''

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)
    def get_success_url(self):
        return reverse('article-list')


class ArticleSearchView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request, *args, **kwargs):
        q = self.request.GET.get('q', '')
        t = self.request.GET.get('t', None)
        txt_query= 	Article.objects.filter(text__contains=q) | \
        Article.objects.filter(title__contains=q) | \
        Article.objects.filter(author__contains=q) 
       # Article.objects.filter(author__category=c) 
        if t is None:
            articles = txt_query
        else:
            articles = txt_query.filter(tags__name__in=[t]) 
        articles_all = Article.objects.all()
        tags = Tag.objects.all()
        tags_cloud = {}
        for tag in tags:
            counter = 0
            for article in articles_all:
                if tag.name in article.tags.names():
                    counter+=1
            if counter !=0:
                tags_cloud[tag.name] = counter
        tags_cloud_sorted = {k: v for k, v in sorted(tags_cloud.items(), key=lambda item: item[1],reverse=True)}
        context = {'articles': articles,
        'tags': tags,
        'tags_cloud':tags_cloud_sorted}
        return render(request, "articles_list.html", context) 


class ArticleTagSearchView(LoginRequiredMixin, ListView):
	template_name = 'articles_list.html'
	login_url = '/login/'
	redirect_field_name = ''

	def get_queryset(self, **kwargs):
		q = self.request.GET.get('q', None)
		print(q)
		return Article.objects.filter(tags__name__in=q) 


class CommingSoonView(LoginRequiredMixin, DetailView):
    template_name = 'comming_soon.html'
    login_url = '/login/'
    redirect_field_name = ''


def login_view(request):
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == "GET":
		return render(request, "login.html", {})
	
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/login')
