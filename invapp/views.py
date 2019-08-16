from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from invapp.forms import KakikomiForm
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post


def top_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'invapp/top_page.html', {})

def detail(request):
    return render(request, 'invapp/detail.html', {})

# def input(request):
#     return render(request, 'invapp/input.html', {})

def input_page(request):

    f = KakikomiForm()

    # if request.method == "POST":
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.author = request.user
    #         post.published_date = timezone.now()
    #         post.save()
    #         return redirect('send_page', pk=post.pk)
    # else:
    #     form = PostForm()

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('send_page')


    return render(request, 'invapp/input.html', {'form1': f, })

def send_page(request):
    return render(request, 'invapp/send.html', {})