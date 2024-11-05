from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView,ListCreateAPIView
from movie.models import MovieDetails,Rating,ReportMovie
from movie.serializers import MovieDetailsSerializers,RatingSerializer,AverageRatingSerializers, ReportMovieSerializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

##only who create the movie he or she can update,delete also can show their own movie
class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieDetails.objects.all()
    serializer_class = MovieDetailsSerializers
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return MovieDetails.objects.filter(created_by=user)
    
##only who create the rating he or she can update,delete also can show their rating
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Rating.objects.filter(ratingUser=user)

##show average rating and total rating of the movie
class AverageRatingListView(generics.ListAPIView):
    queryset = MovieDetails.objects.all()
    serializer_class = AverageRatingSerializers
##Report Movie If not good
class ReportMovieViewset(viewsets.ModelViewSet):
    queryset = ReportMovie.objects.all()
    serializer_class = ReportMovieSerializers
    permission_classes = [IsAuthenticated]

##Show all movie without login
class ShowAllListMovie(ListAPIView):
    queryset = MovieDetails.objects.all()
    serializer_class = MovieDetailsSerializers