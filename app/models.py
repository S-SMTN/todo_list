from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.name}"


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(
        auto_now_add=True,
        blank=True
    )
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        to=Tag,
        related_name="tasks"
    )

    def tag_list(self) -> str:
        return ", ".join(
            [str(tag) for tag in self.tags.all()]
        )

    class Meta:
        ordering = ["is_completed", "-datetime"]

    def __str__(self) -> str:
        return f"{self.content}"
