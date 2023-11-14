from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=1000)
    content = RichTextUploadingField()
    created = models.DateField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    class Meta:
        db_table = "blog"
        ordering = ["created"]

    def __str__(self):
        return self.title
