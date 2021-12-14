from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class School(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name


class Course(models.Model):
  SPRING = 'Spring'
  SUMMER = 'Summer'
  FALL = 'Fall'
  WINTER = 'Winter'
  SEMESTER_CHOICES = [
    (SPRING, 'Spring'),
    (SUMMER, 'Summer'),
    (FALL, 'Fall'),
    (WINTER, 'Winter'),
  ]
  name = models.CharField(max_length=50)
  section_num = models.IntegerField(blank=True)
  semester = models.CharField(
    max_length=6,
    choices=SEMESTER_CHOICES,
    blank=True
  )
  year = models.IntegerField(blank=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class FlashcardDeck(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(blank=True)
  course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Flashcard(models.Model):
  front = models.TextField()
  back = models.TextField()
  flashcard_deck = models.ForeignKey(FlashcardDeck, on_delete=models.CASCADE)


