from django.db import models


class Activity(models.Model):
    class Units(models.TextChoices):
        LESSON = "L", "Lesson"
        MINUTE = "M", "Minute"
        SET = "S", "Set"
        PAGE = "P", "Page"

    unit = models.CharField(
        max_length=1,
        choices=Units.choices,
        default=Units.MINUTE,
    )

    class Types(models.TextChoices):
        CONSTANT = "CNS", "Constant"
        COURSE = "CRS", "Course"
        BOOK = "BOK", "Book"

    type = models.CharField(
        max_length=3,
        choices=Types.choices,
        default=Types.CONSTANT,
    )
    name = models.CharField(max_length=200)
    number_of_lessons = models.PositiveSmallIntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Logs(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.date
