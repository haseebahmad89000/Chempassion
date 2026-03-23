import os
import sys
import django

# Add the project directory to Python path
sys.path.append('C:\\Users\\Dell\\igcse-chemistry-platform')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chemistry_hub.settings')
django.setup()

from pastpapers.models import Topic

topics = [
    {'code': '1', 'name': 'States of Matter', 'order': 1},
    {'code': '2', 'name': 'Atoms, Elements and Compounds', 'order': 2},
    {'code': '3', 'name': 'Stoichiometry', 'order': 3},
    {'code': '4', 'name': 'Electrochemistry', 'order': 4},
    {'code': '5', 'name': 'Chemical Energetics', 'order': 5},
    {'code': '6', 'name': 'Chemical Reactions', 'order': 6},
    {'code': '7', 'name': 'Acids, Bases and Salts', 'order': 7},
    {'code': '8', 'name': 'The Periodic Table', 'order': 8},
    {'code': '9', 'name': 'Metals', 'order': 9},
    {'code': '10', 'name': 'Chemistry of the Environment', 'order': 10},
    {'code': '11', 'name': 'Organic Chemistry', 'order': 11},
]

added_count = 0
for topic in topics:
    if not Topic.objects.filter(code=topic['code']).exists():
        Topic.objects.create(**topic)
        print(f"Added: {topic['code']} - {topic['name']}")
        added_count += 1
    else:
        print(f"Skipped (exists): {topic['code']} - {topic['name']}")

print(f"\nDone! Added {added_count} new topics.")