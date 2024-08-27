from django.db import models


class Banner(models.Model):
    image = models.FileField(upload_to="banners", default="default.png")
    title = models.CharField(max_length=100)
    sort = models.IntegerField(default=1)
    
    class Meta:
        ordering = ["sort"]

    def __str__(self):
        return self.title


class Social(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=100)
    icon = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WhyUs(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(verbose_name="Description")
    sort = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "Why Us"

    def __str__(self):
        return self.title


class Value(models.Model):
    image = models.FileField(
        upload_to="values", blank=True, null=True, default="default.png"
    )
    name = models.CharField(max_length=100)
    desc = models.TextField(verbose_name="Description")
    sort = models.IntegerField(default=1)

    class Meta:
        ordering = ["sort"]

    def __str__(self):
        return self.name
