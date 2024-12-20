from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kores tili")
    description = models.TextField(verbose_name="Topic sertifikatlaar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="01.11.2024")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="")

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name="AZAMJON")
    email = models.EmailField(verbose_name="yuq")
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name="01.11.2024")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students', verbose_name="Kurs")

    def __str__(self):
        return self.name
