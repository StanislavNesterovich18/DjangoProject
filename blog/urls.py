from django.urls import path

from blog import views
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blog_list_view"),
    path("<int:pk>/detail/", views.BlogDetailView.as_view(), name="blog_detail_view"),
    path("<int:pk>/delete/", views.BlogDeleteView.as_view(), name="blog_delete_view"),
    path("create/", views.BlogCreateView.as_view(), name="blog_create_view"),
    path("<int:pk>/update/", views.BlogUpdateView.as_view(), name="blog_update_view"),
]
