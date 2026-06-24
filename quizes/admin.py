from django.contrib import admin
from .models import Quiz, Quiz_Task, Quiz_Answer

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    search_fields = ["title"]


@admin.register(Quiz_Task)
class QuizTaskAdmin(admin.ModelAdmin):
    search_fields = ["context"]


@admin.register(Quiz_Answer)
class QuizAnswerAdmin(admin.ModelAdmin):
    search_fields = ["option"]