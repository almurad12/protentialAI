from rest_framework import serializers
from django.contrib.auth.models import User
from movie.models import Rating,MovieDetails,ReportMovie
from django.db.models import Avg, Count

##Rating Serializer
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields ="__all__"



#Create Movie Serializers
class MovieDetailsSerializers(serializers.ModelSerializer):
    rating = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='rating'
    )
    class Meta:
        model = MovieDetails
        fields = "__all__"
   


#show Average Rating and Total Rating of Serializers
class AverageRatingSerializers(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    total_ratings = serializers.SerializerMethodField()
    class Meta:
        model = MovieDetails
        fields = ['id','title','average_rating','total_ratings']
    def get_average_rating(self, obj):
        return obj.ratings.aggregate(Avg('rating'))['rating__avg'] or 0

    def get_total_ratings(self, obj):
        return obj.ratings.count()

#Report Serializers   
class ReportMovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReportMovie
        fields = "__all__"