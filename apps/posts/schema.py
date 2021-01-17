import graphene
from graphene_django import DjangoObjectType
from .models import Post , PostImages


class PostNode(DjangoObjectType):
    class Meta:
        model = Post

class PostImageNode(DjangoObjectType):
    class Meta:
        model = PostImages