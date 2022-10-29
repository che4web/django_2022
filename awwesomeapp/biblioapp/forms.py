from django import forms
from biblioapp.models import Author,Article

class SearchForm(forms.Form):
    author__name__icontains = forms.CharField(label='Имя автора', max_length=100,required=False)
    date__gte =forms.DateField(
        input_formats=['%d.%m.%Y','%Y-%m-%d'],
        label='Минимальная дата',required=False)
    author =forms.ModelChoiceField(queryset=Author.objects.all(),required=False)
    typ = forms.ChoiceField(
        choices = Article.TYPE_CHOICES,
        required=False)

class BootsrapModelForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})


class ArticleForm(BootsrapModelForm):

    class Meta:
        model = Article
        fields= "__all__"
