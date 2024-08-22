"""
Home page Welcome Message Welcome to I-Dolls Promotional Agency, where our ambassadors are more than just a friendly face – they are the driving force behind your brand’s success! With charisma, expertise, and a passion for engaging audiences, our team transforms casual event-goers into excited customers. Partnering with I-Dolls means you're not just hiring promotional models; you're empowering your brand with vibrant, energetic advocates who bring your vision to life and elevate your brand to new heights. Let us turn your next event into an unforgettable experience!
Benefits: 
"""

import csv
import os
from django.core.management.base import BaseCommand
from ...models import Value

class Command(BaseCommand):
    help = 'Imports data from a CSV file into the Value model'

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
                image = row.get('image', 'default.png')
                name = row.get('name')
                desc = row.get('desc')
                sort = row.get('sort', 1)

                if not name or not desc:
                    self.stdout.write(self.style.WARNING(f"Skipping row with missing name or description: {row}"))
                    continue

                value, created = Value.objects.update_or_create(
                    name=name,
                    defaults={'image': image, 'desc': desc, 'sort': sort},
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added value: {value.name}"))
                else:
                    self.stdout.write(self.style.SUCCESS(f"Updated value: {value.name}"))

        self.stdout.write(self.style.SUCCESS("CSV import completed!"))
