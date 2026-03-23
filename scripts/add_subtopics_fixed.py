import os
import sys

sys.path.append('C:\\Users\\Dell\\igcse-chemistry-platform')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chemistry_hub.settings')

import django
django.setup()

from pastpapers.models import Topic, Subtopic

subtopics_data = [
    # Topic 1
    ('1', '1.1 Solids, liquids and gases', 1),
    ('1', '1.2 Diffusion', 2),
    
    # Topic 2
    ('2', '2.1 Atomic structure and the Periodic Table', 1),
    ('2', '2.2 Ions and ionic bonds', 2),
    ('2', '2.3 Molecules and covalent bonds', 3),
    ('2', '2.4 Metallic bonds', 4),
    ('2', '2.5 Giant covalent structures', 5),
    
    # Topic 3
    ('3', '3.1 Formulae', 1),
    ('3', '3.2 The mole concept', 2),
    ('3', '3.3 Calculations involving masses', 3),
    ('3', '3.4 Calculations involving volumes', 4),
    
    # Topic 4
    ('4', '4.1 Electrolysis', 1),
    
    # Topic 5
    ('5', '5.1 Exothermic and endothermic reactions', 1),
    ('5', '5.2 Bond energy calculations', 2),
    
    # Topic 6
    ('6', '6.1 Rates of reaction', 1),
    ('6', '6.2 Reversible reactions and equilibrium', 2),
    ('6', '6.3 Redox', 3),
    
    # Topic 7
    ('7', '7.1 The characteristic properties of acids and bases', 1),
    ('7', '7.2 Oxides', 2),
    ('7', '7.3 Preparation of salts', 3),
    ('7', '7.4 Identification of ions and gases', 4),
    
    # Topic 8
    ('8', '8.1 Arrangement of elements', 1),
    ('8', '8.2 Group I properties', 2),
    ('8', '8.3 Group VII properties', 3),
    ('8', '8.4 Transition elements', 4),
    ('8', '8.5 Noble gases', 5),
    
    # Topic 9
    ('9', '9.1 Properties of metals', 1),
    ('9', '9.2 Reactivity series', 2),
    ('9', '9.3 Extraction of metals', 3),
    ('9', '9.4 Uses of metals', 4),
    
    # Topic 10
    ('10', '10.1 Water', 1),
    ('10', '10.2 Air quality and climate', 2),
    ('10', '10.3 Nitrogen and sulfur cycles', 3),
    ('10', '10.4 Carbon footprint', 4),
    
    # Topic 11
    ('11', '11.1 Names and formulae of organic compounds', 1),
    ('11', '11.2 Fuels', 2),
    ('11', '11.3 Alkanes', 3),
    ('11', '11.4 Alkenes', 4),
    ('11', '11.5 Alcohols', 5),
    ('11', '11.6 Carboxylic acids', 6),
    ('11', '11.7 Esters', 7),
    ('11', '11.8 Polymers', 8),
]

added = 0
exists = 0

for topic_code, name, order in subtopics_data:
    try:
        topic = Topic.objects.get(code=topic_code)
        obj, created = Subtopic.objects.get_or_create(
            topic=topic,
            name=name,
            defaults={'order': order}
        )
        if created:
            print(f"✓ Added: {topic_code} - {name}")
            added += 1
        else:
            print(f"⊙ Already exists: {topic_code} - {name}")
            exists += 1
    except Topic.DoesNotExist:
        print(f"✗ ERROR: Topic {topic_code} not found!")

print(f"\n========== SUMMARY ==========")
print(f"New subtopics added: {added}")
print(f"Already existed: {exists}")
print(f"Total in database: {Subtopic.objects.count()}")