from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from .models import Topic, Subtopic, Question, Video, LiveClass, StudentProgress, TopicNote

def home(request):
    topics = Topic.objects.annotate(
        question_count=Count('question')
    ).order_by('order')
    
    context = {
        'topics': topics,
    }
    return render(request, 'pastpapers/home.html', context)

def topics_list(request):
    topics = Topic.objects.annotate(
        question_count=Count('question')
    ).order_by('order')
    return render(request, 'pastpapers/topics.html', {'topics': topics})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    subtopics = topic.subtopics.all().order_by('order')
    for subtopic in subtopics:
        subtopic.question_count = subtopic.question_set.count()
    
    context = {
        'topic': topic,
        'subtopics': subtopics,
    }
    return render(request, 'pastpapers/topic_detail.html', context)

def topic_practice(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    questions = topic.question_set.select_related('solution').all()
    context = {
        'questions': questions,
        'title': f'Topic {topic.code}: {topic.name}',
        'topic_id': topic_id,
    }
    return render(request, 'pastpapers/practice.html', context)

def subtopic_practice(request, subtopic_id):
    subtopic = get_object_or_404(Subtopic, id=subtopic_id)
    questions = subtopic.question_set.select_related('solution').all()
    context = {
        'questions': questions,
        'title': subtopic.name,
        'topic_id': subtopic.topic.id,
    }
    return render(request, 'pastpapers/practice.html', context)

def revision_notes(request):
    """Display revision notes page"""
    topics = Topic.objects.all().order_by('order')
    notes_dict = {}
    for topic in topics:
        try:
            note = TopicNote.objects.get(topic=topic)
            notes_dict[topic.id] = note.content
        except TopicNote.DoesNotExist:
            notes_dict[topic.id] = f"<h2>📖 Notes for {topic.name}</h2><p>Coming soon! Check back later for detailed revision notes.</p>"
    
    context = {
        'topics': topics,
        'notes': notes_dict,
    }
    return render(request, 'pastpapers/revision_notes.html', context)

def subtopic_detail(request, subtopic_id):
    """Display detailed notes for a specific subtopic"""
    subtopic = get_object_or_404(Subtopic, id=subtopic_id)
    topic = subtopic.topic
    
    try:
        note = TopicNote.objects.get(topic=topic)
        content = note.content
    except TopicNote.DoesNotExist:
        content = f"<h2>Notes for {subtopic.name}</h2><p>Coming soon!</p>"
    
    context = {
        'subtopic': subtopic,
        'topic': topic,
        'content': content,
    }
    return render(request, 'pastpapers/subtopic_detail.html', context)

def get_subtopic_content(request, subtopic_id):
    """API endpoint to get subtopic content and syllabus statements"""
    subtopic = get_object_or_404(Subtopic, id=subtopic_id)
    topic = subtopic.topic
    
    # Get the full content from TopicNote
    try:
        note = TopicNote.objects.get(topic=topic)
        full_content = note.content
    except TopicNote.DoesNotExist:
        full_content = f"<h2>Notes for {subtopic.name}</h2><p>Coming soon! Check back later for detailed revision notes.</p>"
    
    # Extract statements based on subtopic name
    statements = []
    
    # Topic 1: States of Matter - 1.1 Solids, liquids and gases
    if "1.1" in subtopic.name or "Solids" in subtopic.name:
        statements = [
            {
                "question": "State the distinguishing properties of solids, liquids and gases",
                "answer": """<table style='width:100%; border-collapse: collapse;'>
                    <tr style='background:#1E3A8A; color:white;'><th>Property</th><th>Solid</th><th>Liquid</th><th>Gas</th></tr>
                    <tr><td>Shape</td><td>Fixed shape</td><td>Takes shape of container</td><td>Takes shape of container</td></tr>
                    <tr style='background:#F9FAFB;'><td>Volume</td><td>Fixed volume</td><td>Fixed volume</td><td>Fills container</td></tr>
                    <tr><td>Compressibility</td><td>Very difficult</td><td>Difficult</td><td>Easy to compress</td></tr>
                    <tr style='background:#F9FAFB;'><td>Flow</td><td>Cannot flow</td><td>Can flow</td><td>Can flow</td></tr>
                    <tr><td>Density</td><td>High</td><td>High</td><td>Low</td></tr>
                </table>"""
            },
            {
                "question": "Describe the structures of solids, liquids and gases in terms of particle separation, arrangement and motion",
                "answer": """<table style='width:100%; border-collapse: collapse;'>
                    <tr style='background:#1E3A8A; color:white;'><th>Property</th><th>Solid</th><th>Liquid</th><th>Gas</th></tr>
                    <tr><td>Particle separation</td><td>Very close (touching)</td><td>Close (touching)</td><td>Far apart</td></tr>
                    <tr style='background:#F9FAFB;'><td>Arrangement</td><td>Regular pattern</td><td>Random</td><td>Random</td></tr>
                    <tr><td>Motion</td><td>Vibrate in fixed positions</td><td>Move around each other</td><td>Move quickly in all directions</td></tr>
                </table>
                <pre>
SOLID:              LIQUID:              GAS:
● ● ● ●             ●  ●                ●        ●
● ● ● ●               ●    ●                      ●
● ● ● ●             ●    ●              ●        ●
(Regular)           (Random)            (Far apart)</pre>"""
            },
            {
                "question": "Describe changes of state in terms of melting, boiling, evaporating, freezing and condensing",
                "answer": """<table style='width:100%; border-collapse: collapse;'>
                    <tr style='background:#1E3A8A; color:white;'><th>Change</th><th>From → To</th><th>Energy</th></tr>
                    <tr><td>Melting</td><td>Solid → Liquid</td><td>Heat absorbed</td></tr>
                    <tr style='background:#F9FAFB;'><td>Freezing</td><td>Liquid → Solid</td><td>Heat released</td></tr>
                    <tr><td>Boiling</td><td>Liquid → Gas</td><td>Heat absorbed</td></tr>
                    <tr style='background:#F9FAFB;'><td>Evaporation</td><td>Liquid → Gas</td><td>Heat absorbed</td></tr>
                    <tr><td>Condensation</td><td>Gas → Liquid</td><td>Heat released</td></tr>
                </table>
                <pre>
     Melting ↑      Boiling/Evaporation ↑
SOLID ──────────► LIQUID ──────────────► GAS
      ←──────────          ←─────────────
     Freezing ↓           Condensation ↓</pre>"""
            },
            {
                "question": "Describe the effects of temperature and pressure on the volume of a gas",
                "answer": """<table style='width:100%; border-collapse: collapse;'>
                    <tr style='background:#1E3A8A; color:white;'><th>Condition</th><th>Effect</th><th>Explanation</th></tr>
                    <tr><td>Temperature ↑</td><td>Volume ↑</td><td>Particles gain kinetic energy, move more, push walls outward</td></tr>
                    <tr style='background:#F9FAFB;'><td>Temperature ↓</td><td>Volume ↓</td><td>Particles lose energy, move less, walls move inward</td></tr>
                    <tr><td>Pressure ↑</td><td>Volume ↓</td><td>Particles forced closer together</td></tr>
                    <tr style='background:#F9FAFB;'><td>Pressure ↓</td><td>Volume ↑</td><td>Particles allowed to spread apart</td></tr>
                </table>
                <div class='warning-box'>⚠️ Particles do NOT expand when heated. They gain energy and move more, taking up more space.</div>"""
            }
        ]
    
    # Topic 1.2: Diffusion
    elif "Diffusion" in subtopic.name:
        statements = [
            {
                "question": "Describe and explain diffusion in terms of kinetic particle theory",
                "answer": """<p><strong>Definition:</strong> Diffusion is the net movement of particles from an area of higher concentration to an area of lower concentration until evenly spread.</p>
                <p><strong>Explanation:</strong> Particles are in constant random motion. They move from areas where there are many particles to areas where there are fewer.</p>
                <p><strong>Examples:</strong> Perfume spreading across a room, food coloring in water, oxygen entering blood in lungs.</p>
                <div class='key-definition'>💡 Diffusion happens without any energy input. Higher temperatures speed up diffusion because particles have more kinetic energy.</div>"""
            },
            {
                "question": "Describe and explain the effect of relative molecular mass on the rate of diffusion of gases <span class='supplement-badge'>Supplement</span>",
                "answer": """<p><strong>Rule:</strong> Gases with lower relative molecular mass (lighter gases) diffuse faster.</p>
                <table style='width:100%; border-collapse: collapse;'>
                    <tr style='background:#1E3A8A; color:white;'><th>Gas</th><th>Mr</th><th>Diffusion Rate</th></tr>
                    <tr><td>Hydrogen (H₂)</td><td>2</td><td>Fastest</td></tr>
                    <tr style='background:#F9FAFB;'><td>Helium (He)</td><td>4</td><td>Very fast</td></tr>
                    <tr><td>Oxygen (O₂)</td><td>32</td><td>Slow</td></tr>
                    <tr style='background:#F9FAFB;'><td>Carbon dioxide (CO₂)</td><td>44</td><td>Very slow</td></tr>
                </table>
                <p><strong>Explanation:</strong> At the same temperature, all gas particles have the same average kinetic energy (KE = ½mv²). Lighter particles must move faster, so they diffuse faster.</p>"""
            }
        ]
    
    # Topic 2.1: Atomic structure
    elif "Atomic" in subtopic.name:
        statements = [
            {
                "question": "Describe the structure of the atom as a central nucleus containing neutrons and protons surrounded by electrons in shells",
                "answer": """<p><strong>Atomic Structure:</strong></p>
                <ul>
                    <li><strong>Nucleus</strong> (centre): Contains protons (+) and neutrons (neutral)</li>
                    <li><strong>Electron shells</strong>: Electrons (-) orbit the nucleus in energy levels (shells)</li>
                </ul>
                <pre>
      Electron shells (energy levels)
            /     \\
           /       \\
          |   ⚫    |  ← Nucleus (protons + neutrons)
           \\       /
            \\     /
             -----</pre>"""
            },
            {
                "question": "State the relative charges and relative masses of a proton, a neutron and an electron",
                "answer": """<table style='width:100%; border-collapse: collapse;'>
                    <tr style='background:#1E3A8A; color:white;'><th>Particle</th><th>Relative Charge</th><th>Relative Mass</th><th>Location</th></tr>
                    <tr><td>Proton</td><td>+1</td><td>1</td><td>Nucleus</td></tr>
                    <tr style='background:#F9FAFB;'><td>Neutron</td><td>0</td><td>1</td><td>Nucleus</td></tr>
                    <tr><td>Electron</td><td>-1</td><td>1/1840 (negligible)</td><td>Electron shells</td></tr>
                </table>"""
            },
            {
                "question": "Define proton number/atomic number as the number of protons in the nucleus of an atom",
                "answer": """<p><strong>Atomic Number (Z)</strong> = Number of protons in the nucleus</p>
                <p>In a neutral atom, the number of protons = number of electrons</p>
                <div class='key-definition'>💡 Example: Carbon has atomic number 6 → 6 protons, 6 electrons</div>"""
            },
            {
                "question": "Define mass number/nucleon number as the total number of protons and neutrons in the nucleus of an atom",
                "answer": """<p><strong>Mass Number (A)</strong> = Number of protons + number of neutrons</p>
                <p><strong>Number of neutrons</strong> = Mass number - Atomic number</p>
                <div class='key-definition'>💡 Example: Carbon-12 → 12 - 6 = 6 neutrons</div>"""
            },
            {
                "question": "Determine the electronic configuration of elements and their ions with proton number 1 to 20",
                "answer": """<table style='width:100%; border-collapse: collapse;'>
                    <tr style='background:#1E3A8A; color:white;'><th>Element</th><th>Atomic Number</th><th>Electronic Configuration</th></tr>
                    <tr><td>Hydrogen</td><td>1</td><td>1</td></tr>
                    <tr style='background:#F9FAFB;'><td>Helium</td><td>2</td><td>2</td></tr>
                    <tr><td>Lithium</td><td>3</td><td>2,1</td></tr>
                    <tr style='background:#F9FAFB;'><td>Beryllium</td><td>4</td><td>2,2</td></tr>
                    <tr><td>Boron</td><td>5</td><td>2,3</td></tr>
                    <tr style='background:#F9FAFB;'><td>Carbon</td><td>6</td><td>2,4</td></tr>
                    <tr><td>Nitrogen</td><td>7</td><td>2,5</td></tr>
                    <tr style='background:#F9FAFB;'><td>Oxygen</td><td>8</td><td>2,6</td></tr>
                    <tr><td>Fluorine</td><td>9</td><td>2,7</td></tr>
                    <tr style='background:#F9FAFB;'><td>Neon</td><td>10</td><td>2,8</td></tr>
                    <tr><td>Sodium</td><td>11</td><td>2,8,1</td></tr>
                    <tr style='background:#F9FAFB;'><td>Magnesium</td><td>12</td><td>2,8,2</td></tr>
                    <tr><td>Aluminium</td><td>13</td><td>2,8,3</td></tr>
                    <tr style='background:#F9FAFB;'><td>Silicon</td><td>14</td><td>2,8,4</td></tr>
                    <tr><td>Phosphorus</td><td>15</td><td>2,8,5</td></tr>
                    <tr style='background:#F9FAFB;'><td>Sulfur</td><td>16</td><td>2,8,6</td></tr>
                    <tr><td>Chlorine</td><td>17</td><td>2,8,7</td></tr>
                    <tr style='background:#F9FAFB;'><td>Argon</td><td>18</td><td>2,8,8</td></tr>
                    <tr><td>Potassium</td><td>19</td><td>2,8,8,1</td></tr>
                    <tr style='background:#F9FAFB;'><td>Calcium</td><td>20</td><td>2,8,8,2</td></tr>
                </table>
                <div class='key-definition'>💡 <strong>Shell Rules:</strong> 1st shell = max 2 electrons, 2nd shell = max 8 electrons, 3rd shell = max 8 electrons (simplified model)</div>"""
            },
            {
                "question": "State that Group VIII noble gases have a full outer electron shell; the number of outer shell electrons equals the group number; the number of occupied electron shells equals the period number",
                "answer": """<p><strong>Relationship to Periodic Table:</strong></p>
                <ul>
                    <li><strong>Period number</strong> = Number of occupied electron shells</li>
                    <li><strong>Group number (I-VII)</strong> = Number of electrons in the outer shell</li>
                    <li><strong>Group VIII (Noble gases)</strong> = Full outer shell (stable, unreactive)</li>
                </ul>
                <div class='key-definition'>💡 Example: Sodium (Period 3, Group 1) → 3 shells, 1 outer electron → 2,8,1</div>"""
            }
        ]
    
    # Topic 2.2: Ions and ionic bonds
    elif "Ions" in subtopic.name and "Ionic" in subtopic.name:
        statements = [
            {
                "question": "Describe the formation of positive ions (cations) and negative ions (anions)",
                "answer": """<p><strong>Cations (positive ions):</strong> Metals <strong>lose electrons</strong> to achieve a full outer shell</p>
                <ul><li>Example: Na → Na⁺ + e⁻ (sodium loses 1 electron)</li></ul>
                <p><strong>Anions (negative ions):</strong> Non-metals <strong>gain electrons</strong> to achieve a full outer shell</p>
                <ul><li>Example: Cl + e⁻ → Cl⁻ (chlorine gains 1 electron)</li></ul>
                <div class='key-definition'>💡 Group 1 metals form 1⁺ ions, Group 2 form 2⁺, Group 6 form 2⁻, Group 7 form 1⁻</div>"""
            },
            {
                "question": "State that an ionic bond is a strong electrostatic attraction between oppositely charged ions",
                "answer": """<p>An ionic bond is the <strong>strong electrostatic attraction</strong> between oppositely charged ions.</p>
                <p>Forms when a metal reacts with a non-metal.</p>"""
            },
            {
                "question": "Describe the formation of ionic bonds between Group I and Group VII using dot-and-cross diagrams",
                "answer": """<p><strong>Sodium Chloride (NaCl)</strong></p>
                <pre>
Na atom: 2,8,1          Cl atom: 2,8,7
         ↓                    ↓
Na⁺ ion: 2,8           Cl⁻ ion: 2,8,8

[Na]⁺   [ Cl ]⁻
        ••
        ••</pre>
                <div class='key-definition'>💡 Group I metals lose 1 electron → +1 charge. Group VII non-metals gain 1 electron → -1 charge.</div>"""
            },
            {
                "question": "Describe the properties of ionic compounds: high melting/boiling points; good conductivity when aqueous or molten, poor when solid",
                "answer": """<table style='width:100%; border-collapse: collapse;'>
                    <tr style='background:#1E3A8A; color:white;'><th>Property</th><th>Explanation</th></tr>
                    <tr><td>High melting/boiling points</td><td>Strong electrostatic forces between ions require lots of energy to overcome</td></tr>
                    <tr style='background:#F9FAFB;'><td>Conducts when molten/dissolved</td><td>Ions are free to move and carry charge</td></tr>
                    <tr><td>Poor conductor when solid</td><td>Ions are fixed in position in the lattice</td></tr>
                    <tr style='background:#F9FAFB;'><td>Hard but brittle</td><td>Layers shift, like charges align and repel</td></tr>
                </table>"""
            },
            {
                "question": "Describe the giant lattice structure of ionic compounds <span class='supplement-badge'>Supplement</span>",
                "answer": """<p><strong>Giant Lattice Structure:</strong> Ions are arranged in a regular, repeating 3D pattern with alternating positive and negative ions.</p>
                <pre>
    +   -   +   -
   -   +   -   +
    +   -   +   -
   -   +   -   +
(Alternating positive and negative ions)</pre>"""
            },
            {
                "question": "Explain the properties of ionic compounds in terms of structure and bonding <span class='supplement-badge'>Supplement</span>",
                "answer": """<ul>
                    <li><strong>High melting/boiling points:</strong> Strong electrostatic forces between oppositely charged ions in all directions require large amounts of energy to overcome.</li>
                    <li><strong>Conductivity when molten/dissolved:</strong> Ions become free to move and can carry electric charge.</li>
                    <li><strong>No conductivity when solid:</strong> Ions are fixed in lattice positions and cannot move.</li>
                    <li><strong>Brittleness:</strong> When layers shift, like charges align and repel, causing the crystal to split.</li>
                </ul>"""
            }
        ]
    
    # Topic 2.3: Simple molecules and covalent bonds
    elif "Covalent" in subtopic.name or "Simple Molecules" in subtopic.name:
        statements = [
            {
                "question": "State that a covalent bond is formed when a pair of electrons is shared between two atoms",
                "answer": """<p><strong>Covalent Bond:</strong> Formed when a <strong>pair of electrons is shared</strong> between two non-metal atoms.</p>
                <p>Each atom contributes one electron to the shared pair, and both atoms achieve a full outer shell (noble gas configuration).</p>"""
            },
            {
                "question": "Describe the formation of covalent bonds in simple molecules using dot-and-cross diagrams",
                "answer": """<pre>
H₂:      H• + •H → H:H
Cl₂:     Cl•• + ••Cl → Cl:Cl (with 6 other electrons each)
H₂O:     H:O:H (O shares 2 pairs)
CH₄:     H:C:H with H above and below (C shares 4 pairs)
NH₃:     H:N:H with lone pair on N (N shares 3 pairs)
HCl:     H:Cl (H shares 1 pair)</pre>
                <div class='key-definition'>💡 Only outer shell electrons are shown in dot-and-cross diagrams.</div>"""
            },
            {
                "question": "Describe the properties of simple molecular compounds: low melting/boiling points; poor electrical conductivity",
                "answer": """<table style='width:100%; border-collapse: collapse;'>
                    <tr style='background:#1E3A8A; color:white;'><th>Property</th><th>Explanation</th></tr>
                    <tr><td>Low melting/boiling points</td><td>Weak intermolecular forces between molecules (not the strong covalent bonds inside molecules)</td></tr>
                    <tr style='background:#F9FAFB;'><td>Poor electrical conductivity</td><td>No free electrons or ions to carry charge</td></tr>
                    <tr><td>Often gases or liquids at room temperature</td><td>Weak forces mean they evaporate easily</td></tr>
                </table>"""
            },
            {
                "question": "Describe the formation of covalent bonds in additional molecules (O₂, N₂, CO₂, C₂H₄, CH₃OH) <span class='supplement-badge'>Supplement</span>",
                "answer": """<pre>
O₂:      O::O (double bond)
N₂:      N:::N (triple bond)
CO₂:     O::C::O (double bonds)
C₂H₄:    H₂C=CH₂ (double bond between C)
CH₃OH:   H
         |
    H—C—O—H
         |
         H</pre>"""
            },
            {
                "question": "Explain the properties of simple molecular compounds in terms of structure and bonding <span class='supplement-badge'>Supplement</span>",
                "answer": """<p><strong>Key Concept:</strong></p>
                <ul>
                    <li><strong>Intramolecular forces</strong> (covalent bonds) = strong, hold atoms together within a molecule</li>
                    <li><strong>Intermolecular forces</strong> = weak, hold molecules together</li>
                    <li>Low melting/boiling points because only weak intermolecular forces need to be overcome</li>
                    <li>Poor conductivity because no free electrons or ions are present</li>
                </ul>"""
            }
        ]
    
    # Topic 2.4: Giant covalent structures
    elif "Giant" in subtopic.name:
        statements = [
            {
                "question": "Describe the giant covalent structures of graphite and diamond",
                "answer": """<p><strong>Diamond:</strong> Each carbon atom bonded to 4 others (tetrahedral) - all strong covalent bonds</p>
                <p><strong>Graphite:</strong> Each carbon bonded to 3 others, forming layers of hexagons. Strong covalent bonds within layers; weak intermolecular forces between layers. One free electron per carbon atom becomes delocalised.</p>"""
            },
            {
                "question": "Relate the structures and bonding of graphite and diamond to their uses",
                "answer": """<table style='width:100%; border-collapse: collapse;'>
                    <tr style='background:#1E3A8A; color:white;'><th>Property</th><th>Diamond</th><th>Graphite</th></tr>
                    <tr><td>Bonding</td><td>4 covalent bonds per carbon</td><td>3 covalent bonds per carbon</td></tr>
                    <tr style='background:#F9FAFB;'><td>Structure</td><td>3D tetrahedral</td><td>Layered hexagonal</td></tr>
                    <tr><td>Hardness</td><td>Very hard (hardest natural substance)</td><td>Soft, slippery</td></tr>
                    <tr style='background:#F9FAFB;'><td>Conductivity</td><td>Non-conductor (no free electrons)</td><td>Conductor (delocalised electrons)</td></tr>
                    <tr><td>Uses</td><td>Cutting tools, drills, jewellery</td><td>Pencil lead, lubricant, electrodes</td></tr>
                </table>"""
            }
        ]
    
    # Topic 2.5: Metallic bonding
    elif "Metallic" in subtopic.name:
        statements = [
            {
                "question": "Describe metallic bonding as the electrostatic attraction between positive ions and a 'sea' of delocalised electrons <span class='supplement-badge'>Supplement</span>",
                "answer": """<p><strong>Metallic Bonding:</strong></p>
                <ul>
                    <li>Metal atoms lose their outer electrons to become positive ions</li>
                    <li>These electrons become <strong>delocalised</strong> (free to move) forming a "sea of electrons"</li>
                    <li>The metallic bond is the <strong>electrostatic attraction</strong> between positive metal ions and the delocalised electrons</li>
                </ul>
                <pre>
Metal lattice:   +   +   +   +
                 +   +   +   +   (with sea of electrons around)
                 +   +   +   +</pre>"""
            },
            {
                "question": "Explain the properties of metals: good electrical conductivity; malleability and ductility <span class='supplement-badge'>Supplement</span>",
                "answer": """<table style='width:100%; border-collapse: collapse;'>
                    <tr style='background:#1E3A8A; color:white;'><th>Property</th><th>Explanation</th></tr>
                    <tr><td>Good electrical conductivity</td><td>Delocalised electrons are free to move and carry charge</td></tr>
                    <tr style='background:#F9FAFB;'><td>Good thermal conductivity</td><td>Delocalised electrons transfer kinetic energy quickly</td></tr>
                    <tr><td>High melting/boiling points</td><td>Strong electrostatic forces between ions and electrons require lots of energy to overcome</td></tr>
                    <tr style='background:#F9FAFB;'><td>Malleable (can be hammered into shape)</td><td>Layers of positive ions can slide over each other without breaking the metallic bond</td></tr>
                    <tr><td>Ductile (can be drawn into wires)</td><td>Same reason as malleability - layers can slide</td></tr>
                </table>"""
            }
        ]
    
    # Topic 3: Stoichiometry
    elif "Stoichiometry" in topic.name or "Mole" in subtopic.name:
        statements = [
            {
                "question": "Define the mole and Avogadro constant <span class='supplement-badge'>Supplement</span>",
                "answer": """<p><strong>Mole:</strong> The unit for amount of substance. 1 mole = 6.02 × 10²³ particles (Avogadro constant)</p>
                <p>1 mole of any element = its relative atomic mass in grams</p>
                <p><strong>Formula:</strong> Moles = Mass (g) / Molar Mass (g/mol)</p>"""
            },
            {
                "question": "Calculate reacting masses, concentrations, and volumes of gases <span class='supplement-badge'>Supplement</span>",
                "answer": """<p><strong>Molar Gas Volume:</strong> 1 mole of any gas at r.t.p. occupies 24 dm³</p>
                <p><strong>Concentration:</strong> mol/dm³ = Moles / Volume (dm³)</p>
                <p><strong>Worked Example:</strong> 80g NaOH in 500 cm³ water</p>
                <ul><li>Moles = 80/40 = 2 mol</li><li>Volume = 500/1000 = 0.5 dm³</li><li>Concentration = 2/0.5 = 4 mol/dm³</li></ul>"""
            }
        ]
    
    # Topic 4: Electrochemistry
    elif "Electrochemistry" in topic.name or "Electrolysis" in subtopic.name:
        statements = [
            {
                "question": "Define electrolysis and identify the key components",
                "answer": """<p><strong>Electrolysis:</strong> Decomposition of an ionic compound when molten or in aqueous solution by an electric current.</p>
                <ul><li><strong>Anode (+):</strong> Positive electrode, attracts anions</li><li><strong>Cathode (−):</strong> Negative electrode, attracts cations</li><li><strong>Electrolyte:</strong> Ionic compound that conducts electricity when molten or dissolved</li></ul>"""
            },
            {
                "question": "Predict products during electrolysis of molten compounds",
                "answer": """<p><strong>Molten Lead(II) Bromide:</strong></p>
                <ul><li>Cathode: Pb²⁺ + 2e⁻ → Pb (grey metal)</li><li>Anode: 2Br⁻ → Br₂ + 2e⁻ (brown bromine gas)</li></ul>
                <p><strong>Molten Sodium Chloride:</strong></p>
                <ul><li>Cathode: Na⁺ + e⁻ → Na (sodium metal)</li><li>Anode: 2Cl⁻ → Cl₂ + 2e⁻ (chlorine gas)</li></ul>"""
            },
            {
                "question": "Explain the products during electrolysis of aqueous solutions",
                "answer": """<p><strong>Concentrated Sodium Chloride (Brine):</strong></p>
                <ul><li>Cathode: 2H⁺ + 2e⁻ → H₂ (hydrogen gas)</li><li>Anode: 2Cl⁻ → Cl₂ + 2e⁻ (chlorine gas)</li><li>Remaining: NaOH solution</li></ul>
                <p><strong>Dilute Sulfuric Acid:</strong></p>
                <ul><li>Cathode: 2H⁺ + 2e⁻ → H₂</li><li>Anode: 4OH⁻ → O₂ + 2H₂O + 4e⁻</li></ul>"""
            }
        ]
    
    # Fallback for any subtopic
    if not statements:
        statements = [
            {
                "question": "Syllabus content for this subtopic",
                "answer": "<p>Detailed revision notes for this subtopic will be added soon. Check back later!</p>"
            }
        ]
    
    return JsonResponse({
        'content': full_content,
        'statements': statements,
        'subtopic_name': subtopic.name,
        'topic_name': topic.name
    })

def flashcards(request):
    topics = Topic.objects.all().order_by('order')
    return render(request, 'pastpapers/flashcards.html', {'topics': topics})

def exam_questions(request):
    topics = Topic.objects.all().order_by('order')
    return render(request, 'pastpapers/exam_questions.html', {'topics': topics})

def past_papers(request):
    return render(request, 'pastpapers/past_papers.html')

def mock_exams(request):
    return render(request, 'pastpapers/mock_exams.html')

def target_test(request):
    return render(request, 'pastpapers/target_test.html')

def strengths_weaknesses(request):
    if not request.user.is_authenticated:
        return redirect('login')
    progress = StudentProgress.objects.filter(user=request.user)
    weak_topics = []
    topics = Topic.objects.all()
    for topic in topics:
        topic_progress = progress.filter(question__topic=topic)
        attempted = topic_progress.count()
        if attempted > 0:
            correct = topic_progress.filter(is_correct=True).count()
            weak_topics.append({
                'topic': topic,
                'accuracy': (correct / attempted * 100),
                'attempted': attempted,
                'correct': correct
            })
    return render(request, 'pastpapers/strengths_weaknesses.html', {'weak_topics': weak_topics})

def live_classes(request):
    all_classes = LiveClass.objects.all().order_by('-date')
    upcoming = LiveClass.objects.filter(is_upcoming=True, date__gte=datetime.now()).order_by('date')
    context = {
        'live_classes': all_classes,
        'upcoming': upcoming,
    }
    return render(request, 'pastpapers/live_classes.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'pastpapers/register.html', {'form': form})

@login_required
def dashboard(request):
    progress = StudentProgress.objects.filter(user=request.user)
    total_attempted = progress.count()
    correct_count = progress.filter(is_correct=True).count()
    accuracy = (correct_count / total_attempted * 100) if total_attempted > 0 else 0
    
    weak_topics = []
    topics = Topic.objects.all()
    for topic in topics:
        topic_progress = progress.filter(question__topic=topic)
        attempted = topic_progress.count()
        if attempted > 0:
            correct = topic_progress.filter(is_correct=True).count()
            if (correct / attempted) < 0.5:
                weak_topics.append({
                    'topic': topic,
                    'accuracy': (correct / attempted * 100),
                    'attempted': attempted
                })
    
    context = {
        'total_attempted': total_attempted,
        'correct_count': correct_count,
        'accuracy': round(accuracy, 1),
        'weak_topics': weak_topics,
        'recent_activity': progress.order_by('-attempted_at')[:10],
    }
    return render(request, 'pastpapers/dashboard.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        return redirect('profile')
    return render(request, 'pastpapers/profile.html', {'user': request.user})

@login_required
@csrf_exempt
def save_progress(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question_id = data.get('question_id')
        is_correct = data.get('is_correct')
        answer_given = data.get('answer_given')
        
        question = get_object_or_404(Question, id=question_id)
        
        progress, created = StudentProgress.objects.update_or_create(
            user=request.user,
            question=question,
            defaults={
                'is_attempted': True,
                'is_correct': is_correct,
                'answer_given': answer_given,
            }
        )
        
        return JsonResponse({'status': 'saved'})
    return JsonResponse({'error': 'Invalid request'}, status=400)