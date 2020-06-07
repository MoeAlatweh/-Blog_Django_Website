# import path from library django.urls
from django.urls import path
# import view
from . import views

# add links for pages of our app

urlpatterns = [
    # create url for post_list.html file
    # local: go to 127.0.0.1:8000
    path('', views.post_list, name='post_list'),
]