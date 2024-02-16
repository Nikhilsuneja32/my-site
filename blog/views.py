from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail


#Function base views

# def post_list(request):
#     posts = Post.published.all()

#     return render(request, 'list.html', {'posts' : posts})

# def post_detail(request, id):
def post_detail(request, year, month, day, post):
    # post = Post.published.get(id=id)
    post = Post.published.get(slug=post,publish__year=year,publish__month=month,publish__day=day)

    return render(request, 'detail.html', {'post' : post})

#Class base views

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name = "list.html"

def post_share(request, post_id):
    post = Post.published.get(id=post_id)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n{cd['name']}\'s comments: {cd['comment']}"
            send_mail(subject, message, 'nikhilsuneja.img@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'share.html', {'post': post, 'form': form, 'sent': sent})


    
