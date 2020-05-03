from rest_framework_json_api import serializers
from opinion_ate.models import Author, Movie

class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=30)
    class Meta:
        model = Author
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    score = serializers.IntegerField()
    author_id = serializers.IntegerField()
    class Meta:
        model = Movie
        fields = '__all__'        