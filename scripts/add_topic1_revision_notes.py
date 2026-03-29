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

<div class="main-heading">📌 Topic 1: States of Matter</div>

<div class="sub-heading">1.1 Solids, liquids and gases</div>

<div class="point-item">
    <div class="point-question">
        <span><span class="point-number">1</span> State the distinguishing properties of solids, liquids and gases</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <table>
                <tr><th>Property</th><th>Solid</th><th>Liquid</th><th>Gas</th></tr>
                <tr><td><strong>Shape</strong></td><td>Fixed shape</td><td>Takes shape of container</td><td>Takes shape of container</td></tr>
                <tr><td><strong>Volume</strong></td><td>Fixed volume</td><td>Fixed volume</td><td>Fills container completely</td></tr>
                <tr><td><strong>Compressibility</strong></td><td>Very difficult to compress</td><td>Difficult to compress</td><td>Easy to compress</td></tr>
                <tr><td><strong>Flow</strong></td><td>Does not flow</td><td>Flows freely</td><td>Flows freely</td></tr>
                <tr><td><strong>Density</strong></td><td>High density</td><td>High density</td><td>Very low density</td></tr>
            </table>
            <div class="key-definition">
                🔑 <strong>Key Understanding:</strong> Solids keep their shape because particles are held tightly in fixed positions. Liquids flow because particles can slide past each other. Gases spread out to fill any container because particles move rapidly in all directions.
            </div>
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
            <table>
                <tr><th>Property</th><th>Solid</th><th>Liquid</th><th>Gas</th></tr>
                <tr><td><strong>Particle separation</strong></td><td>Very close (touching)</td><td>Close (touching)</td><td>Far apart (large spaces)</td></tr>
                <tr><td><strong>Arrangement</strong></td><td>Regular, repeating pattern</td><td>Random, irregular</td><td>Random, irregular</td></tr>
                <tr><td><strong>Motion</strong></td><td>Vibrate in fixed positions</td><td>Move around each other</td><td>Move rapidly in all directions</td></tr>
            </table>
            <pre>
SOLID                    LIQUID                    GAS
  ●   ●   ●               ●    ●                  ●        ●
    ●   ●                   ●    ●                       ●
  ●   ●   ●               ●    ●                  ●        ●
(Regular pattern)      (Random arrangement)   (Far apart, random)</pre>
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
            <table>
                <tr><th>Change</th><th>From → To</th><th>Energy Change</th></tr>
                <tr><td><strong>Melting</strong></td><td>Solid → Liquid</td><td>Heat absorbed (endothermic)</td></tr>
                <tr><td><strong>Freezing</strong></td><td>Liquid → Solid</td><td>Heat released (exothermic)</td></tr>
                <tr><td><strong>Boiling</strong></td><td>Liquid → Gas</td><td>Heat absorbed (endothermic)</td></tr>
                <tr><td><strong>Evaporation</strong></td><td>Liquid → Gas</td><td>Heat absorbed (endothermic)</td></tr>
                <tr><td><strong>Condensation</strong></td><td>Gas → Liquid</td><td>Heat released (exothermic)</td></tr>
                <tr><td><strong>Sublimation</strong></td><td>Solid → Gas</td><td>Heat absorbed (endothermic)</td></tr>
            </table>
            <pre>
     Melting ↑      Boiling/Evaporation ↑
SOLID ──────────► LIQUID ──────────────► GAS
      ←──────────          ←─────────────
     Freezing ↓           Condensation ↓</pre>
            <div class="key-definition">
                💡 <strong>Important Notes:</strong><br>
                • Melting point = Freezing point (same temperature)<br>
                • Boiling point is specific for each substance<br>
                • Evaporation occurs at any temperature, only at the surface<br>
                • Boiling occurs throughout the liquid at a specific temperature
            </div>
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
            <table>
                <tr><th>Condition</th><th>Effect</th><th>Explanation</th></tr>
                <tr><td><strong>Temperature ↑</strong></td><td>Volume increases</td><td>Particles gain kinetic energy, move faster, collide with walls more forcefully, pushing outward</td></tr>
                <tr><td><strong>Temperature ↓</strong></td><td>Volume decreases</td><td>Particles lose energy, move slower, collisions become weaker, volume contracts</td></tr>
                <tr><td><strong>Pressure ↑</strong></td><td>Volume decreases</td><td>External force pushes particles closer together, reducing space between them</td></tr>
                <tr><td><strong>Pressure ↓</strong></td><td>Volume increases</td><td>Particles are allowed to spread apart into larger space</td></tr>
            </table>
            <div class="warning-box">
                ⚠️ <strong>Common Mistake Alert:</strong> Particles do NOT expand when heated. The particles themselves stay the same size; they just move more and take up more space.
            </div>
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
            <p><strong>How Energy Affects Particles:</strong></p>
            <table>
                <tr><th>Process</th><th>What Happens to Particles</th></tr>
                <tr><td><strong>Melting</strong></td><td>Particles absorb energy → vibrate more → forces between particles weaken → particles can move past each other</td></tr>
                <tr><td><strong>Boiling</strong></td><td>Particles gain enough energy to overcome all attractive forces → escape as gas</td></tr>
                <tr><td><strong>Freezing</strong></td><td>Particles lose energy → move slower → forces pull them into fixed positions</td></tr>
                <tr><td><strong>Condensing</strong></td><td>Particles lose energy → slow down → forces pull them together into liquid</td></tr>
            </table>
            <pre>
HEATING CURVE:
Temperature
    ↑
    │                                    Gas
    │                                  ─────── (Boiling point)
    │                              Liquid + Gas
    │                            ─────── (Melting point)
    │                        Solid + Liquid
    │      ───────────────────────────────────→ Time
    │      Solid</pre>
            <div class="key-definition">
                🔑 <strong>Key Points:</strong><br>
                • Flat sections (plateaus) = change of state occurring<br>
                • During a change of state, temperature remains constant<br>
                • All energy goes into breaking or forming bonds between particles
            </div>
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
            <p><strong>Temperature Effect:</strong><br>
            Increasing temperature → particles gain kinetic energy → particles move faster and collide with container walls more frequently → each collision has more force → volume increases (if container can expand)</p>
            <p><strong>Pressure Effect:</strong><br>
            Increasing external pressure → particles are forced closer together → same number of particles in smaller space → volume decreases → particles hit walls more frequently but over smaller area</p>
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
            <p><strong>Definition:</strong> Diffusion is the net movement of particles from an area of higher concentration to an area of lower concentration until evenly spread.</p>
            <p><strong>Explanation Using Kinetic Theory:</strong><br>
            • Particles are in constant random motion<br>
            • They move from areas where there are many particles to areas where there are fewer<br>
            • This continues until particles are evenly distributed (equilibrium)</p>
            <p><strong>Examples:</strong><br>
            • Perfume spreading across a room<br>
            • Food coloring dispersing in water<br>
            • Oxygen entering blood in lungs</p>
            <div class="key-definition">
                💡 <strong>Key Fact:</strong> Diffusion happens without any energy input. Higher temperatures speed up diffusion because particles have more kinetic energy.
            </div>
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
            <table>
                <tr><th>Gas</th><th>Relative Molecular Mass (Mr)</th><th>Diffusion Rate</th></tr>
                <tr><td>Hydrogen (H₂)</td><td>2</td><td>Fastest</td></tr>
                <tr><td>Helium (He)</td><td>4</td><td>Very fast</td></tr>
                <tr><td>Water vapour (H₂O)</td><td>18</td><td>Moderate</td></tr>
                <tr><td>Oxygen (O₂)</td><td>32</td><td>Slow</td></tr>
                <tr><td>Carbon dioxide (CO₂)</td><td>44</td><td>Slower</td></tr>
                <tr><td>Chlorine (Cl₂)</td><td>71</td><td>Very slow</td></tr>
            </table>
            <p><strong>Explanation:</strong><br>
            • At the same temperature, all gas particles have the same average kinetic energy<br>
            • Kinetic energy = ½ × mass × velocity²<br>
            • Therefore: velocity² ∝ 1/mass<br>
            • Lighter particles (lower Mr) move faster<br>
            • Faster particles → faster diffusion</p>
            <div class="key-definition">
                🧪 <strong>Classic Experiment:</strong> Ammonia (Mr = 17) and hydrogen chloride (Mr = 36.5) diffuse in opposite directions. Ammonia travels faster, so the white ring of ammonium chloride forms closer to the hydrogen chloride end.
            </div>
        </div>
    </div>
</div>

<div class="warning-box">
    <strong>⚠️ Common Mistakes to Avoid:</strong><br><br>
    • ❌ "Particles expand when heated" → ✅ Particles gain energy and move more, but they do NOT expand<br>
    • ❌ "Space between particles is filled with air" → ✅ Space between particles is empty (vacuum)<br>
    • ❌ "Particles change state" → ✅ The SUBSTANCE changes state due to particle energy changes<br>
    • ❌ "Diffusion requires energy" → ✅ Diffusion happens naturally due to random motion<br>
    • ❌ "Gases with higher Mr diffuse faster" → ✅ Gases with LOWER Mr diffuse faster
</div>
"""

# Add to database
topic = Topic.objects.get(code='1')
note, created = TopicNote.objects.update_or_create(
    topic=topic,
    defaults={'content': content}
)
print(f"✅ Added revision notes for {topic.name}")
print(f"📝 Content includes:")
print("   - 1.1 Solids, liquids and gases (6 points)")
print("   - 1.2 Diffusion (2 points)")
print("   - Examiner tips and common mistakes")
print("\n🔗 View at: https://chempassion.info/revision-notes/")