# import forms feature from django
from django import forms
# import Post,and Comment models from models.py
from .models import Post, Comment


# create class called PostForm that's built inside django to create the new post
class PostForm(forms.ModelForm):
    class Meta:
        # use post model that we have inside models.py
        model = Post
        # create field of title and text that need to fill when create new post
        fields = ('title', 'text')


# create class called CommentForm that's built inside django to create new comment
class CommentForm(forms.ModelForm):
    class Meta:
        # use comment model that we have inside models.py
        model = Comment
        # create field of text that need to fill when create new comment
        fields = ('text',)