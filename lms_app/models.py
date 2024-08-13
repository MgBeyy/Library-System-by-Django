from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    status_book = [
        ('available', 'Available'),
        ('rental', 'Rental'),
        ('sold', 'sold'),
    ]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True, null=True)
    photo_book = models.ImageField(upload_to='photos', blank=True, null=True)
    photo_author = models.ImageField(upload_to='photos', blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rental_price_day = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rental_period = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status_book, default='available', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True, related_name='books')

    def __str__(self):
        return f'{self.title} by {self.author}' if self.author else self.title

    @property
    def title_and_author(self):
        return f'{self.title} by {self.author}' if self.author else self.title
