from django.db import models

# Create your models here.

class QueryResponse(models.Model):
    email = models.EmailField()
    question = models.TextField()
    response = models.TextField()

    def __str__(self):
        return f"{self.email} - {self.question[:50]}"

