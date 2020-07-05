# import path from library django.urls
from django.urls import path
# import view
from . import views

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

]