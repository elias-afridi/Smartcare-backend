from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Doctor,Specialization,Designation,AvailableTime,Review
from .serializers import DoctorSerializer,DesignationSerializer,SpecializationSerializer,AvailableTimeSerializer,ReviewSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
class SpecialiazationViewSet(viewsets.ModelViewSet):
    
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    
    
class DesignationViewSet(viewsets.ModelViewSet):
    
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    
    
class AvailableTimeViewSet(viewsets.ModelViewSet):
    
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    
    
class ReviewViewSet(viewsets.ModelViewSet):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer