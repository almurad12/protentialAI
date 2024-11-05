from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

##show all movie
class MovieDetails(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=120)
    released_at = models.DateField()
    duration  = models.FloatField(default=0.0)
    genre = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='movies')
    language = models.CharField(max_length=50)
    
##Movie Rating Model
class Rating(models.Model):
      movie = models.ForeignKey(MovieDetails,on_delete=models.CASCADE,related_name='ratings')
      ratingUser = models.ForeignKey(User, on_delete=models.CASCADE)
      rating = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(5)])
      class Meta:
        unique_together = ('movie', 'ratingUser')  # Prevent multiple ratings from the same user
    

##Movie Report Model
class ReportMovie(models.Model):
      movieName = models.ForeignKey(MovieDetails,on_delete=models.CASCADE)
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      reportReason = models.CharField(max_length=100)