import csv
import os
from django.core.management.base import BaseCommand
from ...models import Social

class Command(BaseCommand):
    help = 'Imports data from a CSV file into the Social model'

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
                name = row.get('name')
                link = row.get('link')
                icon = row.get('icon', 1)

                if not name or not link:
                    self.stdout.write(self.style.WARNING(f"Skipping row with missing name or link: {row}"))
                    continue

                # Try to create the social record, skip if it already exists
                social, created = Social.objects.get_or_create(
                    name=name,
                    defaults={'link': link, 'icon': icon},
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added social: {social.name}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Social already exists: {social.name}. Skipping."))

        self.stdout.write(self.style.SUCCESS("CSV import completed!"))
