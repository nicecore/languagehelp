from django.contrib import admin
from .models import Post, Reply, Language, Profile

from django.contrib.auth.models import User

admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Language)

# Add profile info to user info in admin panel
class ProfileInline(admin.StackedInline):
  model = Profile


# Extend User model
class UserAdmin(admin.ModelAdmin):
  model = User
  # Just display username fields on admin page
  fields = ["username"]
  inlines = [ProfileInline]

# Unregister and re-register User model in admin panel now that this change has been made

admin.site.unregister(User)

admin.site.register(User, UserAdmin)

admin.site.register(Profile)






