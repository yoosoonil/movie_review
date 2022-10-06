from django.db import models
from django.db.models import Avg
# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    star = models.IntegerField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def avaregereview(self):
        reviews = Review.objects.filter(review=self).aggregate(avarage=Avg('star'))
        avg=0
        if reviews["avarage"] is not None:
            avg=float(reviews["avarage"])
        return avg
    