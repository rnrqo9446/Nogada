from django.contrib import admin
from .models import Exhibition,Classic,Concert,Musical, Musical_Comment, Exhibition_Comment, Concert_Comment, Classic_Comment, Post, Category

admin.site.register(Exhibition)
admin.site.register(Classic)
admin.site.register(Concert)
admin.site.register(Musical)
admin.site.register(Musical_Comment)
admin.site.register(Exhibition_Comment)
admin.site.register(Concert_Comment)
admin.site.register(Classic_Comment)
admin.site.register(Category)
admin.site.register(Post)
