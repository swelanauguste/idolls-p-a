from django.core.management.base import BaseCommand
from page.models import Banner

class Command(BaseCommand):
    help = "Adds a predefined list of banners to the Banner model"

    def handle(self, *args, **kwargs):
        banner = 'banner'
        static = 'images/'
        
        for i in range(1, 5):
            title = f"{banner}{i}"
            if not Banner.objects.filter(title=title, sort=i).exists():
                banner_instance, created = Banner.objects.get_or_create(
                    title=title, sort=i
                )
                self.stdout.write(self.style.SUCCESS(f"Added banner: {title}"))
            else:
                self.stdout.write(
                    self.style.WARNING(f"Banner already exists: {title}")
                )

        self.stdout.write(self.style.SUCCESS("Banner list import completed!"))
