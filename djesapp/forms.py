# coding: utf-8

from django import \
    forms
from django.utils.translation import \
    ugettext_lazy as _

from djesapp.models import \
    Blog


class BlogModelForm(forms.ModelForm):
    """Define a blog form."""

    class Meta:
        """Define blog form meta properties."""

        model = Blog
        fields = ['name', 'rss_url']


class SearchArticleForm(forms.Form):
    """Define a search form."""

    files = forms.CharField(
        label=_('Full-text search'),
    )
