from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

from django.db.models.signals import post_save

class Language(models.Model):
    name_english = models.CharField(max_length=100)
    name_native = models.CharField(max_length=100)

    def __str__(self):
        return self.name_english

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
        
    )
    followed_languages = models.ManyToManyField(Language, related_name='followers', blank=True)
    def __str__(self):
        return self.user.username

# Create Profile when new user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # Make users follow themselves
        user_profile.follows.set([instance.profile.id])
        # Need to save again because there had to be a profile in order to call .set()
        user_profile.save()


post_save.connect(create_profile, sender=User)

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
