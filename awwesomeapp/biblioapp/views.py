from django.shortcuts import render
import datetime
from django.http import HttpResponse,HttpResponseRedirect
from biblioapp.models import Article,Author
from biblioapp.forms import SearchForm,ArticleForm

from django.views.generic import DetailView
from django.views.generic.edit import CreateView



# Create your views here.
def current_datetime0(request):
    now = datetime.datetime.now ()
    article_list = Article.objects.all()
    html = " <html> <body> It is now % s . </body> </html>" % now
    html +='<ol>'
    for article in article_list:
        html += "<li>{}. {} </li>".format(article.id, article.name)
    html +='</ol>'
    return HttpResponse ( html )
def index(request):
    search = request.GET.get('search','')
    article_list = Article.objects.all()
    if search:
        article_list =article_list.filter(name__icontains=search)

    context = {
        'article_list':article_list
    }
    return render(request,'index.html',context )

def article_list(request):
    form = SearchForm(request.GET)
    article_list = Article.objects.all()
    if form.is_valid():
        for key,val in form.cleaned_data.items():
            if val:
                article_list = article_list.filter(**{key:val})


    context = {
        'article_list':article_list,
        'author_list': Author.objects.all(),
        'errors':form.errors,
        'form':form
    }
    return render(request,'article_list.html',context )

class ArticleDetail(DetailView):
    model = Article

def article_detail(request,pk):
    article= Article.objects.get(id=pk)
    context = { 'article':article }
    return render(request,'article_detail.html',context )

class ArticleCreate(CreateView):
    model = Article
    fields = '__all__'

def article_create(request):
    if request.method =="GET":
        form = ArticleForm()
        context = {
            'form':form
        }
        return render(request,'article_form.html',context )
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            context = {
                'form':form
            }
            return render(request,'article_form.html',context )

def article_update(request,pk):
    if request.method =="GET":
        articel = Article.objects.get(id=pk)
        form = ArticleForm(instance=articel)
        context = {
            'form':form
        }
        return render(request,'article_form.html',context )
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            context = {
                'form':form
            }
            return render(request,'article_form.html',context )













def current_datetime(request):
    article_list = Article.objects.all()
    context = {
        'time':datetime.datetime.now(),
        'article_list':article_list
    }
    return render(request,'index.html',context )
