import csv
import os
from django.core.management.base import BaseCommand
from ...models import Value


class Command(BaseCommand):
    help = "Imports data from a CSV file into the Value model"

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

                if not name or not desc:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Skipping row with missing name or description: {row}"
                        )
                    )
                    continue

                # Try to create the value, skip if it already exists
                value, created = Value.objects.get_or_create(
                    name=name,
                    defaults={"image": image, "desc": desc, "sort": sort},
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added value: {value.name}"))
                else:
                    self.stdout.write(
                        self.style.WARNING(f"Value already exists: {value.name}. Skipping.")
                    )

        self.stdout.write(self.style.SUCCESS("CSV import completed!"))
