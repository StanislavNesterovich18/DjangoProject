from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

from blog.models import Blog


class BlogListView(ListView):
    """Работа со списком блогов"""
    model = Blog
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.filter(is_publish=True)


class BlogDetailView(DetailView):
    """Работа с деталями блога"""
    model = Blog

    def get_object(self, queryset=None):
        obj = super(BlogDetailView, self).get_object(queryset)
        obj.count_views += 1
        obj.save()
        return obj


class BlogDeleteView(DeleteView):
    """Удаление блога"""
    model = Blog
    success_url = reverse_lazy("blog:blog_list_view")


class BlogCreateView(CreateView):
    """Создание блога"""
    model = Blog
    success_url = reverse_lazy("blog:blog_list_view")
    fields = "title", "content", "preview"


class BlogUpdateView(UpdateView):
    """Обновление блога"""
    model = Blog
    fields = "title", "content", "preview"

    def get_success_url(self):
        return reverse_lazy("blog:blog_detail_view", kwargs={"pk": self.object.pk})
