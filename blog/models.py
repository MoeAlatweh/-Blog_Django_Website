from django.db import models
#import timezone
from django.utils import timezone


# Create post model and include things you want to see in the post
class Post(models.Model):
    #create author that indicate whose create the post by using ForeignKey
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #create post title by using CharField
    title = models.CharField(max_length=200)
    #create post content by using TextField to can input unlimited lines
    text = models.TextField()
    #create created_date of post by using DateTimeField and make time of creating the post is default time
    created_date = models.DateTimeField(default=timezone.now)
    #create published_date by using DateTimeField
    published_date = models.DateTimeField(blank=True, null=True)

    # create method and call it publish and sit it to the time you publish your post
    def publish(self):
        self.published_date = timezone.now()
        self.save()



    # create string represintaion to show you title of post not just (post object1...)
    # you can return any thing you like to see like author or created-time... , it will be the same just replace title
    def __str__(self):
        return self.title
    # to show the title and the author:
      # return str(self.title) + 'by' + str(self.author)



