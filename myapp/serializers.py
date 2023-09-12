from rest_framework import serializers
from myapp.models import libraryDB

class library_serializer(serializers.ModelSerializer):
    class Meta:
        model=libraryDB
        fields=(
            'Book_id',
            'Book_Name',
            'Book_author',
            'Book_price'
        )