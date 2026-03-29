import os
import sys
import django

sys.path.append('C:\\Users\\Dell\\igcse-chemistry-platform')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chemistry_hub.settings')
django.setup()

from pastpapers.models import Topic, TopicNote

content = """
<style>
.main-heading {
    background: #1E3A8A;
    color: white;
    padding: 0.8rem 1.2rem;
    border-radius: 12px;
    font-size: 1.3rem;
    font-weight: bold;
    margin-bottom: 1rem;
}
.sub-heading {
    background: #E8F5E9;
    color: #1E3A8A;
    padding: 0.5rem 1rem;
    border-radius: 8px;
    margin: 1rem 0;
    font-weight: bold;
    border-left: 4px solid #10B981;
}
.point-number {
    font-weight: bold;
    color: #10B981;
    margin-right: 0.8rem;
}
.supplement-badge {
    background: #FF9800;
    color: white;
    font-size: 0.65rem;
    padding: 0.2rem 0.5rem;
    border-radius: 20px;
    margin-left: 0.5rem;
}
.key-definition {
    background: #FEF3C7;
    border-left: 4px solid #F59E0B;
    padding: 0.5rem 1rem;
    border-radius: 8px;
    margin: 0.5rem 0;
}
.warning-box {
    background: #FEE2E2;
    border-left: 4px solid #EF4444;
    padding: 0.5rem 1rem;
    border-radius: 8px;
    margin: 0.5rem 0;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
}
th {
    background: #1E3A8A;
    color: white;
    padding: 10px;
    text-align: left;
}
td {
    border: 1px solid #E5E7EB;
    padding: 8px 10px;
}
tr:nth-child(even) {
    background: #F9FAFB;
}
pre {
    background: #1F2937;
    color: #F3F4F6;
    padding: 1rem;
    border-radius: 8px;
    overflow-x: auto;
    font-family: 'Courier New', monospace;
    font-size: 0.85rem;
}
</style>

<div class="main-heading">📌 Topic 2: Atoms, Elements and Compounds</div>

<div class="sub-heading">2.1 Elements, compounds and mixtures</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> Describe the differences between elements, compounds and mixtures</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            表
                <tr style="background:#1E3A8A; color:white;"><th>Type</th><th>Definition</th><th>Example</th><th>Can it be separated?</th></tr>
                <tr><td><strong>Element</strong></td><td>A pure substance made of only one type of atom</td><td>Oxygen (O₂), Iron (Fe), Gold (Au)</td><td>Cannot be broken down chemically</td></tr>
                <tr style="background:#F9FAFB;"><td><strong>Compound</strong></td><td>Two or more elements chemically bonded together</td><td>Water (H₂O), Carbon dioxide (CO₂), Sodium chloride (NaCl)</td><td>Cannot be separated by physical means; needs chemical reaction</td></tr>
                <tr><td><strong>Mixture</strong></td><td>Two or more substances physically combined, not chemically bonded</td><td>Air, salt water, sand and iron filings</td><td>Can be separated by physical methods (filtration, evaporation, etc.)</td></tr>
            表
            <pre>
ELEMENT          COMPOUND           MIXTURE
● ● ● ●          ●─● ●─●            ● ●   ●─●
● ● ● ●          ●─● ●─●            ●─●   ● ●
(All same)      (Atoms bonded)     (Not bonded)</pre>
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
            <p><strong>Atomic Structure:</strong></p>
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
             -----</pre>
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
            表
                <tr style="background:#1E3A8A; color:white;"><th>Particle</th><th>Relative Charge</th><th>Relative Mass</th><th>Location</th></tr>
                <tr><td>Proton</td><td>+1</td><td>1</td><td>Nucleus</td></tr>
                <tr style="background:#F9FAFB;"><td>Neutron</td><td>0</td><td>1</td><td>Nucleus</td></tr>
                <tr><td>Electron</td><td>-1</td><td>1/1840 (negligible)</td><td>Electron shells</td></tr>
            表
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
            <p><strong>Atomic Number (Z)</strong> = Number of protons in the nucleus</p>
            <p>In a neutral atom, the number of protons = number of electrons</p>
            <div class="key-definition">
                💡 Example: Carbon has atomic number 6 → 6 protons, 6 electrons
            </div>
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
            <p><strong>Mass Number (A)</strong> = Number of protons + number of neutrons</p>
            <p><strong>Number of neutrons</strong> = Mass number - Atomic number</p>
            <div class="key-definition">
                💡 Example: Carbon-12 has mass number 12, atomic number 6 → 12 - 6 = 6 neutrons
            </div>
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
            表
                <tr style="background:#1E3A8A; color:white;"><th>Element</th><th>Atomic Number</th><th>Electronic Configuration</th></tr>
                <tr><td>Hydrogen</td><td>1</td><td>1</td></tr>
                <tr style="background:#F9FAFB;"><td>Helium</td><td>2</td><td>2</td></tr>
                <tr><td>Lithium</td><td>3</td><td>2,1</td></tr>
                <tr style="background:#F9FAFB;"><td>Beryllium</td><td>4</td><td>2,2</td></tr>
                <tr><td>Boron</td><td>5</td><td>2,3</td></tr>
                <tr style="background:#F9FAFB;"><td>Carbon</td><td>6</td><td>2,4</td></tr>
                <tr><td>Nitrogen</td><td>7</td><td>2,5</td></tr>
                <tr style="background:#F9FAFB;"><td>Oxygen</td><td>8</td><td>2,6</td></tr>
                <tr><td>Fluorine</td><td>9</td><td>2,7</td></tr>
                <tr style="background:#F9FAFB;"><td>Neon</td><td>10</td><td>2,8</td></tr>
                <tr><td>Sodium</td><td>11</td><td>2,8,1</td></tr>
                <tr style="background:#F9FAFB;"><td>Magnesium</td><td>12</td><td>2,8,2</td></tr>
                <tr><td>Aluminium</td><td>13</td><td>2,8,3</td></tr>
                <tr style="background:#F9FAFB;"><td>Silicon</td><td>14</td><td>2,8,4</td></tr>
                <tr><td>Phosphorus</td><td>15</td><td>2,8,5</td></tr>
                <tr style="background:#F9FAFB;"><td>Sulfur</td><td>16</td><td>2,8,6</td></tr>
                <tr><td>Chlorine</td><td>17</td><td>2,8,7</td></tr>
                <tr style="background:#F9FAFB;"><td>Argon</td><td>18</td><td>2,8,8</td></tr>
                <tr><td>Potassium</td><td>19</td><td>2,8,8,1</td></tr>
                <tr style="background:#F9FAFB;"><td>Calcium</td><td>20</td><td>2,8,8,2</td></tr>
            表
            <div class="key-definition">
                💡 <strong>Shell Rules:</strong> 1st shell = max 2 electrons, 2nd shell = max 8 electrons, 3rd shell = max 8 electrons (simplified model)
            </div>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">6</span> State that: (a) Group VIII noble gases have a full outer electron shell; (b) the number of outer shell electrons equals the group number in Groups I to VII; (c) the number of occupied electron shells equals the period number</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Relationship to Periodic Table:</strong></p>
            <ul>
                <li><strong>Period number</strong> = Number of occupied electron shells</li>
                <li><strong>Group number (I-VII)</strong> = Number of electrons in the outer shell</li>
                <li><strong>Group VIII (Noble gases)</strong> = Full outer shell (stable, unreactive)</li>
            </ul>
            <div class="key-definition">
                💡 Example: Sodium (Period 3, Group 1) → 3 shells, 1 outer electron → 2,8,1
            </div>
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
            <p><strong>Definition:</strong> Isotopes are atoms of the same element with the <strong>same number of protons</strong> but <strong>different numbers of neutrons</strong>.</p>
            <p><strong>Example: Chlorine</strong></p>
            <ul>
                <li>Chlorine-35: 17 protons, 18 neutrons</li>
                <li>Chlorine-37: 17 protons, 20 neutrons</li>
            </ul>
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
            <p><strong>Atomic Notation:</strong> \(^{A}_{Z}X\) where:</p>
            <ul>
                <li>A = Mass number (protons + neutrons)</li>
                <li>Z = Atomic number (protons)</li>
                <li>X = Element symbol</li>
            </ul>
            <div class="key-definition">
                💡 Example: \(^{12}_{6}C\) = Carbon-12 (6 protons, 6 neutrons)
            </div>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">3</span> State that isotopes of the same element have the same chemical properties because they have the same number of electrons and therefore the same electronic configuration <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Why Same Chemical Properties?</strong></p>
            <ul>
                <li>Chemical properties depend on <strong>electron configuration</strong></li>
                <li>All isotopes of an element have the same number of electrons</li>
                <li>Therefore, they react the same way chemically</li>
            </ul>
            <p><strong>Why Different Physical Properties?</strong></p>
            <ul>
                <li>Different mass affects physical properties like density, boiling point, and rate of diffusion</li>
            </ul>
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
            <p><strong>Formula:</strong></p>
            <p>Aᵣ = ( % of isotope A × mass of A ) + ( % of isotope B × mass of B ) / 100</p>
            <p><strong>Worked Example: Chlorine</strong></p>
            <ul>
                <li>Chlorine-35: 75% abundance</li>
                <li>Chlorine-37: 25% abundance</li>
            </ul>
            <p>Aᵣ = (75 × 35) + (25 × 37) / 100 = (2625 + 925) / 100 = 3550 / 100 = <strong>35.5</strong></p>
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
            <p><strong>Cations (positive ions):</strong> Metals lose electrons to achieve a full outer shell</p>
            <ul><li>Example: Na → Na⁺ + e⁻ (sodium atom loses 1 electron)</li></ul>
            <p><strong>Anions (negative ions):</strong> Non-metals gain electrons to achieve a full outer shell</p>
            <ul><li>Example: Cl + e⁻ → Cl⁻ (chlorine atom gains 1 electron)</li></ul>
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
            <p>An ionic bond is the <strong>strong electrostatic attraction</strong> between oppositely charged ions.</p>
            <p>Forms when a metal reacts with a non-metal.</p>
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
            <p><strong>Sodium Chloride (NaCl)</strong></p>
            <pre>
Na atom: 2,8,1          Cl atom: 2,8,7
         ↓                    ↓
Na⁺ ion: 2,8           Cl⁻ ion: 2,8,8

[Na]⁺   [ Cl ]⁻
        ••
        ••</pre>
            <div class="key-definition">
                💡 Group I metals lose 1 electron → +1 charge<br>
                Group VII non-metals gain 1 electron → -1 charge
            </div>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">4</span> Describe the properties of ionic compounds: high melting/boiling points; good electrical conductivity when aqueous or molten, poor when solid</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Properties of Ionic Compounds:</strong></p>
            表
                <tr style="background:#1E3A8A; color:white;"><th>Property</th><th>Explanation</th></tr>
                <tr><td>High melting/boiling points</td><td>Strong electrostatic forces between ions require lots of energy to overcome</td></tr>
                <tr style="background:#F9FAFB;"><td>Conducts electricity when molten or dissolved</td><td>Ions are free to move and carry charge</td></tr>
                <tr><td>Poor conductor when solid</td><td>Ions are fixed in position in the lattice</td></tr>
                <tr style="background:#F9FAFB;"><td>Hard but brittle</td><td>Layers of ions can shift, causing like charges to align and repel</td></tr>
            表
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">5</span> Describe the giant lattice structure of ionic compounds as a regular arrangement of alternating positive and negative ions <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Giant Lattice Structure:</strong></p>
            <ul>
                <li>Ions are arranged in a regular, repeating 3D pattern</li>
                <li>Alternating positive and negative ions</li>
                <li>Example: NaCl lattice (cubic structure)</li>
            </ul>
            <pre>
    +   -   +   -
   -   +   -   +
    +   -   +   -
   -   +   -   +
(Alternating positive and negative ions)</pre>
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
            <p><strong>High melting/boiling points:</strong> Strong electrostatic forces between oppositely charged ions in all directions require large amounts of energy to overcome.</p>
            <p><strong>Conductivity when molten/dissolved:</strong> Ions become free to move and can carry electric charge.</p>
            <p><strong>No conductivity when solid:</strong> Ions are fixed in lattice positions and cannot move.</p>
            <p><strong>Brittleness:</strong> When layers shift, like charges align and repel, causing the crystal to split.</p>
        </div>
    </div>
</div>

<div class="sub-heading">2.5 Simple molecules and covalent bonds</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> State that a covalent bond is formed when a pair of electrons is shared between two atoms leading to noble gas electronic configurations</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Covalent Bond:</strong> Formed when a <strong>pair of electrons is shared</strong> between two non-metal atoms.</p>
            <p>Each atom contributes one electron to the shared pair, and both atoms achieve a full outer shell (noble gas configuration).</p>
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
            <pre>
H₂:      H• + •H → H:H
Cl₂:     Cl•• + ••Cl → Cl:Cl (with 6 other electrons each)
H₂O:     H:O:H (O shares 2 pairs)
CH₄:     H:C:H with H above and below (C shares 4 pairs)
NH₃:     H:N:H with lone pair on N (N shares 3 pairs)
HCl:     H:Cl (H shares 1 pair)</pre>
            <div class="key-definition">
                💡 <strong>Note:</strong> Only outer shell electrons are shown in dot-and-cross diagrams.
            </div>
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
            <p><strong>Properties of Simple Molecular Compounds:</strong></p>
            表
                <tr style="background:#1E3A8A; color:white;"><th>Property</th><th>Explanation</th></tr>
                <tr><td>Low melting/boiling points</td><td>Weak intermolecular forces between molecules (not the strong covalent bonds inside molecules)</td></tr>
                <tr style="background:#F9FAFB;"><td>Poor electrical conductivity</td><td>No free electrons or ions to carry charge</td></tr>
                <tr><td>Often gases or liquids at room temperature</td><td>Weak forces mean they evaporate easily</td></tr>
            表
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">4</span> Describe the formation of covalent bonds in simple molecules (CH₃OH, C₂H₄, O₂, CO₂, N₂) using dot-and-cross diagrams <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Additional Molecules:</strong></p>
            <pre>
O₂:      O::O (double bond)
N₂:      N:::N (triple bond)
CO₂:     O::C::O (double bonds)
C₂H₄:    H₂C=CH₂ (double bond between C)
CH₃OH:   H
         |
    H—C—O—H
         |
         H</pre>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">5</span> Explain in terms of structure and bonding the properties of simple molecular compounds: low melting/boiling points due to weak intermolecular forces; poor electrical conductivity <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Key Concept:</strong></p>
            <ul>
                <li><strong>Intramolecular forces</strong> (covalent bonds) = strong, hold atoms together within a molecule</li>
                <li><strong>Intermolecular forces</strong> = weak, hold molecules together</li>
                <li>Low melting/boiling points occur because only weak intermolecular forces need to be overcome</li>
                <li>Poor conductivity because no free electrons or ions are present</li>
            </ul>
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
            <p><strong>Diamond:</strong></p>
            <ul><li>Each carbon atom bonded to 4 others (tetrahedral)</li><li>All strong covalent bonds</li></ul>
            <p><strong>Graphite:</strong></p>
            <ul><li>Each carbon bonded to 3 others, forming layers of hexagons</li><li>Strong covalent bonds within layers; weak intermolecular forces between layers</li><li>One free electron per carbon atom becomes delocalised</li></ul>
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
            表
                <tr style="background:#1E3A8A; color:white;"><th>Property</th><th>Diamond</th><th>Graphite</th></tr>
                <tr><td>Bonding</td><td>4 covalent bonds per carbon</td><td>3 covalent bonds per carbon</td></tr>
                <tr style="background:#F9FAFB;"><td>Structure</td><td>3D tetrahedral</td><td>Layered hexagonal</td></tr>
                <tr><td>Hardness</td><td>Very hard (hardest natural substance)</td><td>Soft, slippery</td></tr>
                <tr style="background:#F9FAFB;"><td>Conductivity</td><td>Non-conductor (no free electrons)</td><td>Conductor (delocalised electrons)</td></tr>
                <tr><td>Uses</td><td>Cutting tools, drills, jewellery</td><td>Pencil lead, lubricant, electrodes</td></tr>
            表
        </div>
    </div>
</div>

<div class="sub-heading">2.7 Metallic bonding</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> Describe metallic bonding as the electrostatic attraction between the positive ions in a giant metallic lattice and a 'sea' of delocalised electrons <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Metallic Bonding:</strong></p>
            <ul>
                <li>Metal atoms lose their outer electrons to become positive ions</li>
                <li>These electrons become <strong>delocalised</strong> (free to move) forming a "sea of electrons"</li>
                <li>The metallic bond is the <strong>electrostatic attraction</strong> between positive metal ions and the delocalised electrons</li>
            </ul>
            <pre>
Metal lattice:   +   +   +   +
                 +   +   +   +   (with sea of electrons around)
                 +   +   +   +</pre>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">2</span> Explain in terms of structure and bonding the properties of metals: good electrical conductivity; malleability and ductility <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            表
                <tr style="background:#1E3A8A; color:white;"><th>Property</th><th>Explanation</th></tr>
                <tr><td>Good electrical conductivity</td><td>Delocalised electrons are free to move and carry charge through the structure</td></tr>
                <tr style="background:#F9FAFB;"><td>Good thermal conductivity</td><td>Delocalised electrons transfer kinetic energy quickly</td></tr>
                <tr><td>High melting/boiling points</td><td>Strong electrostatic forces between ions and electrons require lots of energy to overcome</td></tr>
                <tr style="background:#F9FAFB;"><td>Malleable (can be hammered into shape)</td><td>Layers of positive ions can slide over each other without breaking the metallic bond</td></tr>
                <tr><td>Ductile (can be drawn into wires)</td><td>Same reason as malleability - layers can slide</td></tr>
            表
        </div>
    </div>
</div>

<div class="warning-box">
    <strong>⚠️ Common Mistakes to Avoid:</strong><br><br>
    • ❌ "Atoms expand when heated" → ✅ Particles gain energy and move more, they don't expand<br>
    • ❌ "Isotopes have different chemical properties" → ✅ Same chemical properties, different physical properties<br>
    • ❌ "Ionic compounds conduct electricity when solid" → ✅ Only when molten or dissolved<br>
    • ❌ "Covalent bonds are weak" → ✅ Covalent bonds are strong; intermolecular forces are weak<br>
    • ❌ "Graphite is hard like diamond" → ✅ Graphite is soft and slippery due to layered structure
</div>
"""

# Add to database
topic = Topic.objects.get(code='2')
note, created = TopicNote.objects.update_or_create(
    topic=topic,
    defaults={'content': content}
)
print(f"✅ Added revision notes for {topic.name}")
print(f"📝 Content includes:")
print("   - 2.1 Elements, compounds and mixtures (1 point)")
print("   - 2.2 Atomic structure and Periodic Table (6 points)")
print("   - 2.3 Isotopes (4 points)")
print("   - 2.4 Ions and ionic bonds (6 points)")
print("   - 2.5 Simple molecules and covalent bonds (5 points)")
print("   - 2.6 Giant covalent structures (2 points)")
print("   - 2.7 Metallic bonding (2 points)")
print("\n🔗 View at: https://chempassion.info/revision-notes/")