from django.views.generic import ListView

from .models import Blog


class IndexView(ListView):
    template_name = 'blog/index.html'
    model = Blog
    context_object_name = 'blog_list'
