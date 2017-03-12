from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post


urlpatterns = [
                url(r'^$', ListView.as_view(
                                    queryset=Post.objects.all().order_by("-date")[:25],
                                    template_name="blog/blog.html")),
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name="blog/post.html"))
            ]
# The second URL looks weird, but its basically taking primary key digit values for blog posts so I can create views
# without having to create new views every time