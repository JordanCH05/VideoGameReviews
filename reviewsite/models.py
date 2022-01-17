from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Game(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    developer = models.CharField(max_length=200)
    score = models.DecimalField(decimal_places=2, max_digits=3)
    image = CloudinaryField('image')
    description = models.TextField()
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return self.title

class Review(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    score = models.DecimalField(decimal_places=2, max_digits=3)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    body = models.TextField(blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Review of {self.game} by {self.username}'
