
from rest_framework import  serializers
from biblioapp.models import Article,Author,Journal

class JournalSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    article__id__count = serializers.CharField()
    class Meta:
        model = Journal
        fields = ['id', 'name', 'article__id__count']


class JournalSerializerInline(serializers.ModelSerializer):
    id = serializers.CharField()
    class Meta:
        model = Journal
        fields = ['id', 'name',]


class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    class Meta:
        model = Article
        fields = ['id', 'name', ]



class ArticleSerializer(serializers.ModelSerializer):
    journal =JournalSerializerInline()
    author = AuthorSerializer(many=True)
    class Meta:
        model = Article
        #fields = ['id', 'name', 'date' ,'journal','author']
        fields = "__all__"

    def create(self, validated_data):
        author = validated_data.pop('author')
        journal = validated_data.pop('journal')
        article = Article.objects.create(journal_id=journal['id'],**validated_data)

        author_list = [a['id'] for a in author]
        for x in author_list:
            article.author.add(x)

        return article
        #return super().create(validated_data)


