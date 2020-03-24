from rest_framework import serializers
from .models import Person

# a serializer converts data to json for api response purposes
class PersonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Person
    # fields = ['name', 'numBitches']
    fields = '__all__' #uses all fields
