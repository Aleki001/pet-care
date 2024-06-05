from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages


def kilimo_news(request):
    context = {
        'posts' : Post.objects.all().order_by('-date_posted')
    }
    return render(request, 'news/news.html', context)



def view_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'news/post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'News added successfully.')
            return redirect('account')
    else:
        form = PostForm()
    return render(request, 'website/account.html', {'form': form})


def delete_news(request, pk):
    news = get_object_or_404(Post, pk=pk)
    news.delete()
    return redirect('news')