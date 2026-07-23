from django.contrib import admin
from blog.models import Post,Category,Comments
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ["title","author","counted_views", "status", "published_date"]
    list_filter = ("status","author")
    search_fields = ["title", "content"]
    summernote_fields = ('content',)

    class Meta:
       ordering = ["-created_date"]

class CommentsAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"

    list_display = [
        "name",
        "post_title",
        "approved",
        "created_date",
    ]

    list_filter = (
        "approved",
        "post",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
        "post__title",
    )

    ordering = ("-created_date",)

    @admin.display(description="title")
    def post_title(self, obj):
        return obj.post.title

admin.site.register(Comments,CommentsAdmin)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)