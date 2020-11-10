from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = '博客'
class CommentsConfig(AppConfig):
    name = 'comments'
    verbose_name = '评论'
