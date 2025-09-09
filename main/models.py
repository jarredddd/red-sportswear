import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('sepatu running', 'Sepatu Running'),
        ('jersey', 'Jersey'),
        ('sepatu futsal', 'Sepatu Futsal'),
        ('topi', 'Topi'),
        ('sepatu bola', 'Sepatu Bola'), 
        ('celana training', 'Celana Trainings'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    news_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    stok = models.PositiveIntegerField(default=0)

    
    def __str__(self):
        return self.title
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()

    