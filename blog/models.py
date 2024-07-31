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


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField("Name", max_length=50)
    text_comments = models.TextField("Comment", max_length=1000)
    post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}, {self.post}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

