from django.shortcuts import render
import datetime
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from biblioapp.models import Article,Author,Journal
from biblioapp.forms import SearchForm,ArticleForm

from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView
from rest_framework.decorators import action
from biblioapp.forms import ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from rest_framework import routers, serializers, viewsets
from django_filters import FilterSet,CharFilter
from biblioapp.serializers import AuthorSerializer,JournalSerializer,ArticleSerializer
from rest_framework import filters
from  django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
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
@login_required
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
    def get_context_data(self,*args,**kwargs):
        print(self.kwargs['pk'])
        context =  super().get_context_data(*args,**kwargs)
        return context

def article_by_author(request,pk):
    article= Article.objects.filter(author__id=pk)
    context = { 'article_list':article }
    return render(request,'biblioapp/article_list.html',context )



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
# ViewSets define the view behavior.

class ArticleSetFilter(FilterSet):
    author__name__icontains = CharFilter(field_name="author",lookup_expr="name__icontains")
    name__icontains = CharFilter(field_name="name",lookup_expr="icontains")
    class Meta:
        model = Article
        fields= '__all__'
        exclude = ['img']
from rest_framework import pagination
from rest_framework.response import  Response

class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    model = Article
    serializer_class = ArticleSerializer
    filterset_class  = ArticleSetFilter
    filter_backends = [filters.OrderingFilter,DjangoFilterBackend]
    ordering_fields = '__all__'
    pagination_class = CustomPagination
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if not user.has_perm('biblioapp.view_all_article'):
            queryset = queryset.filter(author__user=self.request.user)
        return queryset

    @action(detail=False,methods=['GET'])
    def my_article(self,request):
        queryset = self.get_queryset()
        queryset =queryset.filter(author__user=self.request.user)
        data = self.serializer_class(queryset,many=True).data
        return JsonResponse(data,safe=False)



class AuthorSetFilter(FilterSet):
    name__icontains = CharFilter(field_name="name",lookup_expr="icontains")
    class Meta:
        model = Author
        fields= '__all__'

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    model = Author
    serializer_class = AuthorSerializer
    filterset_class  = AuthorSetFilter

    @action(detail=False,methods=['GET'])
    def who_iam(self,request):
        author =self.request.user.author
        data = self.serializer_class(author).data
        return JsonResponse(data)


class JournalSetFilter(FilterSet):
    name__icontains = CharFilter(field_name="name",lookup_expr="icontains")
    class Meta:
        model = Journal
        fields= '__all__'

class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    model = Journal
    serializer_class = JournalSerializer
    filterset_class  = JournalSetFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(Count('article__id'))
        return queryset







class JournalDetail(DetailView):
    model = Journal
