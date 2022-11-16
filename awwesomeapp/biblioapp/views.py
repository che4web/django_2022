from django.shortcuts import render
import datetime
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from biblioapp.models import Article,Author
from biblioapp.forms import SearchForm,ArticleForm

from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView
from biblioapp.forms import ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import login_required



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
    return render(request,'index.html',{} )

def article_list_json(request):
    form = SearchForm(request.GET)
    article_list = Article.objects.all()
    if form.is_valid():
        for key,val in form.cleaned_data.items():
            if val:
                article_list = article_list.filter(**{key:val})

    res = []
    for article in  article_list:
        res.append({
            'id':article.id,
            'name':article.name,
            'journal_name':article.journal.name if article.journal else '',
            'date_year':article.date.year if article.date else '',
            'get_all_author_name':article.get_all_author_name(),
        })
    return JsonResponse(res,safe=False)


class SearchFormMixin:
    filter_form = None
    fileter_form_class = None

    def get_filter_form(self):
        if self.filter_form is None:
            self.filter_form= self.fileter_form_class(self.request.GET)
        return self.filter_form
    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.get_filter_form()
        if form.is_valid():
            for key,val in form.cleaned_data.items():
                if val:
                    queryset = queryset.filter(**{key:val})
        return queryset

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['form']=self.get_filter_form()
        return context






class ArticleList(PermissionRequiredMixin,SearchFormMixin,ListView):
    model =Article
    fileter_form_class = SearchForm
    permission_required = ('biblioapp.view_article',)
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if not user.has_perm('biblioapp.view_all_article'):
            queryset = queryset.filter(author__user=self.request.user)
        return queryset
    def get_context_data(self,*args,**kwargs):
        from pageapp.models import Page
        context =  super().get_context_data(*args,**kwargs)
        context['page_list'] = Page.objects.all()

        return context

class ArticleDetail(PermissionRequiredMixin,DetailView):
    permission_required = ('biblioapp.view_article',)
    model = Article

def article_detail(request,pk):
    article= Article.objects.get(id=pk)
    context = { 'article':article }
    return render(request,'article_detail.html',context )

class LoginPerim(LoginRequiredMixin,CreateView):
    pass

class ArticleCreate(LoginPerim):
    model = Article
    form_class = ArticleForm
    #fields = '__all__'

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
@login_required
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
