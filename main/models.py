from django.db import models


class Apps(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, default='')
    language = models.CharField(blank=True, max_length=100)
    description = models.CharField(max_length=2000, blank=True)
    size = models.FloatField(blank=True)
    award = models.CharField(blank=True, max_length=100)
    place = models.IntegerField(blank=True, max_length=100)
    age = models.IntegerField(blank=True, max_length=100)

    class Meta:
        ordering = ['created']
