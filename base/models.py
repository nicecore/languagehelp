from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# TODOS

""" 
Todos:


"""

class Language(models.Model):
    name_english = models.CharField(max_length=100)
    name_native = models.CharField(max_length=100)

    def __str__(self):
        return self.name_english


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField(null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    user_tags = models.CharField(max_length=255, blank=True)
    # Reply count logic
    reply_count = models.PositiveIntegerField(default=0)

    tags = TaggableManager()

    def increment_reply_count(self):
        self.reply_count += 1
        self.save()

    def decrement_reply_count(self):
        self.reply_count -= 1
        self.save()

    # Override Post model save method
    # def save(self, *args, **kwargs):
    #     if self.parent_post:
    #         self.parent_post.increment_reply_count()
    #     super().save(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     # If this post being deleted has a parent_post, decrement its reply count
    #     if self.parent_post:
    #         self.parent_post.decrement_reply_count()
    #     super().delete(*args, **kwargs)

    class Meta:
        ordering = ['-created']


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    tags = TaggableManager()

    # Many-to-one reference to Post; from Post objects can be referenced with 'replies'
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')

    def delete(self, *args, **kwargs):
        self.parent_post.decrement_reply_count()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.parent_post.increment_reply_count()
        super().save(*args, **kwargs)
