import uuid

from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500, null=True)
    url = models.URLField(max_length=500, null=True)
    image = models.URLField(max_length=500)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True, related_name='posts')
    body = models.TextField()
    likes = models.ManyToManyField(to='accounts.CustomUser', related_name="likedposts", through='LikedPost')
    tags = models.ManyToManyField(to='Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    objects = models.Manager()

    def __str__(self):
        return str(self.title)


    class Meta:
        ordering = ['-created']



class LikedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):

        return f"{self.user.username} liked {self.post.title}"


class Tag(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to='icons/', null=True, blank=True)
    slug = models.SlugField(max_length=20, unique=True)
    order = models.IntegerField(null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']



class Comment(models.Model):
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True, related_name='comments')
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=200)
    likes = models.ManyToManyField(to='accounts.CustomUser', related_name="likedcomments", through='LikedComment')
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    objects = models.Manager()

    def __str__(self):
        try:
            return f"{self.author.username} : {str(self.body[:30])}"
        except:
            return f"no author : {str(self.body[:30])}"


    class Meta:
        ordering = ['-created']



class LikedComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):

        return f"{self.user.username} liked {self.comment.body[:30]}"


class Reply(models.Model):
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True, related_name='replies')
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    body = models.CharField(max_length=200)
    likes = models.ManyToManyField(to='accounts.CustomUser', related_name="likedreplies", through='LikedReply')
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    objects = models.Manager()

    def __str__(self):
        try:
            return f"{self.author.username} : {str(self.body[:30])}"
        except:
            return f"no author : {str(self.body[:30])}"

    class Meta:
        ordering = ['created']


class LikedReply(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):

        return f"{self.user.username} liked {self.reply.body[:30]}"
