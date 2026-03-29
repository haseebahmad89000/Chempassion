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
    padding: 0.8rem 1rem;
    border-radius: 8px;
    margin: 0.8rem 0;
}
.warning-box {
    background: #FEE2E2;
    border-left: 4px solid #EF4444;
    padding: 0.8rem 1rem;
    border-radius: 8px;
    margin: 0.8rem 0;
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
    border: 1px solid #ddd;
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
    font-family: monospace;
    font-size: 0.8rem;
}
</style>

<div class="main-heading">📌 Topic 3: Stoichiometry</div>

<div class="sub-heading">3.1 Formulae</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> State the formulae of the elements and compounds named in the subject content</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Diatomic Molecules (7 elements):</strong> H₂, N₂, O₂, F₂, Cl₂, Br₂, I₂</p>
            <p><strong>Common Compounds:</strong></p>
            表
                <tr style="background:#1E3A8A; color:white;"><th>Compound</th><th>Formula</th><th>Compound</th><th>Formula</th> 表
                <tr><td>Water</td><td>H₂O</td><td>Carbon dioxide</td><td>CO₂</td> </tr>
                <tr style="background:#F9FAFB;"><td>Ammonia</td><td>NH₃</td><td>Methane</td><td>CH₄</td> </tr>
                <tr><td>Sodium chloride</td><td>NaCl</td><td>Sulfuric acid</td><td>H₂SO₄</td> </tr>
                <tr style="background:#F9FAFB;"><td>Hydrochloric acid</td><td>HCl</td><td>Sodium hydroxide</td><td>NaOH</td> </tr>
                <tr><td>Calcium carbonate</td><td>CaCO₃</td><td>Magnesium oxide</td><td>MgO</td> </tr>
            表
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">2</span> Define the molecular formula of a compound as the number and type of different atoms in one molecule</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            表
                <tr style="background:#1E3A8A; color:white;"><th>Compound</th><th>Molecular Formula</th><th>Atoms Present</th> 表
                <tr><td>Water</td><td>H₂O</td><td>2 hydrogen, 1 oxygen</td> </tr>
                <tr style="background:#F9FAFB;"><td>Methane</td><td>CH₄</td><td>1 carbon, 4 hydrogen</td> </tr>
                <tr><td>Ammonia</td><td>NH₃</td><td>1 nitrogen, 3 hydrogen</td> </tr>
                <tr style="background:#F9FAFB;"><td>Ethanol</td><td>C₂H₅OH</td><td>2 carbon, 6 hydrogen, 1 oxygen</td> </tr>
                <tr><td>Glucose</td><td>C₆H₁₂O₆</td><td>6 carbon, 12 hydrogen, 6 oxygen</td> </tr>
            表
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">3</span> Deduce the formula of a simple compound from the relative numbers of atoms present in a model or a diagrammatic representation</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            表
                <tr style="background:#1E3A8A; color:white;"><th>Diagram</th><th>Atoms</th><th>Molecular Formula</th> 表
                <tr><td>4 carbon + 10 hydrogen</td><td>C₄H₁₀</td><td>Butane</td> </tr>
                <tr style="background:#F9FAFB;"><td>2 carbon + 4 hydrogen</td><td>C₂H₄</td><td>Ethene</td> </tr>
                <tr><td>1 carbon + 4 hydrogen</td><td>CH₄</td><td>Methane</td> </tr>
                <tr style="background:#F9FAFB;"><td>2 hydrogen + 1 oxygen</td><td>H₂O</td><td>Water</td> </tr>
                <tr><td>1 nitrogen + 3 hydrogen</td><td>NH₃</td><td>Ammonia</td> </tr>
            表
            <div class="key-definition">💡 Count the number of each type of atom in the diagram to determine the molecular formula.</div>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">4</span> Construct word equations and symbol equations to show how reactants form products, including state symbols</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Word Equations:</strong> Reactants → Products (using full chemical names)</p>
            <p>Example: magnesium + oxygen → magnesium oxide</p>
            <p><strong>Symbol Equations:</strong> Use chemical formulae instead of names</p>
            <p>Example: 2Mg(s) + O₂(g) → 2MgO(s)</p>
            <p><strong>State Symbols:</strong></p>
            <ul><li>(s) = solid</li><li>(l) = liquid</li><li>(g) = gas</li><li>(aq) = aqueous (dissolved in water)</li></ul>
            <p><strong>Balancing Equations - Steps:</strong></p>
            <ol><li>Write unbalanced equation with correct formulae</li><li>Count atoms of each element on both sides</li><li>Add coefficients (numbers in front) to balance</li><li>Check again</li></ol>
            <p><strong>Worked Example:</strong> Magnesium + oxygen → magnesium oxide</p>
            <ul><li>Unbalanced: Mg + O₂ → MgO</li><li>Balance oxygen: Mg + O₂ → 2MgO</li><li>Balance magnesium: 2Mg + O₂ → 2MgO</li></ul>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">5</span> Define the empirical formula of a compound as the simplest whole number ratio of the different atoms or ions in a compound <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            表
                <tr style="background:#1E3A8A; color:white;"><th>Compound</th><th>Molecular Formula</th><th>Empirical Formula</th><th>Ratio</th> 表
                <tr><td>Hydrogen peroxide</td><td>H₂O₂</td><td>HO</td><td>1:1</td> </tr>
                <tr style="background:#F9FAFB;"><td>Glucose</td><td>C₆H₁₂O₆</td><td>CH₂O</td><td>1:2:1</td> </tr>
                <tr><td>Ethane</td><td>C₂H₆</td><td>CH₃</td><td>1:3</td> </tr>
                <tr style="background:#F9FAFB;"><td>Ethene</td><td>C₂H₄</td><td>CH₂</td><td>1:2</td> </tr>
                <tr><td>Benzene</td><td>C₆H₆</td><td>CH</td><td>1:1</td> </tr>
            表
            <div class="key-definition">💡 Ionic compounds always have empirical formulas as their chemical formula (e.g., NaCl, MgO).</div>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">6</span> Deduce the formula of an ionic compound from the charges on the ions <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Swap and Drop Method:</strong></p>
            表
                <tr style="background:#1E3A8A; color:white;"><th>Ions</th><th>Swap and Drop</th><th>Formula</th><th>Name</th> 表
                <tr><td>Na⁺ + Cl⁻</td><td>Na¹ Cl¹</td><td>NaCl</td><td>Sodium chloride</td> </tr>
                <tr style="background:#F9FAFB;"><td>Mg²⁺ + Cl⁻</td><td>Mg¹ Cl²</td><td>MgCl₂</td><td>Magnesium chloride</td> </tr>
                <tr><td>Al³⁺ + O²⁻</td><td>Al² O³</td><td>Al₂O₃</td><td>Aluminium oxide</td> </tr>
                <tr style="background:#F9FAFB;"><td>Fe³⁺ + SO₄²⁻</td><td>Fe₂ (SO₄)₃</td><td>Fe₂(SO₄)₃</td><td>Iron(III) sulfate</td> </tr>
                <tr><td>Ca²⁺ + OH⁻</td><td>Ca¹ (OH)₂</td><td>Ca(OH)₂</td><td>Calcium hydroxide</td> </tr>
            表
            <p><strong>Common Polyatomic Ions:</strong> CO₃²⁻ (carbonate), SO₄²⁻ (sulfate), OH⁻ (hydroxide), NO₃⁻ (nitrate), NH₄⁺ (ammonium)</p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">7</span> Construct symbol equations with state symbols, including ionic equations <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Ionic Equations:</strong> Show only the ions that actually react. Remove spectator ions (ions that appear unchanged on both sides).</p>
            <p><strong>Example: Neutralisation</strong></p>
            <ul><li>Full equation: HCl(aq) + NaOH(aq) → NaCl(aq) + H₂O(l)</li><li>Ionic equation: H⁺(aq) + OH⁻(aq) → H₂O(l)</li></ul>
            <p><strong>Example: Displacement of chlorine with potassium iodide</strong></p>
            <ul><li>Full equation: 2KI(aq) + Cl₂(aq) → 2KCl(aq) + I₂(aq)</li><li>Ionic equation: 2I⁻(aq) + Cl₂(aq) → 2Cl⁻(aq) + I₂(aq)</li></ul>
            <div class="key-definition">💡 Steps: 1. Write full balanced equation, 2. Replace ionic compounds with ions, 3. Remove spectator ions, 4. Write simplified ionic equation</div>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">8</span> Deduce the symbol equation with state symbols for a chemical reaction, given relevant information <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Worked Example 1:</strong> Aluminium burns in chlorine to form aluminium chloride.</p>
            <ul><li>Aluminium: Al(s)</li><li>Chlorine: Cl₂(g)</li><li>Aluminium chloride: AlCl₃(s)</li></ul>
            <p>Unbalanced: Al(s) + Cl₂(g) → AlCl₃(s)</p>
            <p>Balance: 2Al(s) + 3Cl₂(g) → 2AlCl₃(s)</p>
            <p><strong>Worked Example 2:</strong> Magnesium reacts with hydrochloric acid</p>
            <ul><li>Magnesium: Mg(s)</li><li>Hydrochloric acid: HCl(aq)</li><li>Magnesium chloride: MgCl₂(aq)</li><li>Hydrogen: H₂(g)</li></ul>
            <p>Unbalanced: Mg(s) + HCl(aq) → MgCl₂(aq) + H₂(g)</p>
            <p>Balance: Mg(s) + 2HCl(aq) → MgCl₂(aq) + H₂(g)</p>
        </div>
    </div>
</div>

<div class="sub-heading">3.2 Relative masses of atoms and molecules</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> Describe relative atomic mass, Aᵣ, as the average mass of the isotopes of an element compared to 1/12th of the mass of an atom of ¹²C</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Relative Atomic Mass (Aᵣ):</strong> The average mass of all isotopes of an element compared to 1/12th of a carbon-12 atom.</p>
            表
                <tr style="background:#1E3A8A; color:white;"><th>Element</th><th>Aᵣ</th><th>Meaning</th> 表
                <tr><td>Hydrogen (H)</td><td>1</td><td>1/12 the mass of carbon-12</td> </tr>
                <tr style="background:#F9FAFB;"><td>Carbon (C)</td><td>12</td><td>Standard reference</td> </tr>
                <tr><td>Oxygen (O)</td><td>16</td><td>16 times heavier than 1/12 of carbon-12</td> </tr>
                <tr style="background:#F9FAFB;"><td>Magnesium (Mg)</td><td>24</td><td>Twice as heavy as carbon-12</td> </tr>
                <tr><td>Chlorine (Cl)</td><td>35.5</td><td>Average of isotopes Cl-35 and Cl-37</td> </tr>
            表
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">2</span> Define relative molecular mass, Mᵣ, as the sum of the relative atomic masses</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            表
                <tr style="background:#1E3A8A; color:white;"><th>Compound</th><th>Formula</th><th>Calculation</th><th>Mᵣ</th> 表
                <td><td>Water</td><td>H₂O</td><td>(2 × 1) + 16</td><td>18</td> </tr>
                <tr style="background:#F9FAFB;"><td>Carbon dioxide</td><td>CO₂</td><td>12 + (2 × 16)</td><td>44</td> </tr>
                <tr><td>Sodium chloride</td><td>NaCl</td><td>23 + 35.5</td><td>58.5</td> </tr>
                <tr style="background:#F9FAFB;"><td>Calcium carbonate</td><td>CaCO₃</td><td>40 + 12 + (3 × 16)</td><td>100</td> </tr>
                <tr><td>Magnesium nitrate</td><td>Mg(NO₃)₂</td><td>24 + (2 × 14) + (6 × 16)</td><td>148</td> </tr>
            表
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">3</span> Calculate reacting masses in simple proportions</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Law of Conservation of Mass:</strong> Total mass of reactants = total mass of products</p>
            <p><strong>Worked Example:</strong> 2Ca + O₂ → 2CaO</p>
            <ul><li>2 × 40 = 80g Ca reacts with 2 × 16 = 32g O₂</li><li>Forms 2 × (40 + 16) = 112g CaO</li><li>Ratio: 80 : 32 : 112 (simplified: 5 : 2 : 7)</li></ul>
            <p><strong>Worked Example:</strong> Calculate mass of CO₂ from 32g CH₄</p>
            <p>CH₄ + 2O₂ → CO₂ + 2H₂O</p>
            <ul><li>16g CH₄ produces 44g CO₂</li><li>32g CH₄ is double → 2 × 44 = 88g CO₂</li></ul>
        </div>
    </div>
</div>

<div class="sub-heading">3.3 The mole and the Avogadro constant <span class="supplement-badge">Supplement</span></div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> State that the mole is the unit of amount of substance and that one mole contains 6.02 × 10²³ particles (Avogadro constant)</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>What is a Mole?</strong> The mole is the unit for amount of substance.</p>
            <ul><li>1 mole = 6.02 × 10²³ particles (Avogadro constant)</li><li>1 mole of any element = its relative atomic mass in grams</li><li>1 mole of any compound = its relative formula mass in grams</li></ul>
            <p><strong>Examples:</strong></p>
            <ul><li>1 mole of carbon = 12 g (contains 6.02 × 10²³ atoms)</li><li>1 mole of water = 18 g (contains 6.02 × 10²³ molecules)</li><li>1 mole of sodium chloride = 58.5 g (contains 6.02 × 10²³ formula units)</li></ul>
            <p><strong>Key Formula:</strong> Moles = Mass (g) / Molar Mass (g/mol)</p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">2</span> Use the relationship: amount of substance (mol) = mass (g) / molar mass (g/mol)</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Worked Examples:</strong></p>
            表
                <tr style="background:#1E3A8A; color:white;"><th>Calculate</th><th>Example</th><th>Answer</th> 表
                <tr><td>Moles from mass</td><td>6g of carbon (Mᵣ=12)</td><td>6/12 = 0.5 mol</td> </tr>
                <tr style="background:#F9FAFB;"><td>Mass from moles</td><td>0.25 mol of water (Mᵣ=18)</td><td>0.25 × 18 = 4.5 g</td> </tr>
                <tr><td>Molar mass from moles</td><td>0.1 mol has mass 5.6g</td><td>5.6/0.1 = 56 g/mol</td> </tr>
                <tr style="background:#F9FAFB;"><td>Number of particles</td><td>0.5 mol of CO₂</td><td>0.5 × 6.02×10²³ = 3.01×10²³ molecules</td> </tr>
            表
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">3</span> Use the molar gas volume, taken as 24 dm³ at room temperature and pressure (r.t.p.), in calculations involving gases</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Molar Gas Volume:</strong> At r.t.p. (20°C, 1 atm), 1 mole of ANY gas occupies 24 dm³ (24,000 cm³).</p>
            <p><strong>Formulas:</strong> Volume (dm³) = Moles × 24 | Moles = Volume (dm³) / 24</p>
            表
                <tr style="background:#1E3A8A; color:white;"><th>Gas</th><th>Moles</th><th>Volume (dm³)</th><th>Volume (cm³)</th> 表
                <tr><td>Hydrogen</td><td>2</td><td>48</td><td>48,000</td> </tr>
                <tr style="background:#F9FAFB;"><td>Carbon dioxide</td><td>0.25</td><td>6</td><td>6,000</td> </tr>
                <tr><td>Oxygen</td><td>5.4</td><td>129.6</td><td>129,600</td> </tr>
            表
            <div class="key-definition">💡 1 dm³ = 1000 cm³. To convert cm³ to dm³, divide by 1000.</div>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">4</span> Calculate concentrations of solutions expressed in g/dm³ and mol/dm³</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Concentration Formulas:</strong></p>
            <p>Concentration (g/dm³) = Mass of solute (g) / Volume of solution (dm³)</p>
            <p>Concentration (mol/dm³) = Moles of solute / Volume of solution (dm³)</p>
            <p><strong>Conversions:</strong> 1 dm³ = 1000 cm³. To convert cm³ to dm³, divide by 1000.</p>
            <p><strong>Worked Example:</strong> 80 g NaOH dissolved in 500 cm³ water</p>
            <ul><li>Molar mass NaOH = 40 g/mol</li><li>Moles = 80 / 40 = 2 mol</li><li>Volume = 500 / 1000 = 0.5 dm³</li><li>Concentration = 2 / 0.5 = 4 mol/dm³</li></ul>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">5</span> Calculate empirical formulae and molecular formulae</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Steps to Calculate Empirical Formula:</strong></p>
            <ol><li>Write the elements</li><li>Write given masses or percentages</li><li>Divide by atomic mass to find moles</li><li>Divide by the smallest number of moles</li><li>Convert to whole numbers</li></ol>
            <p><strong>Worked Example:</strong> 10 g H and 80 g O</p>
            <ul><li>H moles = 10 / 1 = 10</li><li>O moles = 80 / 16 = 5</li><li>Ratio = 10:5 = 2:1</li><li>Empirical formula = H₂O</li></ul>
            <p><strong>Molecular Formula:</strong> (Empirical formula) × n, where n = Mᵣ(molecular) / Mᵣ(empirical)</p>
            <p><strong>Worked Example:</strong> Empirical formula CH₂, Mᵣ = 56</p>
            <ul><li>Mᵣ(CH₂) = 14</li><li>n = 56 / 14 = 4</li><li>Molecular formula = C₄H₈</li></ul>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">6</span> Calculate percentage yield, percentage composition by mass and percentage purity</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Percentage Yield:</strong> % Yield = (Actual yield / Theoretical yield) × 100</p>
            <p>Example: Actual yield = 1.6g, Theoretical = 2.0g → (1.6/2.0) × 100 = 80%</p>
            <p><strong>Percentage Composition by Mass:</strong> % of element = (Mass of element in compound / Mᵣ) × 100</p>
            <p>Example: Fe in Fe₂O₃ → (112/160) × 100 = 70%</p>
            <p><strong>Percentage Purity:</strong> % Purity = (Mass of pure substance / Total mass) × 100</p>
            <p>Example: Pure mass = 13.5g, Total = 15g → (13.5/15) × 100 = 90%</p>
            <div class="key-definition">💡 Percentage yield is always ≤ 100%. Percentage composition of all elements in a compound adds up to 100%.</div>
        </div>
    </div>
</div>

<div class="warning-box">
    <strong>⚠️ Common Mistakes to Avoid:</strong><br><br>
    • ❌ Forgetting to convert cm³ to dm³ → ✅ Always divide by 1000<br>
    • ❌ Using atomic mass instead of molecular mass for compounds → ✅ Use Mᵣ<br>
    • ❌ Confusing empirical and molecular formula → ✅ Empirical = simplest ratio; Molecular = actual atoms<br>
    • ❌ Forgetting to balance equations first → ✅ Always balance before reacting mass calculations<br>
    • ❌ Mixing up actual and theoretical yield → ✅ Actual = what you get; Theoretical = what you should get
</div>
"""

topic = Topic.objects.get(code='3')
note, created = TopicNote.objects.update_or_create(topic=topic, defaults={'content': content})
print(f"✅ Added revision notes for {topic.name}")
print("🔗 View at: https://chempassion.info/revision-notes/")