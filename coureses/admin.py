from django.contrib import admin
from .models import Course, Module, Topic, Quest, Question, Answer


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "module",
    )

    search_fields = (
        "title",
        "module__title",
    )


@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "content",
        "get_topic",
    )

    search_fields = (
        "content",
        "quest__title",
    )

    def get_topic(self, obj):
        return obj.quest.title

    get_topic.short_description = "Temat"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "short_content",
        "get_topic",
        "order",
    )

    ordering = (
        "question__quest__title",
        "order",
    )

    search_fields = (
        "content",
        "question__quest__title",
    )

    def short_content(self, obj):
        return obj.content[:60]

    short_content.short_description = "Pytanie"

    def get_topic(self, obj):
        return obj.question.quest.title

    get_topic.short_description = "Temat"


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    autocomplete_fields = ["question"]
    list_display = (
        "id",
        "content",
        "is_correct",
        "get_question",
    )

    list_filter = (
        "is_correct",
    )

    search_fields = (
        "question__content",
    )

    def get_question(self, obj):
        return obj.question.content[:50]

    get_question.short_description = "Pytanie"


admin.site.register(Course)
admin.site.register(Module)
