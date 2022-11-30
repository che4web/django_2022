from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name ='Автор'
        verbose_name_plural ='Авторы'


class Journal(models.Model):
    name = models.CharField(max_length=255)
    impact_factor = models.FloatField(blank=True,null=True)
    QUARTILE_CHOICES = (
        ("Q1",'Первый квартиль'),
        ("Q2",'Второй квартиль'),
        ("Q3",'Третий квартиль'),
        ("Q4",'Четверты квартиль'),
    )
    quartile = models.CharField(max_length=2,choices=QUARTILE_CHOICES,default='Q4')

    def get_articel_count(self):
        return self.article_set.all().count()
    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=255,verbose_name='Заголовок стати')
    img = models.ImageField(blank=True,null=True,verbose_name='Картинка')
    author = models.ManyToManyField(Author,verbose_name="Авторы")
    desctiption = models.TextField(blank=True,verbose_name="Описание")
    date = models.DateField(blank=True,null=True,verbose_name="дата публикации")
    journal = models.ForeignKey(Journal,
                                on_delete=models.PROTECT,
                                null=True,blank=True,
                                verbose_name="Журнал")
    TYPE_CHOICES = (
        ('AR','Статья  в журнале'),
        ('BK','Книга'),
    )
    pages = models.CharField(max_length=255,blank=True)
    volume = models.CharField(max_length=255,blank=True)
    year = models.CharField(max_length=255,blank=True)
    typ = models.CharField(max_length=2,
                           choices=TYPE_CHOICES,
                           default='AR',
                           verbose_name="Тип публикации"
                           )
    doi = models.CharField(max_length=255,blank=True,null=True)
    referens = models.ManyToManyField('Article',verbose_name="Ссылки")
    def __str__(self):
        return self.get_all_author_name() +self.name
    def save(self,*args,**kwargs):
    #    self.name = self.name.lower()
        return super().save(*args,**kwargs)

    def normal_name(self):
        return self.name.lower()

    def get_all_author_name(self):
        return ', '.join( self.author.all().values_list('name',flat=True))

    def get_foo(self):
        return f"id:{self.id},name: {self.name}"
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('article_detail', kwargs={'pk' : self.pk})

    def get_edit_url(self):
        from django.urls import reverse
        return reverse('article-update', kwargs={'pk' : self.pk})

    class Meta:
        permissions= (
            ('view_all_article',"Может смотреть все статиь"),
        )
