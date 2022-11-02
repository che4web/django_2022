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
    article_list,
    article_detail,
    article_create,
    article_update,
    ArticleDetail,
    ArticleCreate,
    ArticleList,
)


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name="article_table"),
    #path('article/<int:pk>/',article_detail,name="article_detail"),
    path('article/',ArticleList.as_view(),name="article-list"),
    path('article/<int:pk>/',ArticleDetail.as_view(),name="article_detail"),
    path('article/<int:pk>/update',article_update,name="article-update"),
    #path('article/create/',article_create,name="article-create"),
    path('article/create/',ArticleCreate.as_view(),name="article-create"),
    path('time',current_datetime),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
