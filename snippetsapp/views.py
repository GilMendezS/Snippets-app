from .models import Snippet
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from .serializers import SnippetSerializer, UserSerializer

# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer