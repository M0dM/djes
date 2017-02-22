# coding: utf-8
import feedparser

from django.urls import \
    reverse_lazy
from django.views.generic import \
    TemplateView
from django.views.generic.edit import (
    CreateView,
    FormView,
    DeleteView
)

from djesapp.forms import (
    ArticleModelForm,
    BlogModelForm,
    SearchArticleForm
)
from djesapp.models import (
    Article,
    Blog
)


# Blog

class BlogCreateView(CreateView):
    """Create new blog entry."""

    form_class = BlogModelForm
    template_name = 'djesapp/blog.html'
    success_url = reverse_lazy("app:blog")

    def get_context_data(self, **kwargs):
        """Insert already existing blogs into the context dict."""
        kwargs['blogs'] = Blog.objects.all()
        return super(BlogCreateView, self).get_context_data(**kwargs)


class BlogDeleteView(DeleteView):
    """Delete a blog entry and all related articles (by calscade)."""

    model = Blog
    pk_url_kwarg = '_id'
    success_url = reverse_lazy("app:blog")

    def get(self, request, *args, **kwargs):
        """Delete blog entry on get request."""
        return self.delete(request, *args, **kwargs)


# Article

class ArticleCreateView(CreateView):
    """Create new article entry."""

    http_method_names = [u'post']
    form_class = ArticleModelForm
    search_form_class = SearchArticleForm
    template_name = 'djesapp/article.html'
    success_url = reverse_lazy("app:article")


class ArticleDeleteView(DeleteView):
    """Delete a article entry and all related articles (by calscade)."""

    model = Article
    pk_url_kwarg = '_id'
    success_url = reverse_lazy("app:article")

    def get(self, request, *args, **kwargs):
        """Delete article entry on get request."""
        return self.delete(request, *args, **kwargs)


class SearchArticleFormView(FormView):
    """Search for an article with given text query."""

    form_class = SearchArticleForm
    article_form_class = ArticleModelForm
    template_name = 'djesapp/article.html'
    success_url = reverse_lazy("app:blog")

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        context = self.get_context_data()
        ids = []
        context['articles'] = Article.objects.filter(pk__in=ids)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        """Insert all existing articles into the context dict before redirection."""
        context = self.get_context_data()
        context['articles'] = Article.objects.all()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        """Insert already existing articles & SearchArticleForm into the context dict."""
        kwargs['article_form'] = self.article_form_class()
        return super(SearchArticleFormView, self).get_context_data(**kwargs)
