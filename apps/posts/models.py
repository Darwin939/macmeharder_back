from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300, blank=True, default='')
    mini_title = models.CharField(max_length=300,blank=True,null=True)
    body = models.TextField(max_length=10000, blank=True, null=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'post'
        ordering = ['created']

    def __str__(self):
        return self.title

class PostImages(models.Model):
    image = models.ImageField(upload_to='posts/')
    is_avatar = models.BooleanField(default=False)
    post = models.ForeignKey(Post, related_name='post_images',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post Images'
        verbose_name_plural = 'Post_Images'

