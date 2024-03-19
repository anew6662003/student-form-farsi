from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Student(models.Model):
    student_number = models.PositiveIntegerField(_('شماره دانش آموزی'))
    first_name = models.CharField(_('اسم'),max_length=50)
    last_name = models.CharField(_('فامیلی'),max_length=50)
    email = models.EmailField(_('ایمیل'),unique=True, max_length=50, blank = True, null=True)
    field_of_study = models.CharField(_('درس مورد نظر'),max_length=100,  blank=False, null=True )
    gpa = models.FloatField(_('نمره'))

    def __str__(self):
        return f'student: {self.first_name}{self.last_name}'