from django.contrib import admin
from .models import Article, Comment

# StackedInLine
class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]

# class CommentInLine(admin.TabularInline):
#     model = Comment
#     extra = 0

# class ArticleAdmin(admin.ModelAdmin):
#     inlines = [
#         CommentInLine,
#     ]
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)