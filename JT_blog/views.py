from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import BlogPost

class PostListView(TemplateView):
    template_name = "JT_blog/post_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog_posts"] = BlogPost.objects.all()[:5]
        return context
    
class PostCreateView(CreateView):
    model = BlogPost
    template_name = "JT_blog/post_create.html"
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')
