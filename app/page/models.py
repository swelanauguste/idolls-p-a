from django.db import models


class Value(models.Model):
    image = models.FileField(upload_to="values", blank=True, null=True, default='logo.png')
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=100, verbose_name="Description")
    sort = models.IntegerField(default=1)

    class Meta:
        ordering = ["sort"]

    def __str__(self):
        return self.name
