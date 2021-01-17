import graphene
from apps.apps.models import Apps, App_Category, AppImages
from apps.apps.schema import AppsNode, AppCategoryNode, ImagesNode
from apps.posts.models import Post
from apps.posts.schema import PostNode

class Query(graphene.ObjectType):
    """ Описываем запросы и возвращаемые типы данных """
    apps_list = graphene.List(AppsNode,
                              page = graphene.Int(),
                              count = graphene.Int())
    app_categories = graphene.List(AppCategoryNode)
    app_images = graphene.List(ImagesNode)
    app = graphene.Field(AppsNode, app_id=graphene.ID())


    def resolve_app_categories(self, info):
        return App_Category.objects.all()

    def resolve_apps_list(self, info, page = 1, count = 10):
        apps = Apps.objects.all().order_by('-id')
        if page != 1 or page != 10:
            apps = apps[(page-1)*(count):(page)*count]
        return apps

    def resolve_images_list(self,info):
        return AppImages.objects.all().order_by('-id')

    def resolve_app(self, info, app_id):
        """
        :return: app data
        """
        app = Apps.objects.get(id=app_id)
        return app


    # app:post
    post = graphene.Field(PostNode,post_id = graphene.ID())

    def resolve_post(self,info,post_id):
        post = Post.objects.get(id = post_id)
        return  post

    post_list = graphene.List(PostNode)

    def resolve_post_list(self,info):
        return Post.objects.all().order_by('-id')

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


    def resolve_add_app(self, info, **kwargs):
        category, _ = App_Category.objects.get_or_create(name=kwargs.pop('category'))
        return Apps.objects.create(category=category, **kwargs)

    def resolve_remove_app(self, info, app_id):
        try:
            Apps.objects.get(id=app_id).delete()
        except Apps.DoesNotExist:
            return False
        return True

class MyType(graphene.ObjectType):
    something = graphene.String()

schema = graphene.Schema(query=Query, mutation=Mutation , types = [MyType])
