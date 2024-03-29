"""model is handling the posts for the blog"""
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    """tag model with a caption field"""
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Author(models.Model):
    """Author model with the following fields"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.fullname()
class Post(models.Model):
    """New Post Class"""
    title = models.CharField(max_length=250)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    # setting up a relation with author
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True,related_name="posts")
    tags = models.ManyToManyField(Tag)