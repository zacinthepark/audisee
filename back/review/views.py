from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404

from .serializers import ReviewListSerializer, ReviewSerializer
from .models import Review
from api.models import Movie

# Create your views here.

@api_view(['GET', 'POST'])
def movie_review_list(request, movie_pk):
    if request.method == 'GET':
        reviews = Review.objects.filter(movie=movie_pk)
        if reviews:
            serializer = ReviewListSerializer(reviews, many=True)
            return Response(serializer.data)
        else:
            return Response({})
    
    elif request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
