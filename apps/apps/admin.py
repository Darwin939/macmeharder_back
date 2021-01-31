from django.contrib import admin
from .models import App_Category,Apps,AppImages, AppAvatar
# from django.contrib.admin

admin.site.register(Apps)
admin.site.register(App_Category)
admin.site.register(AppImages)
admin.site.register(AppAvatar)