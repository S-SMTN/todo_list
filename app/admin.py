from django.contrib import admin

from app.models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ["content", "deadline", "tags"]
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

    def tag_list(self, obj: Task) -> str:
        return ", ".join(
            [str(tag) for tag in obj.tags.all()]
        )


admin.site.register(Tag)
