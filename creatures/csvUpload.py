import os
import django

# Set the environment variable to your settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'creatures.settings')

# Set up Django
django.setup()

from creaturesApp.models import creature
import csv

# Open and read the CSV file
with open('./Mythological Creatures.csv', newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

    for row in spamreader:
        # Ensure that row has enough values to prevent index errors
        if len(row) >= 5:
            name = row[0]
            description = row[1]
            myth = row[2]
            region = row[3]
            link = row[4]

            # Create and save the creature to the database
            creature.objects.create(
                name=name,
                description=description,
                mythology=myth,
                region=region,
                ref_link=link
            )
            print(f"Imported creature: {name}")
