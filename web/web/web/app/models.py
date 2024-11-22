# models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language_preference = models.CharField(max_length=50)
    current_level = models.CharField(max_length=10)  # E.g., A1, B2, C1
    progress = models.JSONField(default=dict)  # Store progress as a JSON object

class LanguageCourse(models.Model):
    name = models.CharField(max_length=50)       # E.g., Spanish, French
    level = models.CharField(max_length=20)      # E.g., Beginner, Intermediate
    description = models.TextField()

class Lesson(models.Model):
    course = models.ForeignKey(LanguageCourse, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=100)
    content = models.TextField()                 # Lesson content or link to multimedia
    lesson_order = models.IntegerField()         # Order of lesson in the course

class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="quizzes")
    title = models.CharField(max_length=100)

class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    question_text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=100)

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="progress")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    quiz_score = models.IntegerField(null=True, blank=True)
    date_completed = models.DateTimeField(auto_now_add=True)

class QuizOption(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name="options")
    option_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)  # Mark if this option is correct
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True, validators=[EmailValidator()])
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super(CustomUser, self).save(*args, **kwargs)

    def clean(self):
        # Add any additional validations if needed
        if not self.username:
            raise ValidationError('Username is required')
        if not self.email:
            raise ValidationError('Email is required')

    def str(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'