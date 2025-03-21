from rest_framework import viewsets
from .models import Contact
from .contact_serializers import ContactSerializer
from .comment_serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

#Building News Feed
from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer

class NewsFeedPagination(PageNumberPagination):
    page_size = 10  # Adjust this as needed
    page_size_query_param = 'page_size'
    max_page_size = 50

class NewsFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure user is logged in
    pagination_class = NewsFeedPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']  # Allows sorting by created_at

    def get_queryset(self):
        """
        Fetch posts that are relevant to the authenticated user.
        """
        user = self.request.user
        return Post.objects.filter(author=user).order_by('-created_at')  # Show recent posts first

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Automatically sets the author

    def get_serializer_context(self):
        return {"request": self.request}  # Pass request into serializer
    
    