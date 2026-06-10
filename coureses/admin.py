from django.contrib import admin
from .models import Course, Question, Answer

admin.site.register(Course)
# admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Answer)
# Register your models here.
