from django.db import models

# Модель преподавателя
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# Модель курса
class Course(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title

# Модель студента
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.name
