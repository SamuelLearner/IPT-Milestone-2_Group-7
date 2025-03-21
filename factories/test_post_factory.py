import sys
import os
import django

# Setup Django environment
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "connectly_project.settings")
django.setup()

from factories.post_factory import PostFactory
from posts.models import Post

# Test creating different post types
try:
    post1 = PostFactory.create_post(post_type="text", title="My Text Post", content="This is a test post.")
    print(f"Created Post: {post1.title} (ID: {post1.id})")

    # FIXED: Added content="" to avoid missing argument error
    post2 = PostFactory.create_post(post_type="image", title="My Image Post", content="", metadata={"file_size": "2MB"})
    print(f"Created Image Post: {post2.title} (ID: {post2.id})")

    post3 = PostFactory.create_post(post_type="video", title="My Video Post", content="", metadata={"duration": "5min"})
    print(f"Created Video Post: {post3.title} (ID: {post3.id})")

except ValueError as e:
    print(f"Factory Error: {e}")
