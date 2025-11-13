
from django.urls import path
from blog.views import (
    create_blog_post,
    blog_post_list_create,
    blog_post_detail_update_delete,
    BlogPostListCreateView)

urlpatterns = [
    path('create_blog_post/', create_blog_post, name='create_blog_post'),
    path('blog_post_list_create/', blog_post_list_create, name='blog_post_list_create'),
    path('blog_post_list_create_class/', BlogPostListCreateView.as_view(), name='blog_post_list_create_class'),
    path('blog_post_detail_update_delete/<int:id>', blog_post_detail_update_delete, name='blog_post_detail_update_delete'),
]

