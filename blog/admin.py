from django.contrib import admin
from .models import Post
from django.db.models import QuerySet

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "description", "date", "description_status"]
    list_editable = ["description", "date"]
    ordering = ["-date"]
    list_per_page = 10
    actions = ["rename_desc"]
    search_fields = ["title__startswith", "description", "date"]
    list_filter = ["date"]

    @admin.display(description="Оценка описания")
    def description_status(self, post):
        if len(post.content) < 30:
            return "Мало текста, исправить"
        return "Достаточно текста"

    @admin.action(description="Установить пометку, что нужно поменять описание")
    def rename_desc(self, request, qs: QuerySet):
        count_updated = qs.update(description="Нужно новое описание")
        self.message_user(
            request,
            f"Было обновлено {count_updated} записей",
        )
