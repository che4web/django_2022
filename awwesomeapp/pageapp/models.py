from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('category-detail', kwargs={'pk' : self.pk})

class Page(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    headline = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.headline)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('page-detail', kwargs={'slug' : self.slug,'category':self.category.slug})
