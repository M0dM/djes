# coding: utf-8

from django import \
    forms
from django.utils.translation import \
    ugettext_lazy as _

from djesapp.models import (
    Article,
    Blog
)


class BaseForm(forms.Form):
    """Base form without label suffix."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(BaseForm, self).__init__(*args, **kwargs)


class BaseModelForm(forms.ModelForm):
    """Base model form without label suffix."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(BaseModelForm, self).__init__(*args, **kwargs)


class BlogModelForm(BaseModelForm):
    """Define a blog form."""

    class Meta:
        """Define blog form meta properties."""

        model = Blog
        fields = ['name', 'url']


class ArticleModelForm(BaseModelForm):
    """Define an article form."""

    class Meta:
        """Define blog form meta properties."""

        model = Article
        fields = ['blog', 'name', 'content', 'url']


class SearchArticleForm(BaseForm):
    """Define a search form."""

    files = forms.CharField(
        label=_('Full-text search'),
    )
