# import forms feature from django
from django import forms
# import Post model from models.py
from .models import Post


# create class called PostForm that's built inside django to create the new post
class PostForm(forms.ModelForm):
    class Meta:
        # use post model that we have inside models.py
        model = Post
        # create field of title and text that need to fill when create new post
        fields = ('title', 'text')