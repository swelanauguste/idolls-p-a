from django.core.management.base import BaseCommand
from page.models import Banner


class Command(BaseCommand):
    help = "Adds a predefined list of services to the Service model"

    def handle(self, *args, **kwargs):
        banner = 'banner'
        static = 'images/'
        for i in range(1, 5):
            i, created = Banner.objects.get_or_create(
                title=banner + str(i), sort=i,            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added service: {str(i)}"))
            else:
                self.stdout.write(
                    self.style.WARNING(f"Service already exists: {str(i)}")
                )

        self.stdout.write(self.style.SUCCESS("Service list import completed!"))
