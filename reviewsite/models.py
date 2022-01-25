from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

SCORE_CHOICES = [
    (0, '0.0 - Worst Game Ever'),
	(0.5, '0.5 - Horrible'),
    (1, '1.0 - Terrible'),
    (1.5, '1.5 - Rubbish'),
    (2, '2.0 - Bad'),
    (2.5, '2.5 - Mediocre'),
    (3, '3.0 - Playable'),
    (3.5, '3.5 - Ok'),
    (4, '4.0 - Good'),
    (4.5, '4.5 - Great'),
    (5, '5.0 - Master Piece'),
]


class Game(models.Model):
    """ Game Model """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    developer = models.CharField(max_length=200)
    score = models.DecimalField(decimal_places=2, max_digits=3)
    image = CloudinaryField('image')
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return self.title


class Review(models.Model):
    """ Game Review Model """
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='reviews')
    score = models.DecimalField(
        choices=SCORE_CHOICES, decimal_places=1, max_digits=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    body = models.TextField(blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Review of {self.game} by {self.username}'
