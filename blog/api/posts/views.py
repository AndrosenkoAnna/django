from rest_framework import viewsets


from api.posts.serializers import PostSerializer
from posts.models import Post, Tag


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed.
    """

    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = []
