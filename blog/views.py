from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from blog.form import bdd
from blog.models import Post, AllPosts
from django.contrib.auth.decorators import login_required


class PostListView(ListView):
    model = AllPosts
    template_name = 'blog/index.html'
    context_object_name = 'Post'


@login_required
def post_a_form(request):

    if request.method == 'POST':
        form = bdd(request.POST)

        if form.is_valid():
            c = AllPosts(title=form.cleaned_data['title'],
                         content=form.cleaned_data['text'],
                         author=request.user.username)
            c.save()

    else:
        form = bdd()
    return render(request, 'blog/post.html', {'form': form})

