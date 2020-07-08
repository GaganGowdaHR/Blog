from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from account.models import User
from tinymce import models as tinymce_models
from bs4 import BeautifulSoup
# from account.models import Profile

# Create your models here.

# Post
# content
# title
# statuses : draft , publish

class Catagory(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()

    def __str__(self):
        return self.name

class PostQuerySet(models.QuerySet):

    def published(self):
        return self.filter(status = "P")

    def catagories(self,id):
        return self.filter(catagory__id = id)

class PostManager(models.Manager):
    
    def get_queryset(self):
        return PostQuerySet(self.model)

    def published(self):
        return self.get_queryset().published()

    def catagories(self,id,*args,**kwargs):
        print(*args,**kwargs)
        return self.get_queryset().catagories(id)

# class CatagoryPostManager(models.Manager):
#     def get_queryset(self,*args,**kwargs):
#         print(args,kwargs)
#         return super().get_queryset().filter(catagory__id = 1)

class Post(models.Model):
    statuses = [
        ("D","Draft"),
        ("P","Published"),       
    ]     
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique = True,blank = True)
    content = tinymce_models.HTMLField()
    status = models.CharField(max_length=1,choices = statuses)
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog/post",blank = True)
    author = models.ForeignKey(User,on_delete= models.CASCADE)

    objects = models.Manager()
    posts = PostManager()

    def __str__ (self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)


    def get_absolute_url(self):
        return reverse('post-detail',kwargs = {'slug':self.slug})

    def html_to_text(self):
        soup = BeautifulSoup(self.content, features="html.parser")
        text = soup.get_text()
        return text