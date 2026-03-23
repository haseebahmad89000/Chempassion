import os
import sys

sys.path.append('C:\\Users\\Dell\\igcse-chemistry-platform')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chemistry_hub.settings')

import django
django.setup()

from pastpapers.models import PastPaper, Topic, Subtopic, Question, Solution

# Get the past paper (you need to find its ID)
# First, let's list all past papers to find the ID
print("Existing Past Papers:")
papers = PastPaper.objects.all()
for paper in papers:
    print(f"ID: {paper.id} - {paper.code}")

# You need to check the ID. Let's assume it's 1 for now
# If it's not, change this number
paper_id = 1

try:
    paper = PastPaper.objects.get(id=paper_id)
    print(f"\nUsing Past Paper: {paper.code}")
except:
    print(f"\nERROR: Past paper with ID {paper_id} not found!")
    print("Check the list above and update paper_id")
    exit()

# Questions data organized by question number
questions_data = []

# Question 1 - States of Matter
q1_parts = [
    ('1a', 'Complete Table 1.1 to describe the structures of solids, liquids and gases in terms of particle separation, particle arrangement and particle motion.',
     3, 'structured', '1', '1.1 Solids, liquids and gases'),
    ('1b', 'Name each physical change: solid to liquid, gas to liquid, solid to aqueous.',
     3, 'structured', '1', '1.1 Solids, liquids and gases'),
    ('1c(i)', 'Describe, in terms of particles, why gases diffuse.',
     1, 'structured', '1', '1.2 Diffusion'),
    ('1c(ii)', 'State what determines the relative rate of diffusion of gases at constant temperature.',
     1, 'structured', '1', '1.2 Diffusion'),
    ('1d', 'State two other adverse effects of oxides of nitrogen (other than acid rain).',
     2, 'structured', '1', '1.2 Diffusion'),
    ('1e(i)', 'Name the toxic gaseous product of the incomplete combustion of hydrocarbon fuels.',
     1, 'structured', '1', '1.2 Diffusion'),
    ('1e(ii)', 'Name the two non-toxic gases formed in the catalytic converter.',
     2, 'structured', '1', '1.2 Diffusion'),
]

# Question 2 - Iron extraction
q2_parts = [
    ('2a(i)', 'State the name of the main iron ore used in the blast furnace.',
     1, 'structured', '2', '2.1 Atomic structure and the Periodic Table'),
    ('2a(ii)', 'State how the main source of heat is provided in the blast furnace.',
     1, 'structured', '2', '2.1 Atomic structure and the Periodic Table'),
    ('2a(iii)', 'Name the gaseous reducing agent in the blast furnace.',
     1, 'structured', '2', '2.1 Atomic structure and the Periodic Table'),
    ('2a(iv)', 'Write a symbol equation for the reduction of iron(III) oxide by carbon monoxide.',
     2, 'structured', '2', '2.1 Atomic structure and the Periodic Table'),
    ('2a(v)', 'Write two symbol equations to show the role of limestone in removing silicon(IV) oxide from iron ore.',
     2, 'structured', '2', '2.1 Atomic structure and the Periodic Table'),
    ('2b', 'Explain why A, B, C and D are isotopes of iron.',
     2, 'structured', '2', '2.1 Atomic structure and the Periodic Table'),
    ('2c(i)', 'Complete table to show protons, neutrons, electrons in Fe2+ and Fe3+ ions.',
     3, 'structured', '2', '2.1 Atomic structure and the Periodic Table'),
    ('2c(ii)', 'Describe a test for aqueous Fe2+ ions.',
     2, 'structured', '2', '2.1 Atomic structure and the Periodic Table'),
    ('2d(i)', 'Define the term oxidising agent.',
     2, 'structured', '2', '2.1 Atomic structure and the Periodic Table'),
    ('2d(ii)', 'Explain why conversion of Fe2+ to Fe3+ is oxidation.',
     1, 'structured', '2', '2.1 Atomic structure and the Periodic Table'),
    ('2d(iii)', 'State one condition needed for oxidation with potassium manganate(VII).',
     1, 'structured', '2', '2.1 Atomic structure and the Periodic Table'),
    ('2e', 'Suggest the identity of the other product formed when iodide reduces Fe3+.',
     1, 'structured', '2', '2.1 Atomic structure and the Periodic Table'),
]

# Question 3 - Salt preparation
q3_parts = [
    ('3a', 'Complete symbol equation for BaCl2 + Na2SO4 reaction. Include state symbols.',
     2, 'structured', '3', '3.1 Formulae'),
    ('3b', 'Calculate the mass of solid BaCl2 dissolved in step 1.',
     2, 'structured', '3', '3.1 Formulae'),
    ('3c', 'Calculate volume of Na2SO4 solution needed containing 0.100 moles.',
     1, 'structured', '3', '3.1 Formulae'),
    ('3d', 'State the colour of the solid formed in step 2.',
     1, 'structured', '3', '3.1 Formulae'),
    ('3e', 'State the general term given to a solid left in the filter paper after filtration.',
     1, 'structured', '3', '3.1 Formulae'),
    ('3f', 'Suggest what student should do between step 3 and 4, and why mass is greater.',
     2, 'structured', '3', '3.1 Formulae'),
    ('3g', 'State the name of this method of salt preparation.',
     1, 'structured', '3', '3.1 Formulae'),
    ('3h', 'Name alternative barium salt, sulfate salt, and insoluble barium salt.',
     3, 'structured', '3', '3.1 Formulae'),
]

# Question 4 - Acids
q4_parts = [
    ('4a(i)', 'State the formula of the common cation produced when acids dissociate in water.',
     1, 'structured', '7', '7.1 The characteristic properties of acids and bases'),
    ('4a(ii)', 'Explain why nitric acid is strong and ethanoic acid is weak.',
     2, 'structured', '7', '7.1 The characteristic properties of acids and bases'),
    ('4a(iii)', 'State which of the three dilute acids will have the highest pH value.',
     1, 'structured', '7', '7.1 The characteristic properties of acids and bases'),
    ('4a(iv)', 'State the colour of thymolphthalein in all three dilute acids.',
     1, 'structured', '7', '7.1 The characteristic properties of acids and bases'),
    ('4a(v)', 'Give formula of anion formed when sulfuric acid and ethanoic acid dissociate.',
     2, 'structured', '7', '7.1 The characteristic properties of acids and bases'),
    ('4a(vi)', 'Name two gaseous products formed during electrolysis of dilute sulfuric acid.',
     2, 'structured', '7', '7.1 The characteristic properties of acids and bases'),
    ('4a(vii)', 'Name the salt formed when calcium reacts with ethanoic acid.',
     1, 'structured', '7', '7.1 The characteristic properties of acids and bases'),
    ('4b(i)', 'Define the term base.',
     1, 'structured', '7', '7.1 The characteristic properties of acids and bases'),
    ('4b(ii)', 'State what this tells you about solubility of Al(OH)3.',
     1, 'structured', '7', '7.1 The characteristic properties of acids and bases'),
    ('4b(iii)', 'Name one other compound which forms aluminium nitrate with dilute nitric acid.',
     1, 'structured', '7', '7.1 The characteristic properties of acids and bases'),
    ('4b(iv)', 'Determine oxidation number of N atoms in Al(NO3)3. Show working.',
     2, 'structured', '7', '7.1 The characteristic properties of acids and bases'),
]

# Question 5 - Alkanes
q5_parts = [
    ('5a', 'Describe two other general characteristics of alkanes.',
     2, 'structured', '11', '11.3 Alkanes'),
    ('5b(i)', 'State trend in boiling points as carbon chain length increases.',
     1, 'structured', '11', '11.3 Alkanes'),
    ('5b(ii)', 'Name another physical property that shows a trend and describe it.',
     2, 'structured', '11', '11.3 Alkanes'),
    ('5c', 'State why alkanes are described as saturated.',
     1, 'structured', '11', '11.3 Alkanes'),
    ('5d(i)', 'State one condition needed for substitution reaction with chlorine.',
     1, 'structured', '11', '11.3 Alkanes'),
    ('5d(ii)', 'Give structural formula and name of two organic products from propane chlorination.',
     4, 'structured', '11', '11.3 Alkanes'),
    ('5d(iii)', 'Define the term structural isomers.',
     1, 'structured', '11', '11.3 Alkanes'),
]

# Question 6 - Esters
q6_parts = [
    ('6a', 'Draw a circle around all atoms which make up the ester linkage.',
     1, 'structured', '11', '11.7 Esters'),
    ('6b', 'Name compound E (ethyl butanoate).',
     1, 'structured', '11', '11.7 Esters'),
    ('6c', 'Deduce the empirical formula of compound E.',
     1, 'structured', '11', '11.7 Esters'),
    ('6d(i)', 'Name the two compounds that react together to produce compound E.',
     2, 'structured', '11', '11.7 Esters'),
    ('6d(ii)', 'Suggest a suitable catalyst for this reaction.',
     1, 'structured', '11', '11.7 Esters'),
    ('6e', 'Determine the number of unbranched esters with molecular formula C5H10O2.',
     1, 'structured', '11', '11.7 Esters'),
    ('6f', 'Write the symbol equation for complete combustion of C5H10O2.',
     1, 'structured', '11', '11.7 Esters'),
]

# Combine all
all_questions = q1_parts + q2_parts + q3_parts + q4_parts + q5_parts + q6_parts

print(f"\n{'='*60}")
print(f"Importing {len(all_questions)} questions from Oct/Nov 2025 Paper 42")
print(f"{'='*60}\n")

added_count = 0
for q_num, q_text, marks, q_type, topic_code, subtopic_name in all_questions:
    try:
        topic = Topic.objects.get(code=topic_code)
        subtopic = Subtopic.objects.get(topic=topic, name=subtopic_name)
        
        question, created = Question.objects.get_or_create(
            paper=paper,
            question_number=q_num,
            defaults={
                'topic': topic,
                'subtopic': subtopic,
                'question_text': q_text,
                'marks': marks,
                'question_type': q_type,
            }
        )
        
        if created:
            print(f"✓ Added: Q{q_num} - {topic_code} {subtopic_name} ({marks} marks)")
            added_count += 1
        else:
            print(f"⊙ Already exists: Q{q_num}")
            
    except Topic.DoesNotExist:
        print(f"✗ ERROR: Topic {topic_code} not found!")
    except Subtopic.DoesNotExist:
        print(f"✗ ERROR: Subtopic '{subtopic_name}' under topic {topic_code} not found!")

print(f"\n{'='*60}")
print(f"Summary: Added {added_count} new questions")
print(f"Total questions in database: {Question.objects.count()}")