from posts.models import Post, User

class PostFactory:
    @staticmethod
    def create_post(post_type, title, content, metadata=None):
        if metadata is None:
            metadata = {}

        author, _ = User.objects.get_or_create(username="testuser", email="test@example.com")

        return Post.objects.create(
            title=title,
            content=content,
            post_type=post_type,
            metadata=metadata,
            author=author
        )
