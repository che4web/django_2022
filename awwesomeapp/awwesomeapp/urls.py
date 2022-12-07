"""awwesomeapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from biblioapp.views import (
    current_datetime,
    index,
    article_list_json,
    article_detail,
    article_create,
    article_update,
    ArticleDetail,
    ArticleCreate,
    ArticleList,
    ArticleViewSet,
    ArticleTypeViewSet,
    AuthorViewSet,
    JournalViewSet,
    JournalDetail,
    article_by_author,
)


from django.conf import settings
from django.conf.urls.static import static
from pageapp.views import PageList,PageDetail,CategoryList,CategoryDetail
from django.urls import path, include
from rest_framework import routers
from django.contrib.auth import views as auth_views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'journal', JournalViewSet)
router.register(r'type', ArticleTypeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('',index,name="article_table"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'),name="login"),
    #path('article/<int:pk>/',article_detail,name="article_detail"),
    path('journal/<int:pk>/',JournalDetail.as_view(),name="journal-detail"),
    path('article/',ArticleList.as_view(),name="article-list2"),
    path('article/json',article_list_json,name="article-list-json"),
    path('article/by_author/<int:pk>/',article_by_author,name="article_by_author"),
    path('article/<int:pk>/',ArticleDetail.as_view(),name="article_detail"),
    path('article/<int:pk>/update',article_update,name="article-update"),
    #path('article/create/',article_create,name="article-create"),
    path('article/create/',ArticleCreate.as_view(),name="article-create"),
    path('page/',PageList.as_view(),name="page-list"),
  #  path('page/<int:pk>/',PageDetail.as_view(),name="page-detail"),
    path('category/<slug:category>/<slug:slug>/',PageDetail.as_view(),name="page-detail"),
    path('category/<slug:slug>/',PageDetail.as_view(),name="page-detail-slug"),
    path('category/',CategoryList.as_view(),name="category-list"),
    path('category/<int:pk>/',CategoryDetail.as_view(),name="category-detail"),
    path('time',current_datetime),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
