# coding: utf-8

from django.conf.urls import (
    url
)

from djesapp.views import (
    ArticleCreateView,
    ArticleDeleteView,
    BlogCreateView,
    BlogDeleteView,
    SearchArticleFormView
)


urlpatterns = [
    url(  # Create & list articles
        r'^article/create$',
        ArticleCreateView.as_view(),
        name="article"
    ),
    url(  # Delete article by id
        r'^article/(?P<_id>[0-9]+)/delete$',
        ArticleDeleteView.as_view(),
        name="delete_article"
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
    url(  # Filter the article list
        r'^$',
        SearchArticleFormView.as_view(),
        name="search"
    )
]
