from django.contrib import admin

from app.models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ["content", "deadline", "tags", "is_completed"]
    list_display = [
        "content",
        "datetime",
        "deadline",
        "is_completed",
        "tag_list"
    ]
    list_filter = [
        "datetime",
        "is_completed",
        "tags"
    ]


admin.site.register(Tag)
