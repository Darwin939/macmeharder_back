from django.db import models


class App_Category(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        verbose_name = 'App Category'
        verbose_name_plural = 'App_Category'
        ordering = ['name']

    def __str__(self):
        return self.name


class Apps(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, default='')
    language = models.CharField(blank=True, max_length=100, null=True)
    language_count = models.IntegerField(blank=True,null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    award = models.CharField(blank=True, max_length=100, null=True)
    place = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(App_Category, related_name='apps_list', on_delete=models.PROTECT)
    developer = models.CharField(blank=True, max_length=300, null=True)
    chart = models.CharField(blank=True, max_length=300, null=True)
    version = models.CharField(blank=True, max_length=300, null=True)
    compatibility = models.CharField(blank=True, max_length=400, null=True)

    class Meta:
        verbose_name = 'apps'
        verbose_name_plural = 'apps'
        ordering = ['created']

    def __str__(self):
        return self.title

class AppImages(models.Model):
    main_image = models.ImageField(upload_to='apps/')
    is_avatar = models.BooleanField(default=False)
    app = models.ForeignKey(Apps, related_name='app_images',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'App Images'
        verbose_name_plural = 'App_Images'


class AppAvatar(models.Model):
    image = models.ImageField(upload_to='apps/')
    app = models.ForeignKey(Apps, related_name='app_avatar',on_delete=models.CASCADE)

