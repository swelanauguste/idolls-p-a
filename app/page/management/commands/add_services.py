from django.core.management.base import BaseCommand
from promotions.models import Service

class Command(BaseCommand):
    help = 'Adds a predefined list of services to the Service model'

    def handle(self, *args, **kwargs):
        services = [
            "Brand Ambassadors",
            "Sales Ambassadors",
            "Promotional Modeling",
            "Photoshoot and Runway Modeling",
            "Product Sampling and Demonstration",
            "Event Hostesses",
            "Bottle Service",
            "Bar Services",
            "Front Gate Services",
            "Promotional Dancers",
            "Stage Management",
            "Photography",
            "Videography",
        ]

        for service_name in services:
            service, created = Service.objects.get_or_create(name=service_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added service: {service_name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Service already exists: {service_name}"))

        self.stdout.write(self.style.SUCCESS("Service list import completed!"))

