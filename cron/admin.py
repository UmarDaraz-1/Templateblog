from django.contrib import admin

# Register your models here.

from.models import Post, ContactUs, Comment

admin.site.register(Post)
admin.site.register(ContactUs)
admin.site.register(Comment)