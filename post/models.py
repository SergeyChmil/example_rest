from django.db import models
from django.conf import settings
from comments.models import Comment
import uuid
# Create your models here.


def scramble_uploaded_image_name(instance, filename):
    extension = filename.split('.')[-1]
    directory = instance.user.username
    return '{}/{}.{}'.format(directory, uuid.uuid4(), extension)


class Post(models.Model, ):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    publication_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    name = models.CharField(max_length=40, unique_for_date="publication_date", default='New post')
    body = models.TextField()
    # image = models.ImageField('post image', null=True, blank=True, upload_to=scramble_uploaded_image_name)

    isDraft = models.BooleanField(default=True)
    images = models.CharField(max_length=999992, blank=True, null=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):

        return self.name

    @property
    def comments(self):
        instance = self
        queryset = Comment.objects.filter_by_instance(instance)
        return queryset


class Image(models.Model):
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    name = models.CharField(max_length=40, default='New post')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField('Uploaded Image', null=True, blank=True, upload_to=scramble_uploaded_image_name)

    def __str__(self):
        return self.name
