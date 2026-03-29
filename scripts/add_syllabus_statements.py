import os
import sys
import django

sys.path.append('C:\\Users\\Dell\\igcse-chemistry-platform')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chemistry_hub.settings')
django.setup()

from pastpapers.models import Topic, TopicNote

# Topic 1: States of Matter
topic1_content = """
<div class="main-heading">📌 Topic 1: States of Matter</div>

<div class="sub-heading">1.1 Solids, liquids and gases</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> State the distinguishing properties of solids, liquids and gases</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">2</span> Describe the structures of solids, liquids and gases in terms of particle separation, arrangement and motion</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">3</span> Describe changes of state in terms of melting, boiling, evaporating, freezing and condensing</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">4</span> Describe the effects of temperature and pressure on the volume of a gas</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">5</span> Explain changes of state in terms of kinetic particle theory, including the interpretation of heating and cooling curves <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">6</span> Explain, in terms of kinetic particle theory, the effects of temperature and pressure on the volume of a gas <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="sub-heading">1.2 Diffusion</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> Describe and explain diffusion in terms of kinetic particle theory</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">2</span> Describe and explain the effect of relative molecular mass on the rate of diffusion of gases <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>
"""

# Topic 2: Atoms, elements and compounds
topic2_content = """
<div class="main-heading">📌 Topic 2: Atoms, elements and compounds</div>

<div class="sub-heading">2.1 Elements, compounds and mixtures</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> Describe the differences between elements, compounds and mixtures</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="sub-heading">2.2 Atomic structure and the Periodic Table</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> Describe the structure of the atom as a central nucleus containing neutrons and protons surrounded by electrons in shells</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">2</span> State the relative charges and relative masses of a proton, a neutron and an electron</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">3</span> Define proton number/atomic number as the number of protons in the nucleus of an atom</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">4</span> Define mass number/nucleon number as the total number of protons and neutrons in the nucleus of an atom</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">5</span> Determine the electronic configuration of elements and their ions with proton number 1 to 20</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">6</span> State that Group VIII noble gases have a full outer electron shell; the number of outer shell electrons equals the group number; the number of occupied electron shells equals the period number</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="sub-heading">2.3 Isotopes</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> Define isotopes as different atoms of the same element that have the same number of protons but different numbers of neutrons</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">2</span> Interpret and use symbols for atoms and ions</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">3</span> State that isotopes of the same element have the same chemical properties because they have the same number of electrons <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">4</span> Calculate the relative atomic mass of an element from the relative masses and abundances of its isotopes <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="sub-heading">2.4 Ions and ionic bonds</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> Describe the formation of positive ions (cations) and negative ions (anions)</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">2</span> State that an ionic bond is a strong electrostatic attraction between oppositely charged ions</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">3</span> Describe the formation of ionic bonds between elements from Group I and Group VII, using dot-and-cross diagrams</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">4</span> Describe the properties of ionic compounds: high melting/boiling points; good conductivity when aqueous or molten, poor when solid</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">5</span> Describe the giant lattice structure of ionic compounds <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">6</span> Explain in terms of structure and bonding the properties of ionic compounds <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="sub-heading">2.5 Simple molecules and covalent bonds</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> State that a covalent bond is formed when a pair of electrons is shared between two atoms</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">2</span> Describe the formation of covalent bonds in simple molecules (H₂, Cl₂, H₂O, CH₄, NH₃, HCl) using dot-and-cross diagrams</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">3</span> Describe the properties of simple molecular compounds: low melting/boiling points; poor electrical conductivity</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="sub-heading">2.6 Giant covalent structures</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> Describe the giant covalent structures of graphite and diamond</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">2</span> Relate the structures and bonding of graphite and diamond to their uses</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="sub-heading">2.7 Metallic bonding</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> Describe metallic bonding as the electrostatic attraction between positive ions and a 'sea' of delocalised electrons</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">2</span> Explain the properties of metals: good electrical conductivity; malleability and ductility</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><em>Answer coming soon...</em></p>
        </div>
    </div>
</div>
"""

# Continue for Topics 3-11...

print("=" * 60)
print("Adding syllabus statements for Topic 1 and Topic 2...")
print("=" * 60)

# Add Topic 1
topic1 = Topic.objects.get(code='1')
note1, created1 = TopicNote.objects.update_or_create(
    topic=topic1,
    defaults={'content': topic1_content}
)
print(f"✅ Added {len(topic1_content.split('point-item'))-1} statements for Topic 1: States of Matter")

# Add Topic 2
topic2 = Topic.objects.get(code='2')
note2, created2 = TopicNote.objects.update_or_create(
    topic=topic2,
    defaults={'content': topic2_content}
)
print(f"✅ Added statements for Topic 2: Atoms, elements and compounds")

print("\n✨ Done! Statements added. Answers will be added later.")
print("🔗 View at: https://chempassion.info/revision-notes/")