from django.contrib import admin
from .models import User, Answer, Question, Quiz


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
    list_filter = ("first_name", "last_name")


class QuestionInline(admin.TabularInline):
    model = Question


class QuizesAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Quiz, QuizesAdmin)
admin.site.register(Answer)
