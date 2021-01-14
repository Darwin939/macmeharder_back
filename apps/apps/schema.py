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

class Query(graphene.ObjectType):
    """ Описываем запросы и возвращаемые типы данных """
    apps_list = graphene.List(AppsNode)
    app_categories = graphene.List(AppCategoryNode)
    app_images = graphene.List(ImagesNode)
    app = graphene.Field(AppsNode)

    def resolve_app(self,info,app_id):
        """
        :param info:
        :param id:
        :return:
        """
        return Apps.objects.get(id=app_id)

    def resolve_app_categories(self, info):
        return App_Category.objects.all()

    def resolve_apps_list(self, info):
        return Apps.objects.all().order_by('-id')

    def resolve_images_list(self,info):
        return AppImages.objects.all().order_by('-id')


class Mutation(graphene.ObjectType):
    add_app = graphene.Field(AppsNode,
                             title=graphene.String(required=True),
                             language=graphene.String(),
                             description=graphene.String(),
                             size=graphene.String(),
                             award=graphene.String(),
                             place=graphene.String(),
                             age=graphene.String(),
                             category=graphene.String(required=True))

    remove_app = graphene.Field(graphene.Boolean, app_id=graphene.ID())
    toggle_app = graphene.Field(AppsNode, app_id=graphene.ID())

    def resolve_add_app(self, info, **kwargs):
        category, _ = App_Category.objects.get_or_create(name=kwargs.pop('category'))
        return Apps.objects.create(category=category, **kwargs)

    def resolve_remove_app(self, info, app_id):
        try:
            Apps.objects.get(id=app_id).delete()
        except Apps.DoesNotExist:
            return False
        return True

    def resolve_toggle_app(self, info, app_id):
        app = Apps.objects.get(id=app_id)
        return app
