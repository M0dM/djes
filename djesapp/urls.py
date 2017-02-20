# coding: utf-8

from django.conf.urls import (
    url
)

from djesapp.views import (
    BlogCreateView,
    BlogDeleteView,
    HomeTemplateView,
    SearchArticleFormView
)


urlpatterns = [
    url(  # Create & list blogs
        r'^$',
        HomeTemplateView.as_view(),
        name="home"
    ),
    url(  # Create & list blogs
        r'^blog/create$',
        BlogCreateView.as_view(),
        name="blog"
    ),
    url(  # Delete blog by id
        r'^blog/(?P<_id>[0-9]+)/delete$',
        BlogDeleteView.as_view(),
        name="delete_blog"
    ),
    url(  # Full text query search for articles
        r'^article/search$',
        SearchArticleFormView.as_view(),
        name="search"
    ),
]
