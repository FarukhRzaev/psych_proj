from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    date = models.DateField()
    content = models.TextField()
    slug = models.SlugField(null=False, db_index=True)

    def __str__(self):
        return f"{self.title}"

    def get_url(self):
        return reverse("post_details", args=[self.slug])
