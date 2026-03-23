import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chemistry_hub.settings')
django.setup()

from pastpapers.models import Topic, TopicNote

# Complete content for Topic 1: States of Matter
content_topic_1 = """
<h1>📖 Topic 1: States of Matter</h1>

<div style="background: #f0f7ff; padding: 15px; border-radius: 12px; margin-bottom: 20px;">
    <p style="font-size: 1.1rem;">🔬 Click on any section to expand and learn!</p>
</div>

---

## 📌 1.1 Solids, Liquids and Gases

### Point 1: Properties of Solids, Liquids and Gases

<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
    <thead>
        <tr style="background: #2e7d32; color: white;">
            <th style="padding: 12px;">Property</th>
            <th style="padding: 12px;">🔷 Solid</th>
            <th style="padding: 12px;">💧 Liquid</th>
            <th style="padding: 12px;">💨 Gas</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px;"><strong>Shape</strong></td>
            <td style="padding: 10px;">✅ Fixed shape</td>
            <td style="padding: 10px;">📦 Takes shape of container</td>
            <td style="padding: 10px;">📦 Takes shape of container</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee; background: #f9f9f9;">
            <td style="padding: 10px;"><strong>Volume</strong></td>
            <td style="padding: 10px;">✅ Fixed volume</td>
            <td style="padding: 10px;">✅ Fixed volume</td>
            <td style="padding: 10px;">🌀 Fills container</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px;"><strong>Compressibility</strong></td>
            <td style="padding: 10px;">❌ Very difficult</td>
            <td style="padding: 10px;">⚠️ Difficult</td>
            <td style="padding: 10px;">✅ Easy to compress</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee; background: #f9f9f9;">
            <td style="padding: 10px;"><strong>Flow</strong></td>
            <td style="padding: 10px;">❌ Cannot flow</td>
            <td style="padding: 10px;">✅ Can flow</td>
            <td style="padding: 10px;">✅ Can flow</td>
        </tr>
        <tr>
            <td style="padding: 10px;"><strong>Density</strong></td>
            <td style="padding: 10px;">🔺 High</td>
            <td style="padding: 10px;">🔺 High</td>
            <td style="padding: 10px;">🔻 Low</td>
        </tr>
    </tbody>
</table>

---

### Point 2: Particle Structure

<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-top: 10px;">
    <thead>
        <tr style="background: #2e7d32; color: white;">
            <th style="padding: 12px;">Property</th>
            <th style="padding: 12px;">🔷 Solid</th>
            <th style="padding: 12px;">💧 Liquid</th>
            <th style="padding: 12px;">💨 Gas</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px;"><strong>Particle separation</strong></td>
            <td style="padding: 10px;">🔴🔴 Very close (touching)</td>
            <td style="padding: 10px;">🔴🔴 Close (touching)</td>
            <td style="padding: 10px;">🔴     🔴 Far apart</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee; background: #f9f9f9;">
            <td style="padding: 10px;"><strong>Arrangement</strong></td>
            <td style="padding: 10px;">📐 Regular pattern</td>
            <td style="padding: 10px;">🎲 Random</td>
            <td style="padding: 10px;">🎲 Random</td>
        </tr>
        <tr>
            <td style="padding: 10px;"><strong>Motion</strong></td>
            <td style="padding: 10px;">⚡ Vibrate in fixed positions</td>
            <td style="padding: 10px;">🌀 Move around each other</td>
            <td style="padding: 10px;">💨 Move quickly in all directions</td>
        </tr>
    </tbody>
</table>

#### 🎨 Visual Diagram:

<pre style="background: #f8f9fa; padding: 15px; border-radius: 12px; font-family: monospace; font-size: 14px;">
<strong>🔷 SOLID                    💧 LIQUID                   💨 GAS</strong>
  ●  ●  ●  ●                  ●  ●                       ●        ●
  ●  ●  ●  ●                    ●     ●                         ●
  ●  ●  ●  ●                  ●     ●                   ●        ●
  (Regular pattern)          (Random arrangement)      (Far apart, random)
</pre>

---

### Point 3: Changes of State

<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
    <thead>
        <tr style="background: #2e7d32; color: white;">
            <th style="padding: 12px;">Change</th>
            <th style="padding: 12px;">From → To</th>
            <th style="padding: 12px;">Energy</th>
        </tr>
    </thead>
    <tbody>
        <tr><td style="padding: 10px;"><strong>🧊 Melting</strong></td><td style="padding: 10px;">Solid → Liquid</td><td style="padding: 10px;">🔥 Heat absorbed</td></tr>
        <tr style="background: #f9f9f9;"><td style="padding: 10px;"><strong>❄️ Freezing</strong></td><td style="padding: 10px;">Liquid → Solid</td><td style="padding: 10px;">🌡️ Heat released</td></tr>
        <tr><td style="padding: 10px;"><strong>💨 Boiling</strong></td><td style="padding: 10px;">Liquid → Gas</td><td style="padding: 10px;">🔥 Heat absorbed</td></tr>
        <tr style="background: #f9f9f9;"><td style="padding: 10px;"><strong>💧 Evaporation</strong></td><td style="padding: 10px;">Liquid → Gas</td><td style="padding: 10px;">🔥 Heat absorbed</td></tr>
        <tr><td style="padding: 10px;"><strong>☁️ Condensation</strong></td><td style="padding: 10px;">Gas → Liquid</td><td style="padding: 10px;">🌡️ Heat released</td></tr>
        <tr style="background: #f9f9f9;"><td style="padding: 10px;"><strong>✨ Sublimation</strong></td><td style="padding: 10px;">Solid → Gas</td><td style="padding: 10px;">🔥 Heat absorbed</td></tr>
    </tbody>
</table>

#### 📊 Visual Diagram:

<pre style="background: #f8f9fa; padding: 15px; border-radius: 12px; font-family: monospace;">
          🔥 Melting ↑           🔥 Boiling/Evaporation ↑
    🔷 SOLID ──────────► 💧 LIQUID ──────────────► 💨 GAS
          ←──────────                ←─────────────
          ❄️ Freezing ↓             ☁️ Condensation ↓
</pre>

---

### Point 4: Effect of Temperature and Pressure on Gas Volume

<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
    <thead>
        <tr style="background: #2e7d32; color: white;">
            <th style="padding: 12px;">Condition</th>
            <th style="padding: 12px;">Effect</th>
            <th style="padding: 12px;">Explanation</th>
        </tr>
    </thead>
    <tbody>
        <tr><td style="padding: 10px;"><strong>🌡️ Temperature ↑</strong></td><td style="padding: 10px;">📈 Volume ↑</td><td style="padding: 10px;">Particles gain kinetic energy, move more, push walls outward</td></tr>
        <tr style="background: #f9f9f9;"><td style="padding: 10px;"><strong>🌡️ Temperature ↓</strong></td><td style="padding: 10px;">📉 Volume ↓</td><td style="padding: 10px;">Particles lose energy, move less, walls move inward</td></tr>
        <tr><td style="padding: 10px;"><strong>⚡ Pressure ↑</strong></td><td style="padding: 10px;">📉 Volume ↓</td><td style="padding: 10px;">Particles forced closer together</td></tr>
        <tr style="background: #f9f9f9;"><td style="padding: 10px;"><strong>⚡ Pressure ↓</strong></td><td style="padding: 10px;">📈 Volume ↑</td><td style="padding: 10px;">Particles allowed to spread apart</td></tr>
    </tbody>
</table>

---

<div style="background: #fff3e0; padding: 15px; border-radius: 12px; border-left: 4px solid #ff9800; margin: 20px 0;">
<h3>⭐ SUPPLEMENT CONTENT (For A* - C Grades)</h3>
</div>

---

### Point 5: Heating and Cooling Curves

<pre style="background: #f8f9fa; padding: 15px; border-radius: 12px; font-family: monospace;">
<strong>HEATING CURVE:</strong>
Temperature
    ↑
    │                                    💨 Gas
    │                                  ─────── (Boiling)
    │                              💧 Liquid + Gas
    │                            ─────── (Melting)
    │                        🔷 Solid + Liquid
    │      ───────────────────────────────────→ Time
    │      🔷 Solid

<strong>KEY POINTS:</strong>
• Flat sections = change of state occurring
• Temperature constant during change of state
• Energy used to overcome or form particle forces
</pre>

---

### Point 6: Particle Explanation of Temperature and Pressure Effects

<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden;">
    <thead><tr style="background: #ff9800; color: white;"><th style="padding: 12px;">Effect</th><th style="padding: 12px;">Particle Explanation</th></tr></thead>
    <tbody>
        <tr><td style="padding: 10px;"><strong>🌡️ Temperature ↑</strong></td><td style="padding: 10px;">Particles gain kinetic energy → move faster → hit walls harder → volume increases</td></tr>
        <tr style="background: #f9f9f9;"><td style="padding: 10px;"><strong>⚡ Pressure ↑</strong></td><td style="padding: 10px;">External force pushes particles closer → less space → volume decreases</td></tr>
    </tbody>
</table>

---

## 📌 1.2 Diffusion

### Point 1: Diffusion

<div style="background: #e8f5e9; padding: 15px; border-radius: 12px; margin: 10px 0;">
<strong>🧪 Definition:</strong> Movement of particles from high concentration to low concentration
</div>

<strong>📝 Examples:</strong>
<ul>
    <li>🌸 Perfume spreading across a room</li>
    <li>🎨 Food coloring in water</li>
    <li>🫁 Oxygen entering blood in lungs</li>
</ul>

---

### Point 2: Effect of Relative Molecular Mass on Diffusion Rate (Supplement)

<table style="width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden;">
    <thead><tr style="background: #ff9800; color: white;"><th style="padding: 12px;">Gas</th><th style="padding: 12px;">Mr</th><th style="padding: 12px;">Relative Rate</th></tr></thead>
    <tbody>
        <tr><td style="padding: 10px;">Hydrogen (H₂)</td><td style="padding: 10px;">2</td><td style="padding: 10px;">⚡ Very fast</td></tr>
        <tr style="background: #f9f9f9;"><td style="padding: 10px;">Helium (He)</td><td style="padding: 10px;">4</td><td style="padding: 10px;">⚡ Fast</td></tr>
        <tr><td style="padding: 10px;">Oxygen (O₂)</td><td style="padding: 10px;">32</td><td style="padding: 10px;">🐢 Slow</td></tr>
        <tr style="background: #f9f9f9;"><td style="padding: 10px;">Carbon dioxide (CO₂)</td><td style="padding: 10px;">44</td><td style="padding: 10px;">🐢 Very slow</td></tr>
    </tbody>
</table>

<div style="background: #fff3e0; padding: 12px; border-radius: 12px; margin-top: 10px;">
<strong>📐 Formula:</strong> Rate ∝ 1/√Mr<br>
<strong>💡 Explanation:</strong> At same temperature, all particles have same average kinetic energy (KE = ½mv²). Lighter particles must move faster, so they diffuse faster.
</div>

---

## 🎨 Complete Visual Summary

<pre style="background: #f0f7ff; padding: 20px; border-radius: 16px; font-family: monospace; border: 2px solid #2e7d32;">
┌─────────────────────────────────────────────────────────────────────┐
│                      🌡️ STATES OF MATTER 🌡️                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   🔷 SOLID                 💧 LIQUID                 💨 GAS          │
│   ┌─────────┐             ┌─────────┐             ┌─────────┐       │
│   │ ●  ●  ● │             │ ●    ● │             │ ●      ● │       │
│   │ ●  ●  ● │             │   ●    │             │    ●    │       │
│   │ ●  ●  ● │             │ ●    ● │             │ ●      ● │       │
│   └─────────┘             └─────────┘             └─────────┘       │
│   ✅ Fixed shape          📦 Takes shape          🌀 Fills container │
│   ✅ Fixed volume         ✅ Fixed volume         ❌ No fixed volume │
│   ❌ Cannot flow          ✅ Can flow             ✅ Can flow        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

📊 Key Relationship: Temperature ↑ → Particle Energy ↑ → Volume ↑
⚡ Key Relationship: Pressure ↑ → Particle Space ↓ → Volume ↓
</pre>

---

<hr style="margin: 30px 0;">

<p style="text-align: center; color: #2e7d32; font-weight: bold;">
    🧪 Remember: Click on any section in the revision notes to expand and learn! 🧪
</p>
"""

# Add to database
try:
    topic = Topic.objects.get(code='1')
    note, created = TopicNote.objects.update_or_create(
        topic=topic,
        defaults={'content': content_topic_1}
    )
    if created:
        print(f"✅ Added revision notes for {topic.name}")
    else:
        print(f"✅ Updated revision notes for {topic.name}")
    print(f"📝 Content length: {len(content_topic_1)} characters")
except Topic.DoesNotExist:
    print("❌ Topic 1 not found! Adding all topics first...")
    print("   Run scripts/add_topics.py first if topics are missing.")

print("\n✨ Done! Refresh your website to see the revision notes.")
print("🔗 Go to: https://chempassion.info/revision-notes/")