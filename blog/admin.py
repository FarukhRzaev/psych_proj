from django.contrib import admin
from .models import Post, Hashtag, Gallery
from django.db.models import QuerySet


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title"]


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title"]


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
    filter_horizontal = ["hashtag"]

    @admin.display(description="Оценка описания")
    def description_status(self, post):
        if len(post.content) < 2000:
            return "Мало текста, исправить"
        return "Достаточно текста"

    @admin.action(description="Установить пометку, что нужно поменять описание")
    def rename_desc(self, request, qs: QuerySet):
        count_updated = qs.update(description="Нужно новое описание")
        self.message_user(
            request,
            f"Было обновлено {count_updated} записей",
        )
