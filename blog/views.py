from django.shortcuts import render, get_object_or_404, redirect
# import time zone from django.utils
from django.utils import timezone
# import post,and comment from our models
from .models import Post, Comment
# import PostForm, and CommentForm from forms.py
from blog.forms import PostForm, CommentForm
# import login_required from django
from django.contrib.auth.decorators import login_required

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

# add this code that's let you create or edit new post if you are only login, otherwise take you to login page.
@login_required
# create view for post_new to show the new pot has been create it
def post_new(request):
    # works when you submit a post
    # checking when you create post by method POST pass the information you input to them on the form
    if request.method == 'POST' :
        form = PostForm(request.POST)
        # to check if the user put valid text inside the fields , to make sure doesn't try to hack us or so
        if form.is_valid():
            # to create the post data inside the data base but not save it yet
            post = form.save(commit=False)
            # to set the author to who ever create the post
            post.author = request.user
            # to  set the publish date to time we create the post
            #post.published_date = timezone.now()
            # to save the post date inside the data base
            post.save()
            # to take you to post detail page when you submit the post
            # we add redirect to take you in other page, because if you refresh the page will let you create the post again, need to use redirect method in case you have page of checkout because you don't want to pay money every time you refresh the page
            return redirect ('post_detail', pk=post.pk)
    # work when you go to  page to create the post
    else:
        form = PostForm()
        # save value of variable above(form) in stuff_for_frontend to return it to the page
        stuff_for_frontend = {'form': form}
    return render(request, 'blog/post_edit.html' , stuff_for_frontend)

# add this code that's let you create or edit new post if you are only login, otherwise take you to login page.
@login_required
def post_edit(request, pk):
    ## use 'get_object_or_404' to take you to the post if it is exist, if not send you to 404 page
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # use 'instance' way because we need to update existing form not create new one
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # to create the post data inside the data base but not save it yet
            post = form.save(commit=False)
            # to set the author to who ever create the post
            post.author = request.user
            # to  set the publish date to time we create the post
            #post.published_date = timezone.now()
            # to save the post date inside the data base
            post.save()
            # to take you to post detail page when you submit the post
            # we add redirect to take you in other page, because if you refresh the page will let you create the post again, need to use redirect method in case you have page of checkout because you don't want to pay money every time you refresh the page
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        stuff_for_frontend = {'form': form, 'post': post}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)

# add this code that's let you create or edit new post if you are only login, otherwise take you to login page.
@login_required
def post_draft_list(request):
    # just to show post in draft by filter posts that don't have published date
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/post_draft_list.html', stuff_for_frontend)

# add this code that's let you create or edit new post if you are only login, otherwise take you to login page.
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # used publish method that we created in models.py
    post.publish()
    return redirect('post_detail', pk=pk)

# add this code that's let you add a comment if you are only login, otherwise take you to login page.
@login_required
def add_comment_to_post(request, pk):
    ## use 'get_object_or_404' to take you to the post if it is exist, if not send you to 404 page
    post = get_object_or_404(Post, pk=pk)
    ## method of POST means we want to add or edit something, but method of GET means just we see the thing as it is
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # to check if the user put valid text inside the fields , to make sure doesn't try to hack us or so
        if form.is_valid():
            # to create the comment data inside the data base but not save it yet
            comment = form.save(commit= False)
            # to set the author to who ever create the comment
            comment.author = request.user
            # to save the comment date inside the data base
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
        # else means if method is GET
    else:
        form = CommentForm()
        stuff_for_frontend = {'form': form}
    return render(request, 'blog/add_comment_to_post.html', stuff_for_frontend)


# add this code to prevent any user(not the superuser) or visitor to delete a comment   .
@login_required
# to delete comments
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


# add this code to prevent any user(not the superuser) or visitor to approve a comment   .
@login_required
# to approve comments
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)
