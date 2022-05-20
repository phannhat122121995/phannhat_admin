from django.db import models
from autoslug import AutoSlugField
# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    STATUS = (
        ('True', 'Hiển Thị'),
        ('False', 'Ẩn'),
    )
    id = models.IntegerField(primary_key=True)
    # parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.SET_NULL,blank=True, null=True)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(default='default.png', upload_to='images/')
    slug = AutoSlugField(null=True, unique=True, populate_from='title', default=None)
    status=models.CharField(max_length=10, choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})


