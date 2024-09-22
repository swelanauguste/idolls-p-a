import csv
import os

from django.core.management.base import BaseCommand
from ...models import Service


class Command(BaseCommand):
    help = "Imports data from a CSV file into the Service model"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="The path to the CSV file.")

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_file"]

        if not os.path.exists(csv_file):
            self.stdout.write(self.style.ERROR(f"File '{csv_file}' does not exist."))
            return

        with open(csv_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                image = row.get("image", "default.png")
                name = row.get("name")
                desc = row.get("desc")
                sort = row.get("sort", 1)
                is_premium = row.get("is_premium")

                if not name or not desc:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Skipping row with missing name or description: {row}"
                        )
                    )
                    continue

                if Service.objects.filter(name=name).exists():
                    self.stdout.write(
                        self.style.WARNING(f"Service already exists: {name}. Skipping update.")
                    )
                    continue

                # Create or update the service if it does not exist
                services, created = Service.objects.update_or_create(
                    name=name,
                    defaults={"image": image, "desc": desc, "sort": sort, "is_premium": is_premium},
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added service: {services.name}"))
                else:
                    self.stdout.write(self.style.SUCCESS(f"Updated service: {services.name}"))

        self.stdout.write(self.style.SUCCESS("CSV import completed!"))
