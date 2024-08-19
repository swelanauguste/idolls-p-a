from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255)
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # duration = models.DurationField()
    # is_active = models.BooleanField(default=True)
    
    class meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class Booking(models.Model):
    subject = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    sender = models.EmailField()
    cc_myself = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Promotion(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to="promotions/")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
