from django.urls import path
from .views import UserListCreate, UserDetail, PostListCreate, PostDetail, CommentListCreate, CommentDetail

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:user_id>/', UserDetail.as_view(), name='user-detail'),
    
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:post_id>/', PostDetail.as_view(), name='post-detail'),
    
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:comment_id>/', CommentDetail.as_view(), name='comment-detail'),
]
