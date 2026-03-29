import os
import sys
import django

sys.path.append('C:\\Users\\Dell\\igcse-chemistry-platform')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chemistry_hub.settings')
django.setup()

from pastpapers.models import Topic, Subtopic

print("=== ALL TOPICS AND SUBTOPICS ===\n")

for topic in Topic.objects.all().order_by('code'):
    print(f"Topic {topic.code}: {topic.name}")
    subtopics = topic.subtopics.all().order_by('order')
    if subtopics:
        for sub in subtopics:
            print(f"  - ID:{sub.id} | {sub.name}")
    else:
        print("  - NO SUBTOPICS FOUND")
    print()

print(f"Total topics: {Topic.objects.count()}")
print(f"Total subtopics: {Subtopic.objects.count()}")