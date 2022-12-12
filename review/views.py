from rest_framework.viewsets import ModelViewSet
from .serializers import CommentSerializer, RatingSerializer
from .models import Comment, Rating

class CommentViewSet(ModelViewSet):
    queryset = CommentViewSet.objects.all()
    serializer_class = CommentSerializer

class RatingViewSet(ModelViewSet):
    queryset = RatingViewSet.objects.all()
    serializer_class = RatingSerializer
