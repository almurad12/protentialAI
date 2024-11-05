
from django.contrib import admin
from django.urls import path,include
from movie.views import MovieViewSet,RatingViewSet,AverageRatingListView,ReportMovieViewset,ShowAllListMovie

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
##only who create the movie he or she can update,delete also can show their own movie
router.register(r'movielist',MovieViewSet)
##only who create the rating he or she can update,delete also can show their rating
router.register(r'ratings',RatingViewSet)
##Report the movie If not good
router.register(r'reportMovie',ReportMovieViewset)

urlpatterns = [
     path('', include(router.urls)),
     ##show average rating and total rating of the movie
     path('averagerating/', AverageRatingListView.as_view(), name='product-list'),
     ##show all movie without login
     path('showallmovielist/',ShowAllListMovie.as_view())

]
