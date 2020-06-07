from django.db import models


class MovieReview(models.Model):
    review_idx = models.IntegerField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    violence = models.TextField(blank=True, null=True)
    exposure = models.TextField(blank=True, null=True)
    profanity = models.TextField(blank=True, null=True)
    discrimination = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    weak = models.TextField(blank=True, null=True)
    shocking = models.TextField(blank=True, null=True)
    drug = models.TextField(blank=True, null=True)
    fear = models.TextField(blank=True, null=True)
    torture = models.TextField(blank=True, null=True)
    

    class Meta:
        managed = False 
        db_table = 'movie_review'


class Movies(models.Model):
    idx = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    date = models.CharField(max_length=20, blank=True, null=True)
    genre = models.CharField(max_length=20, blank=True, null=True)
    rate = models.CharField(max_length=20, blank=True, null=True)
    img = models.ImageField(default = "noimage.png", blank=True, null=True, upload_to = "ArchiveApp/static/img/posters")
 
    class Meta:
        ordering = ("-idx",)
        managed = False
        db_table = 'movies'

class Admin(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    pwd = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'
