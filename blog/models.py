from django.db import models
from django.urls import reverse


class Hashtag(models.Model):
    title = models.CharField(max_length=20, verbose_name="Хештег")
    slug = models.SlugField(null=False, db_index=True)

    def __str__(self):
        return f"{self.title}"

    def get_url(self):
        return reverse("hashtag_details", args=[self.slug])


class Gallery(models.Model):
    title = models.CharField(max_length=20, verbose_name="Название")
    image = models.FileField(
        upload_to="gallery", verbose_name="Изображение", blank=True, null=True
    )
    slug = models.SlugField(db_index=True)

    def __str__(self):
        return f"{self.title}"


class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    description = models.CharField(max_length=50, verbose_name="Описание")
    date = models.DateField(verbose_name="Дата")
    content = models.TextField(verbose_name="Контент")
    hashtag = models.ManyToManyField(Hashtag, verbose_name="Хештег", blank=True)
    image = models.FileField(
        upload_to="jpeg", verbose_name="Изображение", blank=True, null=True
    )
    slug = models.SlugField(null=False, db_index=True)

    def __str__(self):
        return f"{self.title}"

    def get_url(self):
        return reverse("post_details", args=[self.slug])
