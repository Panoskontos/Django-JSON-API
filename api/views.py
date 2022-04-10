from django.shortcuts import render
from .serializers import *
from .models import *
# Create your views here.
# Import viewsets
from rest_framework import filters
from rest_framework import viewsets
# from rest_framework.filters import SearchFilter

# RelashionshipView
from rest_framework_json_api.views import RelationshipView


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name', 'price', 'description']


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    search_fields = ['name', 'text']
