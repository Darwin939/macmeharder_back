import graphene
from graphene_django import DjangoObjectType
from .models import Post


class PostNode(DjangoObjectType):
    class Meta:
        model = Post
