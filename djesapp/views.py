# coding: utf-8

from django.views.generic import \
    TemplateView
from django.views.generic.edit import (
    CreateView,
    FormView,
    DeleteView
)

from djesapp.forms import (
    BlogModelForm,
    SearchArticleForm
)
from djesapp.models import \
    Blog


# Homepage

class HomeTemplateView(TemplateView):
    """Website homepage."""

    template_name = 'djesapp/home.html'

# Blog

class BlogCreateView(CreateView):
    """Create new blog entry."""

    form_class = BlogModelForm
    template_name = 'djesapp/blog.html'

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        kwargs['blogs'] = Blog.objects.all()
        return super(BlogCreateView, self).get_context_data(**kwargs)


class BlogDeleteView(DeleteView):
    """Delete a blog entry and all related articles (by calscade)."""

    model = Blog

    def get(self, request, *args, **kwargs):
        """Delete blog entry on get request."""
        return self.delete(request, *args, **kwargs)


# Article

class SearchArticleFormView(FormView):
    """Search for an article with given text query."""

    form_class = SearchArticleForm
    template_name = 'djesapp/search.html'
