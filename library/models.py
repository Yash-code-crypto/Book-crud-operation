from django.db import models
from django.contrib.auth.models import User
# Used to generate urls by reversing the URL patterns
from django.urls import reverse
from django.db.models.signals import post_save
from django.contrib.auth.models import PermissionsMixin
from django.utils.timezone import now
import uuid
import random
# relation containg all genre of books

from datetime import date, timedelta, datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager







class Genre(models.Model):
    name = models.CharField(
        max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name




class Book(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character https://www.isbn-international.org/content/what-isbn')
    genre = models.ManyToManyField(
        Genre, help_text="Select a genre for this book")
    language = models.ForeignKey(
        'Language', on_delete=models.SET_NULL, null=True)
    total_copies = models.IntegerField()
    pic = models.ImageField(blank=True, null=True, upload_to='books')
    available_copies = models.IntegerField(name='available_copies')

    # __str__ method is used to override default string returnd by an object
    def __str__(self):
        return self.title



