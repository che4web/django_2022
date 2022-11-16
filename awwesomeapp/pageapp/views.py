from django.shortcuts import render
from pageapp.models import Page,Category
from django.views.generic import DetailView,ListView

# Create your views here.
class PageList(ListView):
    model = Page

class PageDetail(DetailView):
    model = Page

class CategoryList(ListView):
    model = Category

class CategoryDetail(DetailView):
    model = Category
