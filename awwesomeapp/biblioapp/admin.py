from django.contrib import admin
from biblioapp.models import Article,Author,Journal
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','name','typ']
    list_editable =['typ']
    list_filter= ['name','typ','author']
    pass

class ArticelInline(admin.TabularInline):
    model = Article

class JournalAdmin(admin.ModelAdmin):

    list_display = ['id','name','impact_factor','get_articel_count']
    list_editable =['impact_factor']
    inlines= [
        ArticelInline
    ]

admin.site.register(Article,ArticleAdmin)
admin.site.register(Author)
admin.site.register(Journal,JournalAdmin)

