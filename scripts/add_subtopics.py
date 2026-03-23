import os
import sys

sys.path.append('C:\\Users\\Dell\\igcse-chemistry-platform')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chemistry_hub.settings')

import django
django.setup()

from pastpapers.models import Topic, Subtopic

# Define all subtopics
subtopics_data = [
    # Topic 1: States of Matter
    {'topic_code': '1', 'name': '1.1 Solids, liquids and gases', 'order': 1},
    {'topic_code': '1', 'name': '1.2 Diffusion', 'order': 2},
    
    # Topic 2: Atoms, Elements and Compounds
    {'topic_code': '2', 'name': '2.1 Atomic structure', 'order': 1},
    {'topic_code': '2', 'name': '2.2 Ionic bonding', 'order': 2},
    {'topic_code': '2', 'name': '2.3 Covalent bonding', 'order': 3},
    {'topic_code': '2', 'name': '2.4 Metallic bonding', 'order': 4},
    
    # Topic 3: Stoichiometry
    {'topic_code': '3', 'name': '3.1 Formulae', 'order': 1},
    {'topic_code': '3', 'name': '3.2 The mole concept', 'order': 2},
    {'topic_code': '3', 'name': '3.3 Calculations from equations', 'order': 3},
    
    # Topic 4: Electrochemistry
    {'topic_code': '4', 'name': '4.1 Electrolysis', 'order': 1},
    
    # Topic 5: Chemical Energetics
    {'topic_code': '5', 'name': '5.1 Exothermic and endothermic reactions', 'order': 1},
    
    # Topic 6: Chemical Reactions
    {'topic_code': '6', 'name': '6.1 Rates of reaction', 'order': 1},
    {'topic_code': '6', 'name': '6.2 Reversible reactions', 'order': 2},
    {'topic_code': '6', 'name': '6.3 Redox', 'order': 3},
    
    # Topic 7: Acids, Bases and Salts
    {'topic_code': '7', 'name': '7.1 Acids and bases', 'order': 1},
    {'topic_code': '7', 'name': '7.2 Preparation of salts', 'order': 2},
    
    # Topic 8: The Periodic Table
    {'topic_code': '8', 'name': '8.1 Group I (Alkali metals)', 'order': 1},
    {'topic_code': '8', 'name': '8.2 Group VII (Halogens)', 'order': 2},
    {'topic_code': '8', 'name': '8.3 Transition elements', 'order': 3},
    {'topic_code': '8', 'name': '8.4 Noble gases', 'order': 4},
    
    # Topic 9: Metals
    {'topic_code': '9', 'name': '9.1 Properties of metals', 'order': 1},
    {'topic_code': '9', 'name': '9.2 Reactivity series', 'order': 2},
    {'topic_code': '9', 'name': '9.3 Extraction of metals', 'order': 3},
    
    # Topic 10: Chemistry of the Environment
    {'topic_code': '10', 'name': '10.1 Water', 'order': 1},
    {'topic_code': '10', 'name': '10.2 Air', 'order': 2},
    {'topic_code': '10', 'name': '10.3 Pollution', 'order': 3},
    
    # Topic 11: Organic Chemistry
    {'topic_code': '11', 'name': '11.1 Alkanes', 'order': 1},
    {'topic_code': '11', 'name': '11.2 Alkenes', 'order': 2},
    {'topic_code': '11', 'name': '11.3 Alcohols', 'order': 3},
    {'topic_code': '11', 'name': '11.4 Carboxylic acids', 'order': 4},
    {'topic_code': '11', 'name': '11.5 Polymers', 'order': 5},
]

added_count = 0
skipped_count = 0

for data in subtopics_data:
    try:
        topic = Topic.objects.get(code=data['topic_code'])
        subtopic, created = Subtopic.objects.get_or_create(
            topic=topic,
            name=data['name'],
            defaults={'order': data['order']}
        )
        if created:
            print(f"✓ Added: {data['topic_code']} - {data['name']}")
            added_count += 1
        else:
            print(f"⊙ Skipped (exists): {data['topic_code']} - {data['name']}")
            skipped_count += 1
    except Topic.DoesNotExist:
        print(f"✗ Error: Topic {data['topic_code']} not found!")
        
print(f"\nDone! Added {added_count} new subtopics. Skipped {skipped_count} existing.")