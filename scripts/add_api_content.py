import os
import sys
import django

sys.path.append('C:\\Users\\Dell\\igcse-chemistry-platform')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chemistry_hub.settings')
django.setup()

from pastpapers.models import Subtopic

# Content for each subtopic (simplified for now)
subtopic_content = {
    # Topic 1 - States of Matter
    32: {
        "statements": [
            {"question": "State the distinguishing properties of solids, liquids and gases", 
             "answer": "<p><strong>Solids:</strong> Fixed shape and volume, cannot flow, very dense<br><strong>Liquids:</strong> Takes shape of container, fixed volume, can flow, dense<br><strong>Gases:</strong> Takes shape of container, fills container, can flow, low density</p>"},
            {"question": "Describe the structures of solids, liquids and gases in terms of particle separation, arrangement and motion",
             "answer": "<p><strong>Solids:</strong> Particles close (touching), regular pattern, vibrate in fixed positions<br><strong>Liquids:</strong> Particles close, random arrangement, move around each other<br><strong>Gases:</strong> Particles far apart, random arrangement, move quickly in all directions</p>"},
        ]
    },
    33: {
        "statements": [
            {"question": "Describe and explain diffusion in terms of kinetic particle theory",
             "answer": "<p><strong>Diffusion:</strong> Movement of particles from high concentration to low concentration. Particles are in constant random motion, they spread out until evenly distributed.</p>"},
            {"question": "Describe and explain the effect of relative molecular mass on the rate of diffusion of gases",
             "answer": "<p><strong>Rule:</strong> Lighter gases (lower Mr) diffuse faster because at same temperature, all particles have same kinetic energy (KE=½mv²). Lighter particles move faster.</p>"},
        ]
    },
}

# Store content in a JSON file that the API can read
import json

content_file = 'pastpapers/subtopic_content.json'
with open(content_file, 'w') as f:
    json.dump(subtopic_content, f, indent=2)

print(f"✅ Created {content_file} with content for {len(subtopic_content)} subtopics")
print("Now update the API endpoint to read from this file")