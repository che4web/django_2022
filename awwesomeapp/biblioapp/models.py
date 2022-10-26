from django.db import models

# Create your models here.

class CommonInfo(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255,blank=True)
    dirth_day = models.DateField(blank=True,null=True)
    class Meta:
        abstract = True

class Reader(CommonInfo):
    taiff= models.CharField(max_length=255)


class Author(CommonInfo):
    contract = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        print('hello  from save')
        instance = super().save(*args,**kwargs)
        #s ome
        return instance
    class Meta:
        ordering = ['name']
        verbose_name ='Автор'
        verbose_name_plural ='Авторы'


class Journal(models.Model):
    name = models.CharField(max_length=255)

class Article(models.Model):
    name = models.CharField(max_length=255)
    author = models.ManyToManyField(Author)
    desctiption = models.TextField(blank=True)
    data = models.DateField(blank=True,null=True)
    journal = models.ForeignKey(Journal,on_delete=models.PROTECT,null=True,blank=True)
    TYPE_CHOICES = (
        ('AR','Статья  в журнале'),
        ('BK','Книга'),
    )
    typ = models.CharField(max_length=2,
                           choices=TYPE_CHOICES,
                           default='AR',
                           verbose_name="Тип публикации"
                           )
    def get_foo(self):
        return f"id:{self.id},name: {self.name}"
