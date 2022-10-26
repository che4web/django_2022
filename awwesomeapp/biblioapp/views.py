from django.shortcuts import render
import datetime
from django.http import HttpResponse
from biblioapp.models import Article



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

def current_datetime(request):
    article_list = Article.objects.all()
    context = {
        'time':datetime.datetime.now(),
        'article_list':article_list
    }
    return render(request,'index.html',context )
