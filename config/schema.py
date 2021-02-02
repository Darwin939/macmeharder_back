import graphene
from apps.apps.models import Apps, App_Category, AppImages ,AppAvatar
from apps.apps.schema import AppsNode, AppCategoryNode, ImagesNode , AppAvatarNode
from apps.posts.models import Post
from apps.posts.schema import PostNode




class Query(graphene.ObjectType):
    """ Описываем запросы и возвращаемые типы данных """

    apps_list = graphene.List(AppsNode,
                              page = graphene.Int(),
                              count = graphene.Int(),
                              category = graphene.Int())
    app_categories = graphene.List(AppCategoryNode,
                                   page=graphene.Int(),
                                   count=graphene.Int()
                                   )
    app_images = graphene.List(ImagesNode,
                               page=graphene.Int(),
                               count=graphene.Int()
                               )
    app = graphene.Field(AppsNode, app_id=graphene.ID(),)
    app_avatar = graphene.Field(AppAvatarNode, app_avatar_id = graphene.ID(),)

    def resolve_app_avatar(self,info,app_avatar_id):
        avatar = Apps.objects.get(id=app_avatar_id)
        return avatar

    def resolve_app_categories(self, info,page = 1 , count = 10):
        app_categories = App_Category.objects.all()
        return app_categories[(page - 1) * (count):(page) * count]  # pagination


    def resolve_apps_list(self, info, page = 1 , count = 10, category = None ):
        if category is not None:
            apps = Apps.objects.all().order_by('-id').filter(category_id=category)
        else:
            apps = Apps.objects.all().order_by('-id')
        apps = apps[(page-1)*(count):(page)*count]  #pagination
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

    post_list = graphene.List(PostNode,
                              page = graphene.Int(),
                              count = graphene.Int(),
                              category = graphene.Int())

    def resolve_post_list(self,info,page = 1 , count = 10 , category = None):
        if category is not None:
            posts = Post.objects.all().order_by('-id').filter(category_id = category)
        else:
            posts = Post.objects.all().order_by('-id')
        posts = posts[(page - 1) * (count):(page) * count]
        return posts


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


schema = graphene.Schema(query=Query, mutation=Mutation )
