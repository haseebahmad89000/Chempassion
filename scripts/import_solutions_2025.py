import os
import sys

sys.path.append('C:\\Users\\Dell\\igcse-chemistry-platform')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chemistry_hub.settings')

import django
django.setup()

from pastpapers.models import PastPaper, Question, Solution

# Get the past paper
paper = PastPaper.objects.get(year=2025, session='o', variant=4)
print(f"Using Past Paper: {paper.code}")

# Solutions data in format: (question_number, correct_answer, explanation, examiner_tip)
solutions_data = [
    # Question 1 solutions
    ('1a', 'See table: solids - touching, uniform, vibrate; liquids - touching, random, move around; gases - apart, random, move quickly', 
     'Particle arrangement: solids have fixed positions, liquids can move past each other, gases move freely and are far apart', 
     'Remember to describe all three properties for each state'),
    
    ('1b', 'Melting, condensing/condensation, dissolving', 
     'Melting: solid to liquid; Condensation: gas to liquid; Dissolving: solid to aqueous solution', 
     'Use correct terminology for each phase change'),
    
    ('1c(i)', 'Motion / movement of particles', 
     'Gas particles move randomly and spread out from areas of high concentration to low concentration', 
     'Keywords: random motion, concentration gradient'),
    
    ('1c(ii)', 'Relative molecular mass', 
     'Lighter gases diffuse faster because they have lower relative molecular mass', 
     'Diffusion rate is inversely proportional to molecular mass'),
    
    ('1d', '1. Photochemical smog 2. Respiratory problems', 
     'Oxides of nitrogen contribute to air pollution and can cause breathing difficulties', 
     'Other answers: damages buildings, harms plants'),
    
    ('1e(i)', 'Carbon monoxide', 
     'CO is produced when there is insufficient oxygen during combustion', 
     'Carbon monoxide is toxic because it binds to haemoglobin'),
    
    ('1e(ii)', 'Nitrogen and carbon dioxide', 
     'Catalytic converters convert harmful gases into N2 and CO2', 
     'Both products are non-toxic and found naturally in air'),
    
    # Question 2 solutions
    ('2a(i)', 'Hematite', 
     'Hematite is the main iron ore containing iron(III) oxide (Fe2O3)', 
     'Other iron ores exist but hematite is most common'),
    
    ('2a(ii)', 'Burning of carbon (coke)', 
     'Coke (carbon) burns to produce heat and carbon monoxide', 
     'The reaction is exothermic and provides high temperature'),
    
    ('2a(iii)', 'Carbon monoxide', 
     'CO is the reducing agent that removes oxygen from iron oxide', 
     'Carbon monoxide is produced from incomplete combustion of coke'),
    
    ('2a(iv)', '3CO + Fe2O3 -> 2Fe + 3CO2', 
     'Carbon monoxide reduces iron(III) oxide to iron, itself being oxidized to carbon dioxide', 
     'Check balancing: 3 carbons, 3 oxygens on each side'),
    
    ('2a(v)', '1. CaCO3 -> CaO + CO2   2. CaO + SiO2 -> CaSiO3', 
     'Limestone decomposes to calcium oxide, which then reacts with silicon dioxide impurity', 
     'The product calcium silicate forms slag'),
    
    ('2b', 'Atoms of the same element that have the same number of protons but different numbers of neutrons', 
     'Isotopes have same atomic number but different mass numbers', 
     'All isotopes of iron have 26 protons'),
    
    ('2c(i)', 'Fe2+: protons 26, neutrons 28, electrons 24; Fe3+: protons 26, neutrons 32, electrons 23', 
     'For Fe2+: 54Fe2+ has 26p, 28n, 24e; For Fe3+: 58Fe3+ has 26p, 32n, 23e', 
     'Remember: electrons = protons minus charge'),
    
    ('2c(ii)', 'Add NaOH(aq) or NH3(aq) - green precipitate forms', 
     'Iron(II) ions produce a green precipitate with hydroxide ions', 
     'Precipitate may turn brown on standing as it oxidizes'),
    
    ('2d(i)', 'A substance that oxidises another substance and is itself reduced', 
     'Oxidising agents accept electrons and are reduced in the process', 
     'They cause oxidation in other substances'),
    
    ('2d(ii)', 'Loss of (one) electron', 
     'Fe2+ loses an electron to become Fe3+', 
     'Oxidation is loss of electrons (OIL RIG)'),
    
    ('2d(iii)', 'Acidified', 
     'Potassium manganate(VII) requires acidic conditions to act as an oxidising agent', 
     'Dilute sulfuric acid is commonly used'),
    
    ('2e', 'Iodine', 
     'I- reduces Fe3+ to Fe2+ and is itself oxidized to I2', 
     'The reaction produces brown iodine solution'),
    
    # Question 3 solutions
    ('3a', 'BaSO4(s) + 2NaCl(aq)', 
     'Barium sulfate is insoluble (precipitate) and sodium chloride is soluble in water', 
     'Remember state symbols: (s) for solid, (aq) for aqueous'),
    
    ('3b', '20.8 g', 
     'Mr of BaCl2 = 208; mass = moles x Mr = 0.1 x 208 = 20.8 g', 
     'Always use correct relative atomic masses'),
    
    ('3c', '80 cm3', 
     'Volume = moles / concentration = 0.100 / 1.25 = 0.08 dm3 = 80 cm3', 
     'Convert dm3 to cm3 by multiplying by 1000'),
    
    ('3d', 'White', 
     'Barium sulfate is a white precipitate', 
     'Many sulfate precipitates are white'),
    
    ('3e', 'Residue', 
     'The solid left on filter paper is called the residue; the liquid is the filtrate', 
     'Residue is collected for further processing'),
    
    ('3f', 'Rinse the residue with water; because dry residue contains sodium chloride which adds to mass', 
     'Washing removes soluble impurities (NaCl) from the precipitate', 
     'Without washing, the mass would be too high'),
    
    ('3g', 'Precipitation', 
     'This method involves mixing two solutions to form an insoluble product', 
     'Also called double decomposition'),
    
    ('3h', 'Barium nitrate; Potassium sulfate/ammonium sulfate; Barium carbonate', 
     'Any soluble barium salt works; any soluble sulfate salt; any insoluble barium salt', 
     'All must be soluble/insoluble as specified'),
    
    # Question 4 solutions
    ('4a(i)', 'H+', 
     'All acids produce hydrogen ions (protons) when dissolved in water', 
     'H+ is the common cation'),
    
    ('4a(ii)', 'Strong acid: complete dissociation; Weak acid: partial dissociation', 
     'Strong acids ionize completely; weak acids only partially dissociate', 
     'Degree of dissociation determines acid strength'),
    
    ('4a(iii)', 'Ethanoic acid', 
     'Weak acids have higher pH than strong acids of same concentration', 
     'pH is higher because fewer H+ ions are released'),
    
    ('4a(iv)', 'Colourless', 
     'Thymolphthalein is colourless in acidic solutions', 
     'It turns blue in alkaline conditions'),
    
    ('4a(v)', 'SO4 2- and CH3COO-', 
     'Sulfuric acid: H2SO4 -> 2H+ + SO4 2-; Ethanoic acid: CH3COOH -> H+ + CH3COO-', 
     'Ethanoate ion is often written as C2H3O2-'),
    
    ('4a(vi)', 'Hydrogen and oxygen', 
     'Electrolysis of dilute sulfuric acid produces H2 at cathode and O2 at anode', 
     'Water is also electrolysed because the solution is dilute'),
    
    ('4a(vii)', 'Calcium ethanoate', 
     'Calcium reacts with ethanoic acid to produce calcium ethanoate and hydrogen', 
     'Formula: (CH3COO)2Ca'),
    
    ('4b(i)', 'Proton acceptor', 
     'A base accepts H+ ions (protons) from acids', 
     'This is the Bronsted-Lowry definition'),
    
    ('4b(ii)', 'Insoluble', 
     'Al(OH)3 is not an alkali because it does not dissolve in water', 
     'Alkalis are soluble bases'),
    
    ('4b(iii)', 'Aluminium oxide', 
     'Al2O3 reacts with nitric acid to form aluminium nitrate and water', 
     'Also accepts: aluminium hydroxide'),
    
    ('4b(iv)', '+5', 
     'Al3+ = +3, O2- = -2 each, total for three NO3- = -3, each NO3- = -1, N + 3(-2) = -1, so N = +5', 
     'Work systematically through oxidation numbers'),
    
    # Question 5 solutions
    ('5a', 'Have general formula CnH2n+2; differ from one member to next by -CH2- unit', 
     'Alkanes are a homologous series with these characteristics', 
     'They show gradual change in physical properties'),
    
    ('5b(i)', 'Increases', 
     'Boiling points increase as carbon chain length increases', 
     'Due to stronger London dispersion forces'),
    
    ('5b(ii)', 'Viscosity: increases; Density: increases; Flammability: decreases', 
     'Larger alkanes are more viscous, denser, and less flammable', 
     'Any physical property showing trend is acceptable'),
    
    ('5c', 'All carbon-carbon bonds are single bonds', 
     'Saturated means no double or triple bonds', 
     'Each carbon forms four single covalent bonds'),
    
    ('5d(i)', 'Ultraviolet light', 
     'UV light provides energy to initiate radical substitution', 
     'Also accept: sunlight, light energy'),
    
    ('5d(ii)', '1-chloropropane (CH3CH2CH2Cl) and 2-chloropropane (CH3CHClCH3)', 
     'Chlorine can substitute at end carbon or middle carbon', 
     'Both are structural isomers'),
    
    ('5d(iii)', 'Compounds with the same molecular formula but different structural formulae', 
     'Structural isomers have atoms arranged differently', 
     'They have different physical and chemical properties'),
    
    # Question 6 solutions
    ('6a', 'Circle around -COO- group (two carbon atoms and two oxygen atoms)', 
     'The ester linkage is -COO- between carbonyl carbon and oxygen', 
     'Also called ester functional group'),
    
    ('6b', 'Ethyl butanoate', 
     'Butanoate from butanoic acid, ethyl from ethanol', 
     'Named as alkyl alkanoate'),
    
    ('6c', 'C3H6O', 
     'Ethyl butanoate is C6H12O2, simplified ratio 3:6:1', 
     'Divide all subscripts by 2'),
    
    ('6d(i)', 'Butanoic acid and ethanol', 
     'Esterification reaction between carboxylic acid and alcohol', 
     'Butanoic acid = C3H7COOH, ethanol = C2H5OH'),
    
    ('6d(ii)', 'Acid (concentrated H2SO4)', 
     'Sulfuric acid acts as catalyst and dehydrating agent', 
     'Also accepts: concentrated H3PO4'),
    
    ('6e', '4', 
     'Methyl butanoate, ethyl propanoate, propyl ethanoate, butyl methanoate', 
     'Four unbranched esters with formula C5H10O2'),
    
    ('6f', '2C5H10O2 + 13O2 -> 10CO2 + 10H2O', 
     'Complete combustion produces carbon dioxide and water only', 
     'Check balancing: 10 C, 20 H, 26 O on each side'),
]

print(f"\n{'='*60}")
print(f"Adding solutions to {len(solutions_data)} questions")
print(f"{'='*60}\n")

added_count = 0
for q_num, answer, explanation, tip in solutions_data:
    try:
        question = Question.objects.get(paper=paper, question_number=q_num)
        solution, created = Solution.objects.get_or_create(
            question=question,
            defaults={
                'correct_answer': answer,
                'explanation': explanation,
                'examiner_tip': tip,
                'common_mistakes': '',
                'marking_points': []
            }
        )
        if created:
            print(f"✓ Added solution: Q{q_num}")
            added_count += 1
        else:
            print(f"⊙ Solution already exists: Q{q_num}")
    except Question.DoesNotExist:
        print(f"✗ Question Q{q_num} not found!")

print(f"\n{'='*60}")
print(f"Summary: Added {added_count} new solutions")
print(f"Total solutions: {Solution.objects.count()}")