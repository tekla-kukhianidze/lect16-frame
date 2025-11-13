
from django.urls import path, include
from rest_framework.routers import SimpleRouter


from blog.views import (
    create_blog_post,
    blog_post_list_create,
    blog_post_detail_update_delete,
    BlogPostListCreateView,
    BlogPostDetailUpdateDeleteView,
    BlogPostViewSet
)

router = SimpleRouter()
router.register(r'blog_post', BlogPostViewSet)

urlpatterns = [
    path('create_blog_post/', create_blog_post, name='create_blog_post'),
    path('blog_post_list_create/', blog_post_list_create, name='blog_post_list_create'),
    path('blog_post_list_create_class/', BlogPostListCreateView.as_view(), name='blog_post_list_create_class'),
    path('blog_post_detail_update_delete/<int:id>/', blog_post_detail_update_delete, name='blog_post_detail_update_delete'),
    path('blog_post_detail_update_delete_class/<int:id>/', BlogPostDetailUpdateDeleteView.as_view(), name='blog_post_detail_update_delete_class'),
    path('', include(router.urls)),
]

