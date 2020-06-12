from django.shortcuts import render, get_object_or_404
# import time zone from django.utils
from django.utils import timezone
# import post from our models
from .models import Post


# create view for post_list html file
def post_list(request):
    # create posts filter to show the posts from recent one
    #* Post: indicate post model that created inside models.py folder
    #* objects:  used when you want to indicate particuler thing inside post module
    #* filter: to filter
    #* published_date__lte=timezone.now(): check if this post published (lte)less than or equal the time right now
    #* order_by('-published_date'): to show you the posts in order of published date, use the dash"-" to show the post from the newest to oldest
    # another way to use filter(not in this case): Post.objects.all().order_by('-published_date')
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # create dictionary name stuff_for_frontend and contain keyword 'posts' that's have our posts list(the valuse) that created above
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/post_list.html',stuff_for_frontend)


# create view for post_detail.html file, use pk as primary key to indicate each post(each post has unique primary key)
def post_detail(request, pk):
    ## use 'get_object_or_404' to take you to the post if it is exist, if not send you to 404 page (need to import 'get_object_or_404' from django.shortcuts in the top)
    post = get_object_or_404(Post, pk=pk)
    # save value of variable above(post) in stuff_for_frontend to return it to the page
    stuff_for_frontend = {'post': post}
    # make sure to not forget -render-
    return render(request, 'blog/post_detail.html', stuff_for_frontend)
