from django.contrib.auth.models import User
from django.db import models

# Create your models here
from django.urls import reverse
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="user",on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/', default='/avatar/default.jpg',blank=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(null=True)
    about_me = models.TextField(max_length=2000,blank=True,null=True)
    def __str__(self):
        return self.user.username
    def get_absolute_url(self):
        return reverse("profile_url", kwargs={"pk": self.pk})
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='category_image', null=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_list_url", kwargs={"slug": self.slug})

class Post(models.Model):
    author = models.ForeignKey(Profile,  related_name="author", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField(max_length=50000)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL,null=True)
    slug = models.SlugField(max_length=200, default='', unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("post_single_url", kwargs={"slug": self.category.slug, "post_slug": self.slug})
    def get_comment(self):
        return self.comment.all()# comment это related_name в нашем Comment.post. он берёт все связи коментариев с этим постом
class Comment(models.Model):  # коментарии
    author = models.ForeignKey(Profile, related_name='author_comment', on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    message = models.TextField(max_length=500)
    create_at = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)

class Social(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icon/')
    url = models.URLField()

    def __str__(self):
        return self.name








