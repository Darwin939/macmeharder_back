import graphene
from graphene_django import DjangoObjectType
from .models import Apps, App_Category , AppImages , AppAvatar


class AppCategoryNode(DjangoObjectType):
    class Meta:
        model = App_Category

class AppAvatarNode(DjangoObjectType):
    class Meta:
        model = AppAvatar

    url = graphene.String()
    def resolve_url(self,info):
        url = self.image.url
        return url

class AppsNode(DjangoObjectType):
    class Meta:
        model = Apps

class ImagesNode(DjangoObjectType):
    class Meta:
        model = AppImages
        exclude = ('mainImage',)

    url = graphene.String()

    def resolve_url(self,info):
        url = self.main_image.url
        return url

