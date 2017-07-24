from rest_framework import viewsets
from rest_framework.views import APIView
from post_rest.serializers import PostSerializer, ImageSerializer
from post.models import Post, Image
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser,)

    # queryset_list = Illustration.objects.all()

    def perform_create(self, serializer):
        print(self.request.data.get('image'))
        serializer.save(image=self.request.data.get('image'))

    def get_queryset(self):
        queryset = Image.objects.all()
        post = self.request.query_params.get('post', None)
        if post is not None:
            queryset = queryset.filter(post=post)
        return queryset


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('publication_date')
    serializer_class = PostSerializer
    fields = ('pk', 'isDraft', 'name', 'body', 'publication_date')

    def get_queryset(self):
        queryset = Post.objects.all()
        region = self.request.query_params.get('region', None)
        if region is not None:
            queryset = queryset.filter(city__region=region)
        return queryset
