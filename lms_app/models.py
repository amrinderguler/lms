from django.db import models

# Create your models here.
class reader(models.Model):
    def __str__(self):
        return self.reader_name
    reference_id=models.CharField(max_length=200)
    reader_name=models.CharField(max_length=200)
    reader_contact=models.CharField(max_length=200)
    reader_address=models.TextField()
    active=models.BooleanField(default=True)

class Book(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20, unique=True)
    quantity=models.IntegerField(default=1)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    available = models.BooleanField(default=True)

class Bag(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    

