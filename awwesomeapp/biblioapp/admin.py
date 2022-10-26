from django.contrib import admin
from biblioapp.models import Article,Author
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','name','typ']
    list_editable =['typ']
    list_filter= ['name','typ','author']
    pass

admin.site.register(Article,ArticleAdmin)
admin.site.register(Author)

