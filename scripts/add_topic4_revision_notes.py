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

<div class="main-heading">📌 Topic 4: Electrochemistry</div>

<div class="sub-heading">4.1 Electrolysis</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> Define electrolysis as the decomposition of an ionic compound, when molten or in aqueous solution, by the passage of an electric current</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Definition:</strong> Electrolysis is the <strong>decomposition</strong> of an ionic compound when <strong>molten</strong> or in <strong>aqueous solution</strong> by the passage of an <strong>electric current</strong>.</p>
            <p><strong>Why Only Ionic Compounds?</strong></p>
            <ul>
                <li><strong>Solid state:</strong> Ions are fixed in place in the lattice, cannot move → no conductivity</li>
                <li><strong>Molten or dissolved:</strong> Ions are <strong>free to move</strong> and carry charge → conducts electricity</li>
            </ul>
            <div class="key-definition">
                💡 <strong>Key Point:</strong> Covalent compounds cannot undergo electrolysis because they have no free ions or electrons to carry charge.
            </div>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">2</span> Identify in simple electrolytic cells: (a) the anode as the positive electrode, (b) the cathode as the negative electrode, (c) the electrolyte as the molten or aqueous substance that undergoes electrolysis</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Key Terms:</strong></p>
            表
                <tr style="background:#1E3A8A; color:white;"><th>Term</th><th>Definition</th><th>What it attracts</th> 表
                <tr><td><strong>Electrode</strong></td><td>Rod (metal or graphite) that conducts electricity into/out of the electrolyte</td><td>-</td></tr>
                <tr style="background:#F9FAFB;"><td><strong>Anode</strong></td><td><strong>Positive</strong> electrode</td><td>Anions (negative ions)</td></tr>
                <tr><td><strong>Cathode</strong></td><td><strong>Negative</strong> electrode</td><td>Cations (positive ions)</td></tr>
                <tr style="background:#F9FAFB;"><td><strong>Electrolyte</strong></td><td>Ionic compound in molten or dissolved solution that conducts electricity</td><td>-</td></tr>
                <tr><td><strong>Anion</strong></td><td>Negatively charged ion</td><td>Attracted to anode</td></tr>
                <tr style="background:#F9FAFB;"><td><strong>Cation</strong></td><td>Positively charged ion</td><td>Attracted to cathode</td></tr>
            表
            <div class="key-definition">
                💡 <strong>Memory Aid:</strong><br>
                • <strong>RED CAT</strong> → REDuction at CAThode<br>
                • <strong>AN OX</strong> → ANode for OXidation
            </div>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">3</span> Identify the products formed at the electrodes and describe the observations made during the electrolysis of: (a) molten lead(II) bromide, (b) concentrated aqueous sodium chloride, (c) dilute sulfuric acid using inert electrodes</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>(a) Molten Lead(II) Bromide (PbBr₂)</strong></p>
            表
                <tr style="background:#1E3A8A; color:white;"><th>Electrode</th><th>Ion</th><th>Product</th><th>Observation</th></tr>
                <tr><td>Cathode (−)</td><td>Pb²⁺</td><td>Grey lead metal</td><td>Lead deposits on electrode</td></tr>
                <tr style="background:#F9FAFB;"><td>Anode (+)</td><td>Br⁻</td><td>Brown bromine gas</td><td>Bubbling at anode, pungent smell</td></tr>
            表
            
            <p><strong>(b) Concentrated Aqueous Sodium Chloride (Brine)</strong></p>
            表
                <tr style="background:#1E3A8A; color:white;"><th>Electrode</th><th>Ion Discharged</th><th>Product</th><th>Observation</th></tr>
                <tr><td>Cathode (−)</td><td>H⁺ (from water)</td><td>Hydrogen gas</td><td>Bubbling</td></tr>
                <tr style="background:#F9FAFB;"><td>Anode (+)</td><td>Cl⁻</td><td>Chlorine gas</td><td>Bubbling, pungent smell, bleaches damp litmus</td></tr>
            表
            <p><strong>Remaining solution:</strong> Sodium hydroxide (NaOH)</p>
            
            <p><strong>(c) Dilute Sulfuric Acid (H₂SO₄)</strong></p>
            表
                <tr style="background:#1E3A8A; color:white;"><th>Electrode</th><th>Ion Discharged</th><th>Product</th><th>Observation</th></tr>
                <tr><td>Cathode (−)</td><td>H⁺</td><td>Hydrogen gas</td><td>Bubbling, squeaky pop test</td></tr>
                <tr style="background:#F9FAFB;"><td>Anode (+)</td><td>OH⁻ (from water)</td><td>Oxygen gas</td><td>Bubbling, relights glowing splint</td></tr>
            表
            <p><strong>Volume ratio:</strong> Hydrogen : Oxygen = 2 : 1</p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">4</span> State that metals or hydrogen are formed at the cathode and that non-metals (other than hydrogen) are formed at the anode</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>At the Cathode (Negative Electrode):</strong></p>
            <ul>
                <li><strong>Metals</strong> are produced (if metal ions are discharged)</li>
                <li><strong>Hydrogen</strong> is produced (if H⁺ ions are discharged)</li>
            </ul>
            <p><strong>At the Anode (Positive Electrode):</strong></p>
            <ul>
                <li><strong>Non-metals</strong> (other than hydrogen) are produced</li>
                <li>Examples: Chlorine (Cl₂), Bromine (Br₂), Iodine (I₂), Oxygen (O₂)</li>
            </ul>
            <div class="key-definition">
                💡 <strong>Rule:</strong> The product at each electrode depends on which ions are discharged first (based on reactivity).
            </div>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">5</span> Predict the identity of the products at each electrode for the electrolysis of a binary compound in the molten state</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Rule:</strong> For molten binary compounds (two elements), the products are always the elements themselves.</p>
            
            <p><strong>Worked Example 1: Molten Potassium Chloride (KCl)</strong></p>
            <ul>
                <li>Cathode: K⁺ + e⁻ → K (potassium metal)</li>
                <li>Anode: 2Cl⁻ → Cl₂ + 2e⁻ (chlorine gas)</li>
            </ul>
            
            <p><strong>Worked Example 2: Molten Magnesium Oxide (MgO)</strong></p>
            <ul>
                <li>Cathode: Mg²⁺ + 2e⁻ → Mg (magnesium metal)</li>
                <li>Anode: 2O²⁻ → O₂ + 4e⁻ (oxygen gas)</li>
            </ul>
            
            <div class="key-definition">
                💡 <strong>Key Point:</strong> The metal is always produced at the cathode; the non-metal is always produced at the anode.
            </div>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">6</span> State that metal objects are electroplated to improve their appearance and resistance to corrosion</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>What is Electroplating?</strong> Coating one metal with a layer of another metal using electrolysis.</p>
            
            <p><strong>Reasons for Electroplating:</strong></p>
            <ul>
                <li><strong>Corrosion protection:</strong> Prevents rusting/oxidation</li>
                <li><strong>Improved appearance:</strong> Makes objects look more attractive</li>
                <li><strong>Increased durability:</strong> Adds a hard, wear-resistant layer</li>
            </ul>
            
            <p><strong>Examples:</strong></p>
            <ul>
                <li><strong>Galvanising:</strong> Zinc coating on iron/steel (corrosion protection)</li>
                <li><strong>Chromium plating:</strong> On car parts (hard, shiny, corrosion resistant)</li>
                <li><strong>Silver plating:</strong> On cutlery and jewellery (appearance)</li>
                <li><strong>Gold plating:</strong> On jewellery and electronic connectors</li>
            </ul>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">7</span> Describe how metals are electroplated</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Setup for Electroplating:</strong></p>
            <ul>
                <li><strong>Cathode (−):</strong> Object to be plated</li>
                <li><strong>Anode (+):</strong> Pure metal to be plated</li>
                <li><strong>Electrolyte:</strong> Aqueous salt of the plating metal</li>
            </ul>
            
            <p><strong>Example: Plating Iron with Tin</strong></p>
            <ul>
                <li>Cathode: Iron strip (object to be plated)</li>
                <li>Anode: Tin metal</li>
                <li>Electrolyte: Tin(II) chloride solution (SnCl₂)</li>
            </ul>
            
            <p><strong>Half-Equations:</strong></p>
            <ul>
                <li>Cathode: Sn²⁺(aq) + 2e⁻ → Sn(s) (tin deposited on iron)</li>
                <li>Anode: Sn(s) → Sn²⁺(aq) + 2e⁻ (tin dissolves)</li>
            </ul>
            
            <div class="key-definition">
                💡 <strong>Key Observation:</strong> The mass of the cathode increases (metal deposited), while the mass of the anode decreases (metal dissolves).
            </div>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">8</span> Describe the transfer of charge during electrolysis to include: (a) the movement of electrons in the external circuit, (b) the loss or gain of electrons at the electrodes, (c) the movement of ions in the electrolyte <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>How Charge Flows in Electrolysis:</strong></p>
            
            <p><strong>(a) External Circuit:</strong> Electrons flow from the negative terminal of the power supply to the cathode, then from the anode back to the positive terminal.</p>
            
            <p><strong>(b) At the Electrodes:</strong></p>
            <ul>
                <li><strong>Cathode (−):</strong> Cations gain electrons → <strong>reduction</strong></li>
                <li><strong>Anode (+):</strong> Anions lose electrons → <strong>oxidation</strong></li>
            </ul>
            
            <p><strong>(c) In the Electrolyte:</strong> Ions move and carry charge</p>
            <ul>
                <li><strong>Cations (+)</strong> move towards the cathode</li>
                <li><strong>Anions (−)</strong> move towards the anode</li>
            </ul>
            
            <div class="key-definition">
                💡 <strong>Memory Aids:</strong><br>
                • <strong>OIL RIG</strong>: Oxidation Is Loss, Reduction Is Gain (of electrons)<br>
                • <strong>RED CAT</strong>: REDuction at CAThode<br>
                • <strong>AN OX</strong>: ANode for OXidation
            </div>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">9</span> Identify the products formed at the electrodes and describe the observations made during the electrolysis of aqueous copper(II) sulfate using inert carbon/graphite electrodes and when using copper electrodes <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Using Inert Electrodes (Graphite/Platinum):</strong></p>
            表
                <tr style="background:#1E3A8A; color:white;"><th>Electrode</th><th>Ion Discharged</th><th>Product</th><th>Observation</th></tr>
                <tr><td>Cathode (−)</td><td>Cu²⁺ (less reactive than H⁺)</td><td>Copper metal</td><td>Pink/brown deposit on electrode</td></tr>
                <tr style="background:#F9FAFB;"><td>Anode (+)</td><td>OH⁻ (from water)</td><td>Oxygen gas</td><td>Bubbling, relights glowing splint</td></tr>
            表
            
            <p><strong>Half-Equations:</strong></p>
            <ul>
                <li>Cathode: Cu²⁺(aq) + 2e⁻ → Cu(s)</li>
                <li>Anode: 4OH⁻(aq) → O₂(g) + 2H₂O(l) + 4e⁻</li>
            </ul>
            
            <p><strong>Using Copper Electrodes (Active Electrodes):</strong></p>
            表
                <tr style="background:#1E3A8A; color:white;"><th>Electrode</th><th>Process</th><th>Observation</th></tr>
                <tr><td>Cathode (−)</td><td>Cu²⁺ reduced to Cu</td><td><strong>Gains mass</strong> (copper deposited)</td></tr>
                <tr style="background:#F9FAFB;"><td>Anode (+)</td><td>Cu oxidised to Cu²⁺</td><td><strong>Loses mass</strong> (copper dissolves)</td></tr>
            表
            
            <p><strong>Half-Equations:</strong></p>
            <ul>
                <li>Cathode: Cu²⁺(aq) + 2e⁻ → Cu(s)</li>
                <li>Anode: Cu(s) → Cu²⁺(aq) + 2e⁻</li>
            </ul>
            
            <div class="key-definition">
                💡 <strong>Key Observation:</strong> The concentration of Cu²⁺ ions remains constant because copper dissolving at the anode replaces copper deposited at the cathode.
            </div>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">10</span> Predict the identity of the products at each electrode for the electrolysis of a halide compound in dilute or concentrated aqueous solution <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Rule for Anode Products:</strong> The concentration of the solution affects which ion is discharged at the anode.</p>
            
            表
                <tr style="background:#1E3A8A; color:white;"><th>Solution</th><th>Ions Present</th><th>Product at Anode</th><th>Reason</th></tr>
                <tr><td><strong>Concentrated halide</strong></td><td>Cl⁻, Br⁻, I⁻</td><td>Halogen gas (Cl₂, Br₂, I₂)</td><td>Halide ions are discharged</td></tr>
                <tr style="background:#F9FAFB;"><td><strong>Dilute halide</strong></td><td>Cl⁻, Br⁻, I⁻ + OH⁻</td><td>Oxygen gas</td><td>OH⁻ is discharged instead</td></tr>
            表
            
            <p><strong>Examples:</strong></p>
            <ul>
                <li><strong>Concentrated NaCl:</strong> Cl⁻ discharged → chlorine gas at anode</li>
                <li><strong>Dilute NaCl:</strong> OH⁻ discharged → oxygen gas at anode</li>
                <li><strong>Concentrated NaBr:</strong> Br⁻ discharged → bromine gas at anode</li>
                <li><strong>Dilute NaBr:</strong> OH⁻ discharged → oxygen gas at anode</li>
            </ul>
            
            <div class="key-definition">
                💡 <strong>Rule:</strong> Halide ions (Cl⁻, Br⁻, I⁻) are discharged at the anode in <strong>concentrated</strong> solutions. In dilute solutions, OH⁻ ions are discharged instead.
            </div>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">11</span> Construct ionic half-equations for reactions at the anode (to show oxidation) and at the cathode (to show reduction) <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Rules for Writing Half-Equations:</strong></p>
            <ol>
                <li>Identify the ion being discharged</li>
                <li>Determine the product formed</li>
                <li>Balance atoms and charge</li>
            </ol>
            
            <p><strong>Common Half-Equations:</strong></p>
            表
                <tr style="background:#1E3A8A; color:white;"><th>Product</th><th>Half-Equation</th><th>Type</th></tr>
                <tr><td>Hydrogen</td><td>2H⁺ + 2e⁻ → H₂</td><td>Reduction (cathode)</td></tr>
                <tr style="background:#F9FAFB;"><td>Metal (e.g., Cu)</td><td>Cu²⁺ + 2e⁻ → Cu</td><td>Reduction (cathode)</td></tr>
                <tr><td>Chlorine</td><td>2Cl⁻ → Cl₂ + 2e⁻</td><td>Oxidation (anode)</td></tr>
                <tr style="background:#F9FAFB;"><td>Bromine</td><td>2Br⁻ → Br₂ + 2e⁻</td><td>Oxidation (anode)</td></tr>
                <tr><td>Iodine</td><td>2I⁻ → I₂ + 2e⁻</td><td>Oxidation (anode)</td></tr>
                <tr style="background:#F9FAFB;"><td>Oxygen (from OH⁻)</td><td>4OH⁻ → O₂ + 2H₂O + 4e⁻</td><td>Oxidation (anode)</td></tr>
            表
            
            <p><strong>Worked Example: Molten Lead(II) Bromide</strong></p>
            <ul>
                <li>Cathode: Pb²⁺ + 2e⁻ → Pb(l)</li>
                <li>Anode: 2Br⁻ → Br₂(g) + 2e⁻</li>
            </ul>
            
            <p><strong>Worked Example: Concentrated Sodium Chloride</strong></p>
            <ul>
                <li>Cathode: 2H⁺ + 2e⁻ → H₂(g)</li>
                <li>Anode: 2Cl⁻ → Cl₂(g) + 2e⁻</li>
            </ul>
        </div>
    </div>
</div>

<div class="sub-heading">4.2 Hydrogen-oxygen fuel cells</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> State that a hydrogen-oxygen fuel cell uses hydrogen and oxygen to produce electricity with water as the only chemical product</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>What is a Fuel Cell?</strong> A fuel cell is an electrochemical cell that converts chemical energy from a fuel into electrical energy.</p>
            
            <p><strong>Hydrogen-Oxygen Fuel Cell:</strong></p>
            <ul>
                <li><strong>Fuel:</strong> Hydrogen (H₂)</li>
                <li><strong>Oxidant:</strong> Oxygen (O₂)</li>
                <li><strong>Only product:</strong> Water (H₂O)</li>
            </ul>
            
            <p><strong>Overall Reaction:</strong></p>
            <pre>2H₂(g) + O₂(g) → 2H₂O(l)</pre>
            
            <p><strong>Half-Equations:</strong></p>
            <ul>
                <li>Anode (−) : H₂(g) → 2H⁺(aq) + 2e⁻</li>
                <li>Cathode (+) : O₂(g) + 4H⁺(aq) + 4e⁻ → 2H₂O(l)</li>
            </ul>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">2</span> Describe the advantages and disadvantages of using hydrogen-oxygen fuel cells in comparison with gasoline/petrol engines in vehicles <span class="supplement-badge">Supplement</span></span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Advantages of Hydrogen Fuel Cells:</strong></p>
            <ul>
                <li>✅ Only product is <strong>water</strong> (no pollution, no CO₂)</li>
                <li>✅ Renewable (hydrogen can be produced from water)</li>
                <li>✅ Higher energy per kilogram than petrol/diesel</li>
                <li>✅ No moving parts → no power loss in transmission</li>
                <li>✅ Quieter than petrol engines (less noise pollution)</li>
            </ul>
            
            <p><strong>Disadvantages of Hydrogen Fuel Cells:</strong></p>
            <ul>
                <li>❌ Hydrogen production may use fossil fuels (releases CO₂)</li>
                <li>❌ Electrolysis of water requires large amounts of electricity</li>
                <li>❌ Expensive materials (catalysts like platinum)</li>
                <li>❌ Hydrogen is difficult and expensive to store</li>
                <li>❌ Highly flammable and explosive under pressure</li>
                <li>❌ Few hydrogen filling stations available</li>
                <li>❌ Less efficient at low temperatures</li>
            </ul>
            
            <div class="key-definition">
                💡 <strong>Comparison:</strong> Petrol engines produce CO₂, CO, and oxides of nitrogen. Fuel cells produce only water.
            </div>
        </div>
    </div>
</div>

<div class="warning-box">
    <strong>⚠️ Common Mistakes to Avoid:</strong><br><br>
    • ❌ "Electrons flow through the electrolyte" → ✅ Ions move in electrolyte; electrons flow in external circuit<br>
    • ❌ "Positive ions go to anode" → ✅ Cations (+) go to cathode (−)<br>
    • ❌ "Anode is negative" → ✅ Anode is positive (+)<br>
    • ❌ "Cathode is positive" → ✅ Cathode is negative (−)<br>
    • ❌ "OIL RIG is about oxygen" → ✅ OIL RIG is about electrons<br>
    • ❌ "Hydrogen fuel cells produce CO₂" → ✅ Only product is water<br>
    • ❌ "All metals are produced at cathode" → ✅ Only metals below hydrogen in reactivity series; hydrogen is produced for reactive metals
</div>
"""

# Add to database
topic = Topic.objects.get(code='4')
note, created = TopicNote.objects.update_or_create(
    topic=topic,
    defaults={'content': content}
)
print(f"✅ Added revision notes for {topic.name}")
print(f"📝 Content includes:")
print("   - 4.1 Electrolysis (11 points)")
print("   - 4.2 Hydrogen-oxygen fuel cells (2 points)")
print("   - Total: 13 syllabus points")
print("\n🔗 View at: https://chempassion.info/revision-notes/")