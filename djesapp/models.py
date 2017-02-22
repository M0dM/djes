# coding: utf-8

from django.db import \
    models
from django.db.models.signals import (
    post_save,
    pre_delete
)
from simple_elasticsearch.mixins import \
    ElasticsearchTypeMixin


class Blog(models.Model):
    name = models.CharField(max_length=256)
    url = models.CharField(max_length=512)

    def __str__(self):
        return self.name

class Article(models.Model, ElasticsearchTypeMixin):
    blog = models.ForeignKey('Blog')
    name = models.CharField(max_length=256)
    content = models.TextField()
    url = models.CharField(max_length=512, null=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_queryset(cls):
        return Article.objects.all().prefetch_related(
            'blog'
        )

    @classmethod
    def get_index_name(cls):
        return 'djes'

    @classmethod
    def get_type_name(cls):
        return 'article'

    @classmethod
    def get_type_mapping(cls):
        return {
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string", "index": "analyzed", "analyzer": "custom_french_analyzer"},
                "url": {"type": "string"},
                "blog": {
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string", "index": "analyzed", "analyzer": "custom_french_analyzer"},
                        "url": {"type": "string"}
                    }
                },
                "content": {"type": "string"}
            }
        }

    @classmethod
    def get_document(cls, obj):
        return {
            'id': obj.id,
            'name': obj.name,
            'url': obj.url,
            'blog': {
                'id': obj.blog.id,
                'name': obj.blog.name,
                'url': obj.blog.url
            },
            'content': obj.content
        }


# Signals
post_save.connect(
    Article.save_handler,
    sender=Article
)
pre_delete.connect(
    Article.delete_handler,
    sender=Article
)
