from django.shortcuts import get_object_or_404,render
from django.views.generic import  ListView
from .models import Post



class HomePageView(ListView):
    model = Post
    context_object_name = "posts"
    # context_object_name: this is reference to the data that is being collected from this class here or this view
    paginate_by = 1

    def get_template_names(self):
        if self.request.htmx:
            print('htmx yes')
            return 'blog/components/post-list-elements.html'
        return 'blog/index.html'


def post_single(request,post):
    post = get_object_or_404(Post,slug = post,status = 'published')
    return render(request,'blog/single.html',{'post':post})
