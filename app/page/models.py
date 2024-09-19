from django.db import models
from django.utils.text import slugify

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


class Service(models.Model):
    image = models.FileField(
        upload_to="services", blank=True, null=True, default="default.png"
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    desc = models.TextField(verbose_name="Description", blank=True, null=True)
    sort = models.IntegerField(default=1, blank=True, null=True)
    is_premium = models.BooleanField(default=False)

    class Meta:
        ordering = ["sort"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Booking(models.Model):
    subject = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


# class Promotion(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     image = models.FileField(upload_to="promotions/")
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.title