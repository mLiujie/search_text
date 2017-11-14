from __future__ import unicode_literals

from django.contrib import admin
from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length = 60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
	return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

    def __unicode__(self):
	return u'%s %s'% (self.first_name,self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    publisher = models.ForeignKey(Publisher)
    publication_data = models.DateField()

    def __unicode__(self):
	return self.title

class UserAdmin(admin.ModelAdmin):
    list_display=('title','author','publication_data',)

admin.site.register(Book,UserAdmin)
admin.site.register(Author)
admin.site.register(Publisher)
