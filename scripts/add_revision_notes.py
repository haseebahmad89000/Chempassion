import os
import sys
import django

sys.path.append('C:\\Users\\Dell\\igcse-chemistry-platform')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chemistry_hub.settings')
django.setup()

from pastpapers.models import Topic, TopicNote

content_topic_1 = """
<div class="point-item">
    <div class="point-question">
        <span><strong>1.1 Point 1:</strong> State the distinguishing properties of solids, liquids and gases</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <table>
                <tr><th>Property</th><th>Solid</th><th>Liquid</th><th>Gas</th></tr>
                <tr><td>Shape</td><td>Fixed shape</td><td>Takes shape of container</td><td>Takes shape of container</td></tr>
                <tr><td>Volume</td><td>Fixed volume</td><td>Fixed volume</td><td>Fills container</td></tr>
                <tr><td>Compressibility</td><td>Very difficult</td><td>Difficult</td><td>Easy to compress</td></tr>
                <tr><td>Flow</td><td>Cannot flow</td><td>Can flow</td><td>Can flow</td></tr>
                <tr><td>Density</td><td>High</td><td>High</td><td>Low</td></tr>
            </table>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><strong>1.1 Point 2:</strong> Describe the structures of solids, liquids and gases in terms of particle separation, arrangement and motion</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <table>
                <tr><th>Property</th><th>Solid</th><th>Liquid</th><th>Gas</th></tr>
                <tr><td>Particle separation</td><td>Very close (touching)</td><td>Close (touching)</td><td>Far apart</td></tr>
                <tr><td>Arrangement</td><td>Regular pattern</td><td>Random</td><td>Random</td></tr>
                <tr><td>Motion</td><td>Vibrate in fixed positions</td><td>Move around each other</td><td>Move quickly in all directions</td></tr>
            </table>
            <pre>
SOLID:              LIQUID:              GAS:
● ● ● ●             ●  ●                ●        ●
● ● ● ●               ●    ●                      ●
● ● ● ●             ●    ●              ●        ●
(Regular)           (Random)            (Far apart)</pre>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><strong>1.1 Point 3:</strong> Describe changes of state in terms of melting, boiling, evaporating, freezing and condensing</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <table>
                <tr><th>Change</th><th>From → To</th><th>Energy</th></tr>
                <tr><td>Melting</td><td>Solid → Liquid</td><td>Heat absorbed</td></tr>
                <tr><td>Freezing</td><td>Liquid → Solid</td><td>Heat released</td></tr>
                <tr><td>Boiling</td><td>Liquid → Gas</td><td>Heat absorbed</td></tr>
                <tr><td>Evaporation</td><td>Liquid → Gas</td><td>Heat absorbed</td></tr>
                <tr><td>Condensation</td><td>Gas → Liquid</td><td>Heat released</td></tr>
            </table>
            <pre>
     Melting ↑      Boiling/Evaporation ↑
SOLID ──────────► LIQUID ──────────────► GAS
      ←──────────          ←─────────────
     Freezing ↓           Condensation ↓</pre>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><strong>1.1 Point 4:</strong> Describe the effects of temperature and pressure on the volume of a gas</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <table>
                <tr><th>Condition</th><th>Effect</th><th>Explanation</th></tr>
                <tr><td>Temperature ↑</td><td>Volume ↑</td><td>Particles gain kinetic energy, move more, push walls outward</td></tr>
                <tr><td>Temperature ↓</td><td>Volume ↓</td><td>Particles lose energy, move less, walls move inward</td></tr>
                <tr><td>Pressure ↑</td><td>Volume ↓</td><td>Particles forced closer together</td></tr>
                <tr><td>Pressure ↓</td><td>Volume ↑</td><td>Particles allowed to spread apart</td></tr>
            </table>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><strong>⭐ Supplement 1.1 Point 5:</strong> Explain changes of state using kinetic particle theory, including heating/cooling curves</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Kinetic Theory Explanation:</strong></p>
            <ul>
                <li><strong>Melting:</strong> Particles gain energy → vibrate more → overcome forces → move freely</li>
                <li><strong>Boiling:</strong> Particles gain enough energy to overcome all forces → become gas</li>
                <li><strong>Freezing:</strong> Particles lose energy → move slower → forces pull them into fixed positions</li>
                <li><strong>Condensing:</strong> Particles lose energy → move slower → forces pull them together</li>
            </ul>
            <pre>
HEATING CURVE:
Temperature
    ↑
    │                    Gas
    │                  ─────── (Boiling)
    │              Liquid + Gas
    │            ─────── (Melting)
    │        Solid + Liquid
    │      ───────────────────→ Time
    │      Solid</pre>
            <div class="key-point">
                🔑 <strong>Key Point:</strong> During a change of state, temperature remains constant. Energy goes into breaking/forming bonds between particles.
            </div>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><strong>⭐ Supplement 1.1 Point 6:</strong> Explain the effects of temperature and pressure on gas volume using kinetic particle theory</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Temperature Effect:</strong> Particles gain kinetic energy → move faster → hit walls harder → volume increases</p>
            <p><strong>Pressure Effect:</strong> External force pushes particles closer → less space → volume decreases</p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><strong>1.2 Point 1:</strong> Describe and explain diffusion in terms of kinetic particle theory</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <p><strong>Definition:</strong> Diffusion is the net movement of particles from a region of higher concentration to a region of lower concentration, until evenly distributed.</p>
            <p><strong>Explanation:</strong> Particles are in constant random motion. They move from areas where there are many particles to areas where there are fewer. This continues until particles are evenly spread.</p>
            <p><strong>Examples:</strong> Perfume spreading across a room, food coloring in water, oxygen entering blood in lungs.</p>
        </div>
    </div>
</div>

<div class="point-item">
    <div class="point-question">
        <span><strong>⭐ Supplement 1.2 Point 2:</strong> Explain the effect of relative molecular mass on the rate of diffusion of gases</span>
        <span class="icon">▼</span>
    </div>
    <div class="point-answer">
        <div class="answer-content">
            <table>
                <tr><th>Gas</th><th>Mr</th><th>Relative Rate</th></tr>
                <tr><td>Hydrogen (H₂)</td><td>2</td><td>Very fast</td></tr>
                <tr><td>Helium (He)</td><td>4</td><td>Fast</td></tr>
                <tr><td>Oxygen (O₂)</td><td>32</td><td>Slow</td></tr>
                <tr><td>Carbon dioxide (CO₂)</td><td>44</td><td>Very slow</td></tr>
            </table>
            <p><strong>Formula:</strong> Rate ∝ 1/√Mr</p>
            <p><strong>Explanation:</strong> At the same temperature, all gas particles have the same average kinetic energy (KE = ½mv²). Lighter particles must move faster, so they diffuse faster.</p>
        </div>
    </div>
</div>

<div class="key-point">
    🧪 <strong>Summary:</strong> Solids have fixed shape and volume with regular particle arrangement. Liquids take shape of container with random particle arrangement. Gases fill any container with particles far apart and moving randomly.
</div>
"""

# Save to database
topic = Topic.objects.get(code='1')
note, created = TopicNote.objects.update_or_create(
    topic=topic,
    defaults={'content': content_topic_1}
)
print(f"✅ Updated revision notes for {topic.name}")
print("📝 Content now uses click-to-reveal format")
print("🔗 View at: https://chempassion.info/revision-notes/")