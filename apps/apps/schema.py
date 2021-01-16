import graphene
from graphene_django import DjangoObjectType
from .models import Apps, App_Category , AppImages


class AppCategoryNode(DjangoObjectType):
    class Meta:
        model = App_Category


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

