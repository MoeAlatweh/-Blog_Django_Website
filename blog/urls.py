# import path from library django.urls
from django.urls import path
# import view
from . import views
# import login functionality from django
from django.contrib.auth import views as auth_views

# add links for pages of our app

urlpatterns = [
    # create url for post_list.html file
    # local: go to 127.0.0.1:8000
    # online: mydjangosite.com
    path('', views.post_list, name='post_list'),
    # <int:pk> : it is indicate the id number of the post
    # local: go to 127.0.0.1:8000/post/1
    # online: mydjangosite.com/post/1
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # local: go to 127.0.0.1:8000/post/new
    # online: mydjangosite.com/post/new
    path('post/new/', views.post_new, name='post_new'),
    # local: go to 127.0.0.1:8000/post/2/edit
    # online: mydjangosite.com/post/2/edit
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # local: go to 127.0.0.1:8000/drafts
    # online: mydjangosite.com/drafts
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    # local: go to 127.0.0.1:8000/post/2/publish
    # online: mydjangosite.com/post/2/publish
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    # local: go to 127.0.0.1:8000/accounts/login
    # online: mydjangosite.com/accounts/login
    path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),

]