import os
import sys
import django

sys.path.append('C:\\Users\\Dell\\igcse-chemistry-platform')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chemistry_hub.settings')
django.setup()

from pastpapers.models import Topic, TopicNote

# ==================== TOPIC 1: States of Matter ====================
topic1_content = """
<div class="main-heading">📌 Topic 1: States of Matter</div>

<div class="sub-heading">1.1 Solids, liquids and gases</div>

<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> State the distinguishing properties of solids, liquids and gases</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe the structures of solids, liquids and gases in terms of particle separation, arrangement and motion</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Describe changes of state in terms of melting, boiling, evaporating, freezing and condensing</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> Describe the effects of temperature and pressure on the volume of a gas</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">5</span> Explain changes of state in terms of kinetic particle theory, including the interpretation of heating and cooling curves <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">6</span> Explain, in terms of kinetic particle theory, the effects of temperature and pressure on the volume of a gas <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">1.2 Diffusion</div>

<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe and explain diffusion in terms of kinetic particle theory</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe and explain the effect of relative molecular mass on the rate of diffusion of gases <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
"""

# ==================== TOPIC 2: Atoms, elements and compounds ====================
topic2_content = """
<div class="main-heading">📌 Topic 2: Atoms, elements and compounds</div>

<div class="sub-heading">2.1 Elements, compounds and mixtures</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe the differences between elements, compounds and mixtures</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">2.2 Atomic structure and the Periodic Table</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe the structure of the atom as a central nucleus containing neutrons and protons surrounded by electrons in shells</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> State the relative charges and relative masses of a proton, a neutron and an electron</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Define proton number/atomic number as the number of protons in the nucleus of an atom</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> Define mass number/nucleon number as the total number of protons and neutrons in the nucleus of an atom</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">5</span> Determine the electronic configuration of elements and their ions with proton number 1 to 20</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">6</span> State that Group VIII noble gases have a full outer electron shell; number of outer shell electrons equals group number; number of occupied shells equals period number</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">2.3 Isotopes</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Define isotopes as different atoms of the same element with same protons but different neutrons</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Interpret and use symbols for atoms and ions</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> State that isotopes have same chemical properties due to same electronic configuration <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> Calculate relative atomic mass from isotopic abundances <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">2.4 Ions and ionic bonds</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe formation of positive ions (cations) and negative ions (anions)</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> State that an ionic bond is a strong electrostatic attraction between oppositely charged ions</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Describe formation of ionic bonds between Group I and Group VII using dot-and-cross diagrams</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> Describe properties of ionic compounds: high melting/boiling points; good conductivity when aqueous or molten, poor when solid</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">5</span> Describe giant lattice structure of ionic compounds <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">6</span> Explain properties of ionic compounds in terms of structure and bonding <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">2.5 Simple molecules and covalent bonds</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> State that a covalent bond is formed when a pair of electrons is shared between two atoms</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe formation of covalent bonds in H₂, Cl₂, H₂O, CH₄, NH₃, HCl using dot-and-cross diagrams</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Describe properties of simple molecular compounds: low melting/boiling points; poor electrical conductivity</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">2.6 Giant covalent structures</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe giant covalent structures of graphite and diamond</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Relate structures and bonding of graphite and diamond to their uses</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">2.7 Metallic bonding</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe metallic bonding as electrostatic attraction between positive ions and a 'sea' of delocalised electrons</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Explain properties of metals: good electrical conductivity; malleability and ductility</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
"""

# ==================== TOPIC 3: Stoichiometry ====================
topic3_content = """
<div class="main-heading">📌 Topic 3: Stoichiometry</div>

<div class="sub-heading">3.1 Formulae</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> State the formulae of the elements and compounds named in the subject content</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Define the molecular formula of a compound</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Deduce the formula of a simple compound from the relative numbers of atoms present</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> Construct word equations and symbol equations, including state symbols</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">5</span> Define empirical formula <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">6</span> Deduce formula of ionic compound from charges on ions <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">7</span> Construct symbol equations with state symbols, including ionic equations <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">3.2 Relative masses of atoms and molecules</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe relative atomic mass, Aᵣ</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Define relative molecular mass, Mᵣ</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Calculate reacting masses in simple proportions</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">3.3 The mole and Avogadro constant</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> State that the mole is the unit of amount of substance and contains 6.02 × 10²³ particles <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Use the relationship: amount = mass / molar mass <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Use molar gas volume (24 dm³ at r.t.p.) in calculations <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> Calculate reacting masses, limiting reactants, volumes of gases, concentrations <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">5</span> Calculate empirical and molecular formulae <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">6</span> Calculate percentage yield, percentage composition, percentage purity <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
"""

# ==================== TOPIC 4: Electrochemistry ====================
topic4_content = """
<div class="main-heading">📌 Topic 4: Electrochemistry</div>

<div class="sub-heading">4.1 Electrolysis</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Define electrolysis as the decomposition of an ionic compound by an electric current</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Identify anode, cathode and electrolyte in simple electrolytic cells</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Identify products during electrolysis of molten lead(II) bromide, concentrated NaCl, dilute H₂SO₄</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> State that metals or hydrogen form at cathode; non-metals (other than H₂) at anode</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">5</span> Predict products for electrolysis of a binary compound in molten state</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">6</span> State that metal objects are electroplated to improve appearance and corrosion resistance</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">7</span> Describe how metals are electroplated</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">8</span> Describe transfer of charge during electrolysis <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">9</span> Construct ionic half-equations for reactions at electrodes <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">4.2 Hydrogen-oxygen fuel cells</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> State that hydrogen-oxygen fuel cell uses hydrogen and oxygen to produce electricity with water as only product</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe advantages and disadvantages of fuel cells compared to petrol engines <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
"""

# ==================== TOPIC 5: Chemical Energetics ====================
topic5_content = """
<div class="main-heading">📌 Topic 5: Chemical Energetics</div>

<div class="sub-heading">5.1 Exothermic and endothermic reactions</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> State that an exothermic reaction transfers thermal energy to surroundings, increasing temperature</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> State that an endothermic reaction takes in thermal energy from surroundings, decreasing temperature</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Interpret reaction pathway diagrams showing exothermic and endothermic reactions</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> Define enthalpy change, ΔH <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">5</span> Define activation energy, Eₐ <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">6</span> Draw and label reaction pathway diagrams <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">7</span> Explain enthalpy change in terms of bond breaking and bond making <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">8</span> Calculate enthalpy change using bond energies <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
"""

# ==================== TOPIC 6: Chemical Reactions ====================
topic6_content = """
<div class="main-heading">📌 Topic 6: Chemical Reactions</div>

<div class="sub-heading">6.1 Physical and chemical changes</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Identify physical and chemical changes, and describe differences between them</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">6.2 Rate of reaction</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe effect of concentration, pressure, surface area, temperature, catalysts on rate</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> State that a catalyst increases rate and is unchanged at end</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Describe practical methods for investigating rate of reaction</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> Interpret data and graphs from rate experiments</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">5</span> Describe collision theory <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">6</span> Explain effects on rate using collision theory <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">7</span> State that catalyst decreases activation energy <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">6.3 Reversible reactions and equilibrium</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> State that some chemical reactions are reversible</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe how changing conditions affects reversible reactions</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Describe equilibrium in a closed system <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> Predict how position of equilibrium is affected by changes <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">5</span> State Haber process equation and conditions <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">6</span> State Contact process equation and conditions <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">6.4 Redox</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Use Roman numerals to indicate oxidation number</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Define redox as simultaneous oxidation and reduction</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Define oxidation as gain of oxygen, reduction as loss of oxygen</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> Define oxidation as loss of electrons, reduction as gain of electrons <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">5</span> Identify oxidising and reducing agents <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
"""

# ==================== TOPIC 7: Acids, Bases and Salts ====================
topic7_content = """
<div class="main-heading">📌 Topic 7: Acids, Bases and Salts</div>

<div class="sub-heading">7.1 Properties of acids and bases</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe properties of acids: reactions with metals, bases, carbonates</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe acids in terms of effect on indicators (litmus, thymolphthalein, methyl orange)</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> State that bases are oxides/hydroxides of metals; alkalis are soluble bases</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> Describe properties of bases: reactions with acids, ammonium salts</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">5</span> Describe alkalis in terms of effect on indicators</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">6</span> State that acids contain H⁺ ions; alkalis contain OH⁻ ions</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">7</span> Describe neutralisation: H⁺ + OH⁻ → H₂O</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">8</span> Define acids as proton donors, bases as proton acceptors <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">9</span> Define strong acids (complete dissociation) and weak acids (partial dissociation) <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">7.2 Oxides</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Classify oxides as acidic (SO₂, CO₂) or basic (CuO, CaO)</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe amphoteric oxides (Al₂O₃, ZnO) <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">7.3 Preparation of salts</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe preparation of soluble salts by reaction of acid with alkali, metal, insoluble base, insoluble carbonate</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe solubility rules for salts</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Define hydrated and anhydrous substances</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> Describe preparation of insoluble salts by precipitation <span class="supplement-badge">Supplement</span></span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
"""

# ==================== TOPIC 8: The Periodic Table ====================
topic8_content = """
<div class="main-heading">📌 Topic 8: The Periodic Table</div>

<div class="sub-heading">8.1 Arrangement of elements</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe the Periodic Table arrangement in periods and groups by increasing proton number</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe change from metallic to non-metallic character across a period</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Relate group number to charge of ions formed</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> Explain similarities in chemical properties of elements in the same group</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">8.2 Group I properties (Alkali metals)</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe trends down Group I: decreasing melting point, increasing density, increasing reactivity</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">8.3 Group VII properties (Halogens)</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe trends down Group VII: increasing density, decreasing reactivity</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> State appearance of halogens at r.t.p.</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Describe displacement reactions of halogens with halide ions</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">8.4 Transition elements</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe transition elements: high densities, high melting points, form coloured compounds, act as catalysts</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">8.5 Noble gases</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe noble gases as unreactive, monatomic gases due to full outer shell</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
"""

# ==================== TOPIC 9: Metals ====================
topic9_content = """
<div class="main-heading">📌 Topic 9: Metals</div>

<div class="sub-heading">9.1 Properties of metals</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Compare physical properties of metals and non-metals</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe chemical properties of metals: reactions with dilute acids, water, steam, oxygen</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">9.2 Uses of metals</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe uses of aluminium and copper based on their properties</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">9.3 Alloys and their properties</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe an alloy as a mixture of a metal with other elements</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> State that alloys can be harder and stronger than pure metals</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">9.4 Reactivity series</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> State the order of the reactivity series</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe reactions of metals with water, steam, dilute acid</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">9.5 Corrosion of metals</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> State conditions for rusting: oxygen and water</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe barrier methods to prevent rusting</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">9.6 Extraction of metals</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe ease of obtaining metals from ores related to reactivity series</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe extraction of iron from hematite in the blast furnace</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> State that aluminium is extracted by electrolysis</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
"""

# ==================== TOPIC 10: Chemistry of the Environment ====================
topic10_content = """
<div class="main-heading">📌 Topic 10: Chemistry of the Environment</div>

<div class="sub-heading">10.1 Water</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe chemical tests for water using anhydrous cobalt(II) chloride and anhydrous copper(II) sulfate</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe how to test purity of water using melting point and boiling point</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> State substances found in natural water sources</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> Describe treatment of domestic water supply</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">10.2 Fertilisers</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> State that ammonium salts and nitrates are used as fertilisers</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">10.3 Air quality and climate</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> State composition of clean, dry air</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> State sources of air pollutants</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> State adverse effects of air pollutants</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> Describe strategies to reduce environmental issues</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">5</span> Describe photosynthesis: CO₂ + H₂O → glucose + oxygen</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
"""

# ==================== TOPIC 11: Organic Chemistry ====================
topic11_content = """
<div class="main-heading">📌 Topic 11: Organic Chemistry</div>

<div class="sub-heading">11.1 Formulae, functional groups and terminology</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Draw and interpret displayed formula of a molecule</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Write and interpret general formulae: alkanes, alkenes, alcohols, carboxylic acids</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Identify a functional group</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">4</span> State that a homologous series has similar chemical properties due to same functional group</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">5</span> Define saturated and unsaturated compounds</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">11.2 Naming organic compounds</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Name and draw displayed formulae of methane, ethane, ethene, ethanol, ethanoic acid</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">11.3 Fuels</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Name fossil fuels: coal, natural gas, petroleum</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe fractional distillation of petroleum</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">11.4 Alkanes</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> State alkanes are saturated hydrocarbons with single covalent bonds</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe substitution reaction of alkanes with chlorine</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">11.5 Alkenes</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> State alkenes are unsaturated hydrocarbons with double covalent bond</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe manufacture of alkenes by cracking</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Describe test to distinguish saturated/unsaturated: bromine water</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">11.6 Alcohols</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe manufacture of ethanol by fermentation and catalytic addition</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe combustion of ethanol</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> State uses of ethanol</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">11.7 Carboxylic acids</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Describe reactions of ethanoic acid with metals, bases, carbonates</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe formation of ethanoic acid by oxidation of ethanol</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Describe reaction of carboxylic acid with alcohol to form an ester</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>

<div class="sub-heading">11.8 Polymers</div>
<div class="point-item"><div class="point-question"><span><span class="point-number">1</span> Define polymers as large molecules from monomers</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">2</span> Describe formation of poly(ethene) by addition polymerisation</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
<div class="point-item"><div class="point-question"><span><span class="point-number">3</span> Describe environmental challenges caused by plastics</span><span class="icon">▼</span></div><div class="point-answer"><div class="answer-content"><p><em>Answer coming soon...</em></p></div></div></div>
"""

# Dictionary of all topics
all_topics = {
    '1': topic1_content,
    '2': topic2_content,
    '3': topic3_content,
    '4': topic4_content,
    '5': topic5_content,
    '6': topic6_content,
    '7': topic7_content,
    '8': topic8_content,
    '9': topic9_content,
    '10': topic10_content,
    '11': topic11_content,
}

print("=" * 60)
print("Adding syllabus statements for ALL 11 topics...")
print("=" * 60)

for code, content in all_topics.items():
    try:
        topic = Topic.objects.get(code=code)
        note, created = TopicNote.objects.update_or_create(
            topic=topic,
            defaults={'content': content}
        )
        point_count = content.count('point-item')
        print(f"✅ Topic {code}: {topic.name} - {point_count} statements added")
    except Topic.DoesNotExist:
        print(f"❌ Topic {code} not found!")

print("\n" + "=" * 60)
print("✨ All 11 topics added with syllabus statements!")
print("📝 Each point has 'Answer coming soon...'")
print("🔗 View at: https://chempassion.info/revision-notes/")