"""
Why Choose I-Dolls Promotional Agency?
At I-Dolls Promotional Agency, we go beyond the ordinary. We’re dedicated to making every interaction with your brand unforgettable. Here's why choosing I-Dolls is the right move for your promotional needs:
"""

"""
Choose I-Dolls Promotional Agency and partner with a team that’s committed to helping you achieve your promotional goals. Let’s elevate your brand to new heights together!
"""

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

                whyus, created = WhyUs.objects.update_or_create(
                    title=title,
                    defaults={'desc': desc, 'sort': sort},
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added whyus: {whyus.title}"))
                else:
                    self.stdout.write(self.style.SUCCESS(f"Updated whyus: {whyus.title}"))

        self.stdout.write(self.style.SUCCESS("CSV import completed!"))