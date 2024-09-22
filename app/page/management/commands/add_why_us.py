import csv
import os
from django.core.management.base import BaseCommand
from ...models import WhyUs

class Command(BaseCommand):
    help = 'Imports data from a CSV file into the WhyUs model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file.')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        if not os.path.exists(csv_file):
            self.stdout.write(self.style.ERROR(f"File '{csv_file}' does not exist."))
            return

        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = row.get('title')
                desc = row.get('desc')
                sort = row.get('sort', 1)

                if not title or not desc:
                    self.stdout.write(self.style.WARNING(f"Skipping row with missing title or description: {row}"))
                    continue

                # Try to create the WhyUs record, skip if it already exists
                whyus, created = WhyUs.objects.get_or_create(
                    title=title,
                    defaults={'desc': desc, 'sort': sort},
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added WhyUs: {whyus.title}"))
                else:
                    self.stdout.write(self.style.WARNING(f"WhyUs already exists: {whyus.title}. Skipping."))

        self.stdout.write(self.style.SUCCESS("CSV import completed!"))
