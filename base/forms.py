from django.forms import ModelForm
from .models import Post, Reply
from django.contrib.auth.models import User

# Still need ReplyForm

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'language']
        # Does literally every hashtag get saved in the database, because that seems like an impossible number of database rows
        # fields = '__all__'
        # exclude = ['author', 'created', 'reply_count' ]


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['body']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


