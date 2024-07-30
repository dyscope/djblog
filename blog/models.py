from django.db import models

class Post(models.Model):
    title = models.CharField("Title", max_length=100)
    author = models.CharField("Author", max_length=100)
    description = models.TextField("Post content")
    date = models.DateField("Publication date")
    img = models.ImageField("Image", upload_to="image/%Y/%m")

    def __str__(self) -> str:
        return f"{self.title}, {self.author}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
