from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ('created_at', )

    def __str__(self):
        return f'{self.owner}--->{self.title}'

class Like(models.Model):
    owner = models.ForeignKey('auth.User', related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    likes_number = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.post}-->{self.owner}"


class DisLike(models.Model):
    owner = models.OneToOneField('auth.User', related_name='dis_likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="dis_likes", on_delete=models.CASCADE)
    dislikes_number = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.post}-->{self.owner}"