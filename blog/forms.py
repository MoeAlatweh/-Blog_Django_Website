# import forms feature from django
from django import forms
# import Post,and Comment models from models.py
from .models import Post, Comment
# import user from django
from django.contrib.auth.models import User
# import functions from crispy_forms for signup ability
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
# maybe will not gona' use it
from crispy_forms.bootstrap import (PrependedText, PrependedAppendedText, FormActions)

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


# create class of sign up model
# lines below come from documentation
class UserForm(forms.ModelForm):
    # 'widget' to show password as stars for security
    password = forms.CharField(widget=forms.PasswordInput())
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Sign up', 'Sign up', css_class='btn-primary'))
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)