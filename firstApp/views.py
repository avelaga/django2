from django.shortcuts import render
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

# where the actual functions go

# ListCreateAPIView - post and get
# ListAPIView - get only
class PersonList(generics.ListCreateAPIView):
  queryset = Person.objects.all() # where data is coming from
  serializer_class = PersonSerializer