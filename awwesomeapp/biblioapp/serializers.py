
from rest_framework import  serializers
from biblioapp.models import Article,Author,Journal

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'name', ]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'name', ]



class ArticleSerializer(serializers.ModelSerializer):
    journal =JournalSerializer()
    author = AuthorSerializer(many=True)
    class Meta:
        model = Article
        #fields = ['id', 'name', 'date' ,'journal','author']
        fields = "__all__"


