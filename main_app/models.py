from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toy-detail', kwargs={'pk': self.id})

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # Add the M:M relationship
    toys = models.ManyToManyField(Toy)
    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cat-detail", kwargs={"cat_id": self.id})

class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'
    
    class Meta:
        # This line makes the newest feedings appear first
        ordering = ['-date']



