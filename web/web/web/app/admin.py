# admin.py

from django.contrib import admin
from .models import UserProfile, LanguageCourse, Lesson, Quiz, QuizQuestion, Progress, QuizOption

admin.site.register(UserProfile)
admin.site.register(LanguageCourse)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(Progress)
admin.site.register(QuizOption)
