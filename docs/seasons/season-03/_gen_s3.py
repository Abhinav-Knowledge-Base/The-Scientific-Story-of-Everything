#!/usr/bin/env python3
"""Generate Season 3 Phase 3 detailed episode treatments."""
from pathlib import Path

OUT = Path(__file__).resolve().parent / "episodes"
OUT.mkdir(parents=True, exist_ok=True)


def md_table(rows, headers):
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for r in rows:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


def render(ep, next_title):
    goals = "\n".join(f"{i}. {g}" for i, g in enumerate(ep["goals"], 1))
    acts = md_table(ep["acts"], ["Act", "Function"])
    beats = "\n\n".join(f"**{b[0]}**  \n{b[1]}" for b in ep["beats"])
    evidence = md_table(ep["evidence"], ["Claim", "Ladder"])
    myths = md_table(ep["myths"], ["Myth", "Correction"])
    debates = "\n".join(f"- {d}" for d in ep["debates"])
    visuals = "\n".join(f"{i}. {v}" for i, v in enumerate(ep["visuals"], 1))
    terms = "\n".join(f"- {t}" for t in ep["terms"])
    dont = "\n".join(f"- {d}" for d in ep["dont"])
    if ep["n"] == 30:
        handoff = (
            "→ **Season 4 — Frontiers** (unfinished questions, futures, meaning, coda)\n\n"
            "Season 3 complete — human depth map finished."
        )
    else:
        handoff = f"→ **S3E{ep['n']+1:02d} {next_title}**"

    return f"""# S3E{ep['n']:02d} — {ep['title']}

**Season:** 3 — The Human Story  
**Series question:** *How did we get here?* (human depth)  
**Logline:** {ep['logline']}

**Phase 1 outline:** [../../season-03-the-human-story.md](../../season-03-the-human-story.md) (Episode {ep['n']})  
**Comes from:** {ep['from_ep']}  
**Goes to:** {ep['to_ep']}  
**Deepens:** {ep['deepens']}

---

## Learning goals

{goals}

---

## Suggested shape

{acts}

---

## Beat sheet

{beats}

---

## Evidence ladder

{evidence}

---

## Misconceptions to kill

{myths}

---

## Debate / open questions

{debates}

**Further depth / related:** {ep['s_pointer']}

---

## Visual set-pieces

{visuals}

---

## Terms

{terms}

---

## Do not claim

{dont}

---

## Honesty beat (closing card)

**Known:** See Established rows above.  
**Unknown:** See Active debate / Unknown rows and open questions.  
**Better evidence:** Sharper fossils, genomes, archaeology, and historical sources.

---

## Baton handoff

{handoff}
"""


def make(**kwargs):
    return kwargs


EPS = [
    make(
        n=1,
        slug="primates-among-mammals",
        title="Primates Among Mammals",
        logline="Place humans inside the primate radiation without special pleading—trees, not ladders.",
        from_ep="Season 2 close / Season 1 Episode 23 baton",
        to_ep="S3E02 Becoming Bipedal",
        deepens="S1 Ep. 23",
        goals=[
            "Locate humans among primates and apes without special pleading.",
            "Kill ladder thinking early and permanently for the season.",
            "Compare sociality and ecology across living primates.",
            "Hand off to bipedalism as the next anatomical experiment.",
        ],
        acts=[
            ("Cold open", "March-of-progress image smashed"),
            ("Act I", "Primate traits in ecological context"),
            ("Act II", "Ape diversity and radiation"),
            ("Act III", "Anti-ladder: our path is one experiment"),
            ("Act IV", "Baton → upright walking"),
        ],
        beats=[
            ("Cold open", "Classic ladder graphic collapses into a branching primate tree."),
            ("Act I", "Hands, vision, and social brains as primate packages—not destiny markers."),
            ("Act II", "Living ape diversity: different solutions, shared ancestry."),
            ("Act III", "Humans sit on one branch; chimpanzees are cousins, not ancestors."),
            ("Act IV", "Next: standing up reshapes the body and the niche."),
        ],
        evidence=[
            ("Common ancestry of humans and other apes", "Established"),
            ("Exact last common ancestor anatomy", "Incomplete / Active debate"),
            ("Drivers of ape intelligence", "Active debate"),
        ],
        myths=[
            ("We evolved from modern chimpanzees", "Shared ancestor; both lineages changed"),
            ("Primates form a ladder to humans", "Branching radiation"),
        ],
        debates=[
            "Relationships among Miocene ape fossils",
            "Which ecological pressures most shaped ape cognition",
        ],
        visuals=[
            "Primate family tree with humans as one tip",
            "Canopy-to-ground camera among living primates",
            "Ladder graphic crossed out → tree graphic",
        ],
        terms=["Primate", "Ape", "Common ancestry", "Radiation"],
        dont=[
            "Do not narrate a ladder culminating in humans.",
            "Do not treat chimpanzees as living fossils of our past.",
        ],
        s_pointer="S1E23; continues into S3E02.",
    ),
    make(
        n=2,
        slug="becoming-bipedal",
        title="Becoming Bipedal",
        logline="Walking upright—early, costly, mosaic; competing hypotheses get scorecards, not slogans.",
        from_ep="S3E01 Primates Among Mammals",
        to_ep="S3E03 Tools, Fire, and Expanding Niches",
        deepens="S1 Ep. 23",
        goals=[
            "Show the anatomical package of bipedalism.",
            "Use trackways and fossils as primary evidence.",
            "Score competing why-hypotheses without crowning a winner.",
            "Emphasize mosaic timing: walking before big brains.",
            "Hand off to tools and fire as niche expanders.",
        ],
        acts=[
            ("Cold open", "Footprints in ash"),
            ("Act I", "Anatomy of upright walking"),
            ("Act II", "Why—hypothesis scorecards"),
            ("Act III", "Mosaic evolution"),
            ("Act IV", "Baton → technology as ecology"),
        ],
        beats=[
            ("Cold open", "Laetoli-style tracks: bipedal gait preserved in volcanic ash."),
            ("Act I", "Pelvis, feet, spine, and energetics—costs and benefits."),
            ("Act II", "Energy, carrying, heat, habitat: Active debate, not settled story."),
            ("Act III", "Traits arrive out of order; walking often precedes large brains."),
            ("Act IV", "Next: tools and fire expand what bodies can do."),
        ],
        evidence=[
            ("Early hominins were bipedal", "Established"),
            ("A single proven primary cause of bipedalism", "Active debate"),
            ("Exact mosaic sequence across all lineages", "Incomplete"),
        ],
        myths=[
            ("Big brains evolved first, then walking", "Walking is often earlier"),
            ("One neat adaptive story explains bipedalism", "Multiple hypotheses remain open"),
        ],
        debates=[
            "Primary drivers of bipedalism",
            "How many independent bipedal experiments existed",
        ],
        visuals=[
            "Skeleton overlays: ape → early hominin → modern",
            "Hypothesis cards with evidence chips",
            "Trackway reconstruction walk",
        ],
        terms=["Bipedalism", "Hominin", "Mosaic evolution", "Trackway"],
        dont=[
            "Do not sell a single-cause slogan as established fact.",
            "Do not imply bipedalism instantly produced modernity.",
        ],
        s_pointer="S1E23 depth; leads to S3E03.",
    ),
    make(
        n=3,
        slug="tools-fire-and-expanding-niches",
        title="Tools, Fire, and Expanding Niches",
        logline="Stone tools and contested fire control—technology becomes ecology long before Homo sapiens.",
        from_ep="S3E02 Becoming Bipedal",
        to_ep="S3E04 Homo erectus and the First Cosmopolitan Humans",
        deepens="S1 Ep. 23–24",
        goals=[
            "Survey early stone-tool industries accessibly.",
            "Show butchery and ranging evidence tied to technology.",
            "Separate opportunistic fire from controlled fire with evidence standards.",
            "Introduce social learning as the transmission channel.",
            "Hand off to long-lived cosmopolitan Homo.",
        ],
        acts=[
            ("Cold open", "Knapping sparks at dusk"),
            ("Act I", "Stone tools"),
            ("Act II", "Fire debates"),
            ("Act III", "Niche expansion"),
            ("Act IV", "Baton → erectus world"),
        ],
        beats=[
            ("Cold open", "A flake strikes; night work becomes possible—or does it? Evidence check."),
            ("Act I", "Oldowan and Acheulean as archaeological packages, not genius myths."),
            ("Act II", "What counts as controlled fire; dates remain contested."),
            ("Act III", "Diet, defense, and range expand with technology."),
            ("Act IV", "Next: wide-ranging Homo erectus."),
        ],
        evidence=[
            ("Ancient stone-tool use by hominins", "Established"),
            ("Early controlled fire timelines", "Active debate"),
            ("Social learning transmitting skills", "Strong inference / Established broad"),
        ],
        myths=[
            ("One inventor discovered tools/fire", "Gradual, multi-lineage patterns"),
            ("Fire control is settled for earliest sites", "Standards and dates contested"),
        ],
        debates=[
            "Earliest secure controlled fire",
            "Cognitive requirements for early industries",
        ],
        visuals=[
            "Knapping close-ups and cut-mark forensics",
            "Hearth vs wildfire evidence checklist",
            "Range maps expanding with tech",
        ],
        terms=["Oldowan", "Acheulean", "Social learning", "Niche construction"],
        dont=[
            "Do not romanticize a first inventor.",
            "Do not treat all burned sediment as controlled fire.",
        ],
        s_pointer="S1E23–24; continues to S3E04.",
    ),
    make(
        n=4,
        slug="homo-erectus-and-the-first-cosmopolitan-humans",
        title="Homo erectus and the First Cosmopolitan Humans",
        logline="A long-lived human species spreads across Africa and Eurasia—duration that challenges sapiens-centrism.",
        from_ep="S3E03 Tools, Fire, and Expanding Niches",
        to_ep="S3E05 Neanderthals, Denisovans, and Other Humans",
        deepens="S1 Ep. 24",
        goals=[
            "Show geographic range and longevity of erectus-grade humans.",
            "Outline body and technology packages cautiously.",
            "Flag naming/lumping debates without derailing the story.",
            "Hand off to other archaic humans.",
        ],
        acts=[
            ("Cold open", "Duration bar vs sapiens"),
            ("Act I", "Anatomy and range"),
            ("Act II", "Lifeways"),
            ("Act III", "Naming debates"),
            ("Act IV", "Baton → other humans"),
        ],
        beats=[
            ("Cold open", "Erectus-grade humans endure far longer than sapiens has so far."),
            ("Act I", "Africa-to-Eurasia sites as a cosmopolitan map."),
            ("Act II", "Endurance, tools, and social life—inferred carefully."),
            ("Act III", "Lumpers vs splitters: taxonomy as working language."),
            ("Act IV", "Next: Neanderthals, Denisovans, and kin."),
        ],
        evidence=[
            ("Wide Old World distribution of erectus-grade humans", "Established"),
            ("Exact species splitting within the grade", "Active debate"),
            ("Language capacity", "Unknown / Speculative"),
        ],
        myths=[
            ("Only sapiens traveled far early", "Erectus was earlier cosmopolitan"),
            ("Erectus was a brief stepping-stone", "Long-lasting radiation"),
        ],
        debates=[
            "Asian vs African trajectories",
            "How many named species within the grade",
        ],
        visuals=[
            "Old World site map",
            "Duration bar graphic",
            "Lumper/splitter taxonomy slider",
        ],
        terms=["Homo erectus", "Acheulean", "Cosmopolitan species"],
        dont=[
            "Do not frame erectus as a failed draft of us.",
            "Do not pretend taxonomy is settled.",
        ],
        s_pointer="S1E24; leads to S3E05.",
    ),
    make(
        n=5,
        slug="neanderthals-denisovans-and-other-humans",
        title="Neanderthals, Denisovans, and Other Humans",
        logline="Other humans were people with histories—archaeology, genomes, admixture, and contingent extinction.",
        from_ep="S3E04 Homo erectus and the First Cosmopolitan Humans",
        to_ep="S3E06 Homo sapiens in Africa",
        deepens="S1 Ep. 24",
        goals=[
            "Present Neanderthal lifeways without caricature.",
            "Show Denisovans mainly through DNA and sparse fossils.",
            "Briefly acknowledge other archaic humans.",
            "Treat admixture as Established where evidenced.",
            "Frame extinction as loss and contingency, not destiny.",
        ],
        acts=[
            ("Cold open", "Many faces on a shared landscape"),
            ("Act I", "Neanderthals"),
            ("Act II", "Denisovans and others"),
            ("Act III", "Mixing and vanishing"),
            ("Act IV", "Baton → sapiens in Africa"),
        ],
        beats=[
            ("Cold open", "Multiple human kinds share Ice Age Eurasia."),
            ("Act I", "Sites, culture, care, hunting—anti-brute framing."),
            ("Act II", "Denisova DNA shadow; brief note on floresiensis and kin."),
            ("Act III", "Admixture into sapiens; extinction causes debated."),
            ("Act IV", "Next: African origins of modern humans in depth."),
        ],
        evidence=[
            ("Neanderthal and Denisovan admixture into some sapiens populations", "Established"),
            ("Neanderthal behavioral complexity", "Established / Strong inference"),
            ("A single extinction cause", "Active debate"),
        ],
        myths=[
            ("Neanderthals were dumb brutes", "Complex behavior evidenced"),
            ("Other humans were props for our rise", "People with their own histories"),
        ],
        debates=[
            "Extinction causes and timing",
            "Full geographic ranges of Denisovans",
        ],
        visuals=[
            "Overlapping range maps",
            "DNA admixture ribbons",
            "Respectful facial reconstructions (labeled speculative)",
        ],
        terms=["Neanderthal", "Denisovan", "Admixture", "Archaic human"],
        dont=[
            "Do not use triumph-of-sapiens parade framing.",
            "Do not caricature Neanderthals.",
        ],
        s_pointer="S1E24; leads to S3E06.",
    ),
    make(
        n=6,
        slug="homo-sapiens-in-africa",
        title="Homo sapiens in Africa",
        logline="Modern humans arise within Africa’s deep population structure—not a single tiny birthplace myth.",
        from_ep="S3E05 Neanderthals, Denisovans, and Other Humans",
        to_ep="S3E07 Out of Africa in Depth",
        deepens="S1 Ep. 24–25",
        goals=[
            "Present fossil and genetic evidence for African origins.",
            "Emphasize structured, multi-region African populations.",
            "Note early cultural signals without overclaiming.",
            "Hand off to dispersal pulses in depth.",
        ],
        acts=[
            ("Cold open", "Africa as a network of sites"),
            ("Act I", "Fossils"),
            ("Act II", "Population structure"),
            ("Act III", "Early cultural signals"),
            ("Act IV", "Baton → leaving Africa"),
        ],
        beats=[
            ("Cold open", "Lights across African sites—no single glowing village of origin."),
            ("Act I", "Early sapiens fossils with soft chronological edges."),
            ("Act II", "Genetics: deep structure and pan-African models."),
            ("Act III", "Hints of symbolism and complex behavior."),
            ("Act IV", "Next: out-of-Africa routes and pulses."),
        ],
        evidence=[
            ("Homo sapiens originated in Africa (broad sense)", "Established"),
            ("A single pinpoint birthplace village", "Oversimplification / Speculative"),
            ("Exact pan-African demographic models", "Active debate"),
        ],
        myths=[
            ("Non-Africans have a separate species origin", "False"),
            ("One African Eden village", "Structured populations across regions"),
        ],
        debates=[
            "Pan-African vs more localized origin models",
            "Timing of cognitive/cultural markers",
        ],
        visuals=[
            "African site network map",
            "Genetic structure schematic",
            "Fossil timeline with uncertainty bars",
        ],
        terms=["Homo sapiens", "Population structure", "Pan-African model"],
        dont=[
            "Do not erase African diversity after the exit story begins.",
            "Do not invent a single Eden pinpoint as fact.",
        ],
        s_pointer="S1E24–25; deeper here before S3E07.",
    ),
    make(
        n=7,
        slug="out-of-africa-in-depth",
        title="Out of Africa in Depth",
        logline="Routes, pulses, encounters—peopling the planet with fossils, archaeology, and genetics braided.",
        from_ep="S3E06 Homo sapiens in Africa",
        to_ep="S3E08 Brains, Childhood, and Social Life",
        deepens="S1 Ep. 25",
        goals=[
            "Present multi-pulse dispersal rather than one cartoon wave.",
            "Cover Eurasia, Sahul, and Americas with dating debates flagged.",
            "Integrate archaic encounters and admixture.",
            "Show how evidence streams braid and sometimes conflict.",
            "Hand off to the mind/culture arc.",
        ],
        acts=[
            ("Cold open", "Multiple wave arrows"),
            ("Act I", "Exits and corridors"),
            ("Act II", "Encounters"),
            ("Act III", "Far horizons"),
            ("Act IV", "Baton → minds that carried culture"),
        ],
        beats=[
            ("Cold open", "Several arrows leave Africa—not one heroic couple."),
            ("Act I", "Climate windows, corridors, and failed pulses."),
            ("Act II", "Meetings with Neanderthals and Denisovans."),
            ("Act III", "Sahul; Americas first-arrival debates."),
            ("Act IV", "Next: brains, childhood, and social life."),
        ],
        evidence=[
            ("Out-of-Africa peopling of the world", "Established"),
            ("Exact pulse timings and route weights", "Active debate"),
            ("Earliest peopling of the Americas", "Active debate"),
        ],
        myths=[
            ("One couple left Africa once", "Populations and multiple pulses"),
            ("First-arrival dates are frozen dogma", "Active research frontier"),
        ],
        debates=[
            "Relative importance of coastal vs inland routes",
            "Local admixture contributions",
        ],
        visuals=[
            "Multi-pulse migration animation",
            "Artifact and genome trail overlays",
            "Americas dating debate graphic",
        ],
        terms=["Dispersal pulse", "Beringia", "Sahul", "Founder effect (light)"],
        dont=[
            "Do not freeze a single first-arrival date as absolute.",
            "Do not ignore failed or minor pulses.",
        ],
        s_pointer="Deeper than S1E25; leads to mind arc S3E08–11.",
    ),
    make(
        n=8,
        slug="brains-childhood-and-social-life",
        title="Brains, Childhood, and Social Life",
        logline="Expensive brains and long childhoods reshape life history—foundations of cumulative culture.",
        from_ep="S3E07 Out of Africa in Depth",
        to_ep="S3E09 Language",
        deepens="S1 Ep. 26",
        goals=[
            "Explain encephalization costs in energy terms.",
            "Link long childhoods to cooperative care and teaching.",
            "Sketch social-cognition bases without overclaiming.",
            "Hand off to language as the cooperation transformer.",
        ],
        acts=[
            ("Cold open", "Brain energy pie chart"),
            ("Act I", "Costly brains"),
            ("Act II", "Long childhoods"),
            ("Act III", "Social life"),
            ("Act IV", "Baton → language"),
        ],
        beats=[
            ("Cold open", "A large brain’s energy budget on screen."),
            ("Act I", "Size trends with caveats—size is not everything."),
            ("Act II", "Extended learning windows and alloparents."),
            ("Act III", "Social cognition bases for teaching and norms."),
            ("Act IV", "Next: language transforms cooperation."),
        ],
        evidence=[
            ("Human brains are large and metabolically costly", "Established"),
            ("Settled driver sequence for encephalization", "Active debate"),
            ("Cooperative care enabling long childhoods", "Strong inference"),
        ],
        myths=[
            ("Brain size alone creates culture", "Insufficient without social learning"),
            ("Childhood is just helplessness", "It is also a learning adaptation"),
        ],
        debates=[
            "Social vs ecological drivers of brain expansion",
            "How early cooperative breeding intensified",
        ],
        visuals=[
            "Energy-budget charts",
            "Multi-age caregiving groups",
            "Brain-size trend with uncertainty",
        ],
        terms=["Encephalization", "Alloparent", "Life history", "Social cognition"],
        dont=[
            "Do not deliver sex-myth lectures without evidence.",
            "Do not equate brain size with worth or destiny.",
        ],
        s_pointer="S1E26; continues to S3E09.",
    ),
    make(
        n=9,
        slug="language",
        title="Language",
        logline="Language transforms cooperation and cumulative culture—origins hard to date; fossils stay mostly silent.",
        from_ep="S3E08 Brains, Childhood, and Social Life",
        to_ep="S3E10 Art, Ritual, and Symbolism",
        deepens="S1 Ep. 26",
        goals=[
            "Define distinctive features of language accessibly.",
            "Hold biology and culture together without false precision.",
            "State dating limits honestly.",
            "Show consequences for teaching and cooperation.",
            "Hand off to external symbols and ritual.",
        ],
        acts=[
            ("Cold open", "Silent fossils, loud culture"),
            ("Act I", "What language is"),
            ("Act II", "The origins problem"),
            ("Act III", "Consequences"),
            ("Act IV", "Baton → art and ritual"),
        ],
        beats=[
            ("Cold open", "Bones do not speak; cultural trails sometimes do."),
            ("Act I", "Displacement, productivity, teaching—language as a system."),
            ("Act II", "When it emerged remains Unknown; Neanderthal capacity open."),
            ("Act III", "Language fuels the cultural ratchet."),
            ("Act IV", "Next: marks, images, burials, ornaments."),
        ],
        evidence=[
            ("Language transforms human cooperation", "Strong inference / Established broad"),
            ("Exact emergence date of language", "Unknown"),
            ("Full Neanderthal language capacity", "Active debate / Unknown"),
        ],
        myths=[
            ("Language fossilizes directly", "It does not"),
            ("We can date first words precisely", "False precision"),
        ],
        debates=[
            "Timing of full linguistic modernity",
            "Continuity with Neanderthal communication",
        ],
        visuals=[
            "Signal → grammar cascade animation",
            "Fossil silence vs artifact noise split screen",
            "Teaching circle with spoken instruction",
        ],
        terms=["Language", "Displacement", "Recursion (light)", "Cultural ratchet"],
        dont=[
            "Do not invent fake dating precision.",
            "Do not claim a single gene equals language.",
        ],
        s_pointer="S1E26; S4 returns to mind/consciousness frontiers.",
    ),
    make(
        n=10,
        slug="art-ritual-and-symbolism",
        title="Art, Ritual, and Symbolism",
        logline="Marks, images, burials, ornaments—minds trafficking in meaning; resist a single creative-explosion slogan.",
        from_ep="S3E09 Language",
        to_ep="S3E11 Cumulative Culture and Teaching",
        deepens="S1 Ep. 26",
        goals=[
            "Survey art, ornament, and burial evidence globally.",
            "Expose dating controversies and regional chronologies.",
            "Admit meaning is often unknowable.",
            "Allow multiple origins of symbolic behavior.",
            "Hand off to cumulative culture mechanics.",
        ],
        acts=[
            ("Cold open", "Torchlit cave wall"),
            ("Act I", "Evidence types"),
            ("Act II", "Dating fights"),
            ("Act III", "Meaning limits"),
            ("Act IV", "Baton → teaching and ratchet"),
        ],
        beats=[
            ("Cold open", "Images wake under torchlight—then the evidence checklist begins."),
            ("Act I", "Beads, ochre, parietal art, burial practices."),
            ("Act II", "Regional chronologies are complex; explosion slogans overreach."),
            ("Act III", "Interpretation humility: we see marks, not minds."),
            ("Act IV", "Next: how teaching stacks innovations across generations."),
        ],
        evidence=[
            ("Symbolic artifacts evidence complex minds", "Strong inference"),
            ("A single global creative explosion", "Often overstated / Active debate"),
            ("Exact meanings of prehistoric images", "Unknown / Speculative"),
        ],
        myths=[
            ("One cave marks the birth of the modern mind", "Complex, multi-regional chronology"),
            ("We know what the paintings meant", "Usually we do not"),
        ],
        debates=[
            "Earliest unambiguous symbolism",
            "Continuity of ritual across regions",
        ],
        visuals=[
            "Cave reveal with dating uncertainty bars",
            "Global ornament and art map",
            "Meaning-speculation dial set to low",
        ],
        terms=["Symbolism", "Parietal art", "Burial", "Ochre"],
        dont=[
            "Do not invent ritual meanings as fact.",
            "Do not sell a single creative-explosion date as settled.",
        ],
        s_pointer="S1E26; leads to S3E11.",
    ),
    make(
        n=11,
        slug="cumulative-culture-and-teaching",
        title="Cumulative Culture and Teaching",
        logline="Humans stack innovations across generations—a second inheritance system powered by teaching and norms.",
        from_ep="S3E10 Art, Ritual, and Symbolism",
        to_ep="S3E12 Ice Age Humans and Megafauna",
        deepens="S1 Ep. 26",
        goals=[
            "Define cumulative culture and the ratchet effect.",
            "Show imitation, teaching, and norms as mechanisms.",
            "Compare carefully with animal cultures.",
            "Explain why cultural acceleration can later explode.",
            "Hand off to Ice Age forensic detail.",
        ],
        acts=[
            ("Cold open", "Ratchet mechanism"),
            ("Act I", "High-fidelity social learning"),
            ("Act II", "The ratchet"),
            ("Act III", "Animal comparisons"),
            ("Act IV", "Baton → Ice Age worlds"),
        ],
        beats=[
            ("Cold open", "A ratchet clicks: improvements stick across generations."),
            ("Act I", "Imitation and teaching raise fidelity of transmission."),
            ("Act II", "Stacks of tools, recipes, and norms accumulate."),
            ("Act III", "Other animals have culture; humans amplify degree and kind."),
            ("Act IV", "Next: these minds face ice, megafauna, and hard climates."),
        ],
        evidence=[
            ("Cumulative culture is central to human success", "Strong inference / Established broad"),
            ("Exact minimum cognitive kit for ratchet", "Active debate"),
            ("Why acceleration intensifies when it does", "Active debate"),
        ],
        myths=[
            ("Animals have zero culture", "Continuity exists; degree differs"),
            ("Culture is just technology gadgets", "Includes norms and knowledge"),
        ],
        debates=[
            "Minimum requirements for cumulative culture",
            "When cultural evolution begins to accelerate sharply",
        ],
        visuals=[
            "Ratchet graphic",
            "Stacking tool generations",
            "Human vs animal culture comparison cards",
        ],
        terms=["Cumulative culture", "Ratchet effect", "Norm", "Social learning"],
        dont=[
            "Do not sneer at animal cognition.",
            "Do not claim culture replaces biology.",
        ],
        s_pointer="S1E26; bridge toward farming later.",
    ),
    make(
        n=12,
        slug="ice-age-humans-and-megafauna",
        title="Ice Age Humans and Megafauna",
        logline="Glacial cycles, megafauna, and human adaptation in forensic detail—extinctions without a forced universal verdict.",
        from_ep="S3E11 Cumulative Culture and Teaching",
        to_ep="S3E13 Hunter-Gatherer Worlds",
        deepens="S1 Ep. 27",
        goals=[
            "Apply glacial cycles to human landscapes concretely.",
            "Present megafauna extinction debates region by region.",
            "Show cold-world lifeways for sapiens and Neanderthals.",
            "Use LGM end as threshold into Holocene foragers.",
            "Hand off to diverse hunter-gatherer worlds.",
        ],
        acts=[
            ("Cold open", "Ice sheet vs kill site tension"),
            ("Act I", "Climate machinery"),
            ("Act II", "People in the cold"),
            ("Act III", "Giants vanish"),
            ("Act IV", "Baton → Holocene foragers"),
        ],
        beats=[
            ("Cold open", "Ice advances; spears and climate both enter the courtroom."),
            ("Act I", "Bridges, refugia, and resource pulses."),
            ("Act II", "Technology and society under glacial pressure."),
            ("Act III", "Human vs climate vs both—regional recipes."),
            ("Act IV", "Next: Holocene hunter-gatherer diversity."),
        ],
        evidence=[
            ("End-Pleistocene megafauna losses are a real pattern", "Established"),
            ("A universal single extinction cause", "Active debate"),
            ("Regional human contribution varies", "Active debate / Incomplete"),
        ],
        myths=[
            ("Only humans OR only climate, always", "Often combined and regional"),
            ("Ice Age humans were uniformly struggling survivors", "Diverse skilled adaptations"),
        ],
        debates=[
            "Regional extinction cause mixtures",
            "Timing of human arrival vs extinction pulses",
        ],
        visuals=[
            "Ice-sheet advance maps",
            "Megafauna fade timelines",
            "Courtroom cards: climate / humans / synergy",
        ],
        terms=["LGM", "Megafauna", "Refugium", "Pleistocene"],
        dont=[
            "Do not force a universal extinction verdict.",
            "Do not erase Neanderthal cold adaptations.",
        ],
        s_pointer="S1E27 depth; leads to S3E13.",
    ),
    make(
        n=13,
        slug="hunter-gatherer-worlds",
        title="Hunter-Gatherer Worlds",
        logline="Most of human history is foraging—diverse, skilled, ecological expertise, not a single stereotype.",
        from_ep="S3E12 Ice Age Humans and Megafauna",
        to_ep="S3E14 Domestication and the Neolithic Transition",
        deepens="S1 Ep. 28",
        goals=[
            "Destroy the single caveman stereotype.",
            "Show ethnographic and archaeological diversity carefully.",
            "Highlight knowledge intensity of foraging lifeways.",
            "Set up why farming is a trade-off, not pure progress.",
            "Hand off to domestication.",
        ],
        acts=[
            ("Cold open", "Stereotype shatter montage"),
            ("Act I", "Diversity of foragers"),
            ("Act II", "Skill and knowledge"),
            ("Act III", "Trade-offs before farming"),
            ("Act IV", "Baton → domestication"),
        ],
        beats=[
            ("Cold open", "Many forager worlds replace the cartoon caveman."),
            ("Act I", "Coasts, deserts, forests, Arctic—different solutions."),
            ("Act II", "Tracking, plants, seasons, social rules."),
            ("Act III", "Mobility, health, and equality myths vs evidence."),
            ("Act IV", "Next: plants and animals remake humans."),
        ],
        evidence=[
            ("Foraging dominated most of human history", "Established"),
            ("Forager lifeways were diverse", "Established"),
            ("Simple equality/health generalizations", "Often overstated / Active debate"),
        ],
        myths=[
            ("All hunter-gatherers lived the same short brutal life", "Diversity and skill"),
            ("Farming is pure progress from misery", "Trade-offs appear later"),
        ],
        debates=[
            "How far ethnography can illuminate deep prehistory",
            "Inequality among foragers",
        ],
        visuals=[
            "Global forager diversity mosaic",
            "Seasonal round calendar",
            "Stereotype vs evidence checklist",
        ],
        terms=["Forager", "Hunter-gatherer", "Mobility", "Ethnographic analogy"],
        dont=[
            "Do not romanticize or demean foragers.",
            "Do not treat one ethnography as universal prehistory.",
        ],
        s_pointer="S1E28; leads to S3E14.",
    ),
    make(
        n=14,
        slug="domestication-and-the-neolithic-transition",
        title="Domestication and the Neolithic Transition",
        logline="Plants, animals, and humans remake each other—region by region, with costs and benefits.",
        from_ep="S3E13 Hunter-Gatherer Worlds",
        to_ep="S3E15 Prehistoric Complexity Before Cities",
        deepens="S1 Ep. 28",
        goals=[
            "Explain domestication as coevolution.",
            "Compare multiple independent farming origins.",
            "Show diet, disease, labor, and inequality trade-offs.",
            "Avoid teleology toward civilization.",
            "Hand off to pre-urban complexity.",
        ],
        acts=[
            ("Cold open", "Wild plant becomes crop"),
            ("Act I", "What domestication is"),
            ("Act II", "Multiple hearths"),
            ("Act III", "Costs and benefits"),
            ("Act IV", "Baton → complexity before cities"),
        ],
        beats=[
            ("Cold open", "Seed morphology shifts under human selection."),
            ("Act I", "Mutual remaking of species and societies."),
            ("Act II", "Southwest Asia, China, Americas, Africa, New Guinea—and more."),
            ("Act III", "Calories vs disease, labor, hierarchy risks."),
            ("Act IV", "Next: megaliths and networks before urban cradles."),
        ],
        evidence=[
            ("Multiple independent domestication centers", "Established"),
            ("Farming involves health and labor trade-offs", "Established / Strong inference"),
            ("Exact pathways in every region", "Incomplete / Active debate"),
        ],
        myths=[
            ("Farming invented once and spread everywhere", "Multiple origins"),
            ("Neolithic = instant cities", "Long, uneven transitions"),
        ],
        debates=[
            "Push vs pull models for adoption",
            "Roles of climate, population, and ideology",
        ],
        visuals=[
            "Domestication centers map",
            "Wild-to-crop morphology morph",
            "Trade-off scorecard",
        ],
        terms=["Domestication", "Neolithic", "Secondary products", "Sedentism"],
        dont=[
            "Do not treat farming as inevitable progress.",
            "Do not collapse all regions into Fertile Crescent only.",
        ],
        s_pointer="S1E28; leads to S3E15.",
    ),
    make(
        n=15,
        slug="prehistoric-complexity-before-cities",
        title="Prehistoric Complexity Before Cities",
        logline="Megaliths, exchange networks, and non-urban complexity—slowing the path so cradles do not feel sudden.",
        from_ep="S3E14 Domestication and the Neolithic Transition",
        to_ep="S3E16 Cradles of Civilization Compared",
        deepens="S1 Ep. 28–29",
        goals=[
            "Show complex societies without cities.",
            "Use monuments and networks as evidence of organization.",
            "Separate complexity from urbanism and states.",
            "Bridge into comparative cradles.",
        ],
        acts=[
            ("Cold open", "Monument without a skyline"),
            ("Act I", "What complexity means"),
            ("Act II", "Case studies"),
            ("Act III", "Networks before capitals"),
            ("Act IV", "Baton → cradles compared"),
        ],
        beats=[
            ("Cold open", "A megalithic horizon with no skyscrapers."),
            ("Act I", "Ritual, labor coordination, inequality—without cities."),
            ("Act II", "Select regional cases (keep comparative, not exhaustive)."),
            ("Act III", "Goods and ideas travel before empires."),
            ("Act IV", "Next: six-to-seven cradles side by side."),
        ],
        evidence=[
            ("Non-urban societies can be highly complex", "Established"),
            ("Monument building requires organized labor", "Strong inference"),
            ("Political forms behind every monument", "Often Incomplete"),
        ],
        myths=[
            ("Complexity requires cities", "False"),
            ("Prehistory is only villages waiting for civilization", "Rich non-urban worlds"),
        ],
        debates=[
            "How to define social complexity",
            "Roles of ritual vs economy in monument projects",
        ],
        visuals=[
            "Megalith construction labor animation",
            "Exchange-network map",
            "Urban vs complex Venn",
        ],
        terms=["Megalith", "Complexity", "Exchange network", "Monumentality"],
        dont=[
            "Do not treat monuments as proto-cities by default.",
            "Do not invent priest-kings without evidence.",
        ],
        s_pointer="S1E28–29 bridge; leads to S3E16.",
    ),
    make(
        n=16,
        slug="cradles-of-civilization-compared",
        title="Cradles of Civilization Compared",
        logline="Six-to-seven cradles in comparative depth—shared problems, different solutions, no single template.",
        from_ep="S3E15 Prehistoric Complexity Before Cities",
        to_ep="S3E17 Writing, Numbers, Law, and States",
        deepens="S1 Ep. 29",
        goals=[
            "Compare cradles: Mesopotamia, Egypt, Indus, China, Mesoamerica, Andean, and related cases.",
            "Find shared pressures without forcing identical pathways.",
            "Highlight writing/urbanism differences honestly.",
            "Hand off to writing, numbers, law, and states.",
        ],
        acts=[
            ("Cold open", "Seven lamps light"),
            ("Act I", "Shared problems"),
            ("Act II", "Different solutions"),
            ("Act III", "Comparison matrix"),
            ("Act IV", "Baton → external memory and states"),
        ],
        beats=[
            ("Cold open", "Multiple cradles illuminate—not one origin of civilization."),
            ("Act I", "Surplus, water, conflict, ritual, trade as recurring pressures."),
            ("Act II", "Cities, states, and scripts appear unevenly."),
            ("Act III", "Side-by-side matrix of features."),
            ("Act IV", "Next: writing, numbers, law—external memory."),
        ],
        evidence=[
            ("Multiple independent urban/civilizational traditions", "Established"),
            ("Identical pathway in every cradle", "False / Oversimplification"),
            ("Indus political form details", "Incomplete / Active debate"),
        ],
        myths=[
            ("Civilization started only in one place", "Multiple cradles"),
            ("All early states look like Mesopotamia", "Divergent institutions"),
        ],
        debates=[
            "How to define civilization without bias",
            "Roles of environment vs culture in each case",
        ],
        visuals=[
            "Comparative cradle map",
            "Feature matrix animation",
            "River and highland twin geographies",
        ],
        terms=["Cradle", "Urbanism", "State", "Civilization (contested term)"],
        dont=[
            "Do not rank cradles as more/less advanced.",
            "Do not erase Indigenous American independent developments.",
        ],
        s_pointer="S1E29 depth; leads to S3E17.",
    ),
    make(
        n=17,
        slug="writing-numbers-law-and-states",
        title="Writing, Numbers, Law, and States",
        logline="External memory and administration make empires and long knowledge possible—power and literacy intertwined.",
        from_ep="S3E16 Cradles of Civilization Compared",
        to_ep="S3E18 The Axial Age in Depth",
        deepens="S1 Ep. 29",
        goals=[
            "Explain writing and numerals as external memory.",
            "Show law codes and administration as state tools.",
            "Link bureaucracy to scale and inequality.",
            "Bridge toward Axial ethical/philosophical transformations.",
        ],
        acts=[
            ("Cold open", "Clay tablet as hard drive"),
            ("Act I", "Writing and numbers"),
            ("Act II", "Law and administration"),
            ("Act III", "Scale and power"),
            ("Act IV", "Baton → Axial Age"),
        ],
        beats=[
            ("Cold open", "A tablet outlives a memory—knowledge becomes portable."),
            ("Act I", "Scripts and accounting across cradles (unevenly)."),
            ("Act II", "Law lists, taxes, archives."),
            ("Act III", "States scale trust and coercion together."),
            ("Act IV", "Next: Axial Age critiques and new moral languages."),
        ],
        evidence=[
            ("Writing enables large-scale administration", "Established"),
            ("Multiple independent inventions of writing", "Established"),
            ("Literacy rates in early states", "Often low / Incomplete"),
        ],
        myths=[
            ("Writing equals wisdom for everyone", "Often elite tool first"),
            ("Law codes equal justice", "Also instruments of power"),
        ],
        debates=[
            "Primary drivers of script invention",
            "How much oral culture persisted beside writing",
        ],
        visuals=[
            "Tablet-as-hard-drive metaphor",
            "Archive room reconstruction",
            "Tax-and-law flowchart",
        ],
        terms=["Writing", "External memory", "Bureaucracy", "Law code"],
        dont=[
            "Do not equate literacy with moral superiority.",
            "Do not ignore oral knowledge systems.",
        ],
        s_pointer="S1E29; leads to S3E18.",
    ),
    make(
        n=18,
        slug="the-axial-age-in-depth",
        title="The Axial Age in Depth",
        logline="First-millennium-BCE transformations across Greek, Indian, Chinese, and Hebrew worlds—parallel, not identical.",
        from_ep="S3E17 Writing, Numbers, Law, and States",
        to_ep="S3E19 Faiths as Social Architecture",
        deepens="S1 Ep. 30",
        goals=[
            "Survey Axial transformations comparatively.",
            "Keep chronology: Axial before later universal faith expansions.",
            "Avoid single-cause global theory as fact.",
            "Hand off to religions as scalable social architecture.",
        ],
        acts=[
            ("Cold open", "Four lamps of critique"),
            ("Act I", "What Axial Age means"),
            ("Act II", "Regional paths"),
            ("Act III", "Limits of the label"),
            ("Act IV", "Baton → faiths as architecture"),
        ],
        beats=[
            ("Cold open", "Philosophy, prophecy, and ethics rise in several zones."),
            ("Act I", "Second-order thinking about cosmos, self, and justice."),
            ("Act II", "Greek, Indian, Chinese, Hebrew trajectories—distinct."),
            ("Act III", "Label useful, not a mystical global switch."),
            ("Act IV", "Next: how major faiths scale trust beyond tribes."),
        ],
        evidence=[
            ("Major intellectual/religious transformations in the first millennium BCE", "Established broad"),
            ("A single synchronized Axial cause", "Active debate / Speculative"),
            ("Uniform Axial package everywhere", "Oversimplification"),
        ],
        myths=[
            ("Axial Age was one worldwide event", "Regional, staggered, diverse"),
            ("Philosophy replaces religion then", "They intertwine differently by region"),
        ],
        debates=[
            "Usefulness of the Axial Age concept",
            "Roles of empire, trade, and literacy",
        ],
        visuals=[
            "Comparative timeline of thinkers/traditions",
            "Map of Axial zones",
            "Concept dial: useful label vs overclaim",
        ],
        terms=["Axial Age", "Second-order thinking", "Prophecy", "Philosophy"],
        dont=[
            "Do not put Christianity/Islam chronologically before Axial.",
            "Do not force identical doctrines across regions.",
        ],
        s_pointer="S1E30 depth; leads to S3E19.",
    ),
    make(
        n=19,
        slug="faiths-as-social-architecture",
        title="Faiths as Social Architecture",
        logline="How major religions scaled trust, law, identity, and charity beyond the tribe—bonds, not only beliefs.",
        from_ep="S3E18 The Axial Age in Depth",
        to_ep="S3E20 Worlds of Faith and Exchange",
        deepens="S1 Ep. 31",
        goals=[
            "Treat religions as social technologies of belonging.",
            "Show law, ritual, charity, and identity at scale.",
            "Stay descriptive and comparative, not apologetic or hostile.",
            "Hand off to exchange worlds carrying faiths and goods.",
        ],
        acts=[
            ("Cold open", "Strangers share a sacred calendar"),
            ("Act I", "Beyond the tribe"),
            ("Act II", "Institutions"),
            ("Act III", "Costs and conflicts"),
            ("Act IV", "Baton → faiths on the move"),
        ],
        beats=[
            ("Cold open", "Ritual and rule let distant strangers cooperate."),
            ("Act I", "Universalizing and communal bonds."),
            ("Act II", "Law, education, pilgrimage, endowment."),
            ("Act III", "Exclusion and conflict as real parts of the architecture."),
            ("Act IV", "Next: Silk Roads and oceans move beliefs and goods."),
        ],
        evidence=[
            ("Religions can scale cooperation beyond kin", "Strong inference / Established broad"),
            ("A single sociological formula for all faiths", "Oversimplification"),
            ("Net historical good/bad ledger", "Not a scientific claim"),
        ],
        myths=[
            ("Religion is only private belief", "Also law, identity, institution"),
            ("Science episode means anti-religion episode", "Series stays descriptive"),
        ],
        debates=[
            "How much religion vs state drives large-scale trust",
            "Measuring cohesion effects empirically",
        ],
        visuals=[
            "Tribe → umma/church/sangha scale graphic",
            "Institution map: school, court, pilgrimage",
            "Bond and boundary twin doors",
        ],
        terms=["Social architecture", "Sacred law", "Pilgrimage", "Identity"],
        dont=[
            "Do not evangelize or attack.",
            "Do not collapse all religions into one template.",
        ],
        s_pointer="S1E31; leads to S3E20.",
    ),
    make(
        n=20,
        slug="worlds-of-faith-and-exchange",
        title="Worlds of Faith and Exchange",
        logline="Silk Roads, oceans, and empires—beliefs, goods, and techniques in motion across Afro-Eurasia and beyond.",
        from_ep="S3E19 Faiths as Social Architecture",
        to_ep="S3E21 How Humans Keep Time (Deep Dive)",
        deepens="S1 Ep. 31",
        goals=[
            "Map major exchange corridors.",
            "Show faiths and technologies traveling together.",
            "Include maritime as well as overland routes.",
            "Hand off to calendars and the global hour map.",
        ],
        acts=[
            ("Cold open", "Caravan and dhow split screen"),
            ("Act I", "Corridors"),
            ("Act II", "Beliefs in motion"),
            ("Act III", "Empires and brokers"),
            ("Act IV", "Baton → keeping time"),
        ],
        beats=[
            ("Cold open", "Silk, spice, scripture, and steel share routes."),
            ("Act I", "Silk Roads, Indian Ocean, Sahara, later Atlantic notes."),
            ("Act II", "Buddhism, Islam, Christianity, and others along trade."),
            ("Act III", "Empires protect and tax; diasporas transmit."),
            ("Act IV", "Next: how humans keep sacred and civil time."),
        ],
        evidence=[
            ("Long-distance Afro-Eurasian exchange networks", "Established"),
            ("Religions spread along trade and conquest", "Established"),
            ("Exact volume of every corridor", "Incomplete"),
        ],
        myths=[
            ("Premodern world was static and isolated", "Extensive exchange"),
            ("Only Europe moved history", "Multi-polar exchange"),
        ],
        debates=[
            "Relative weight of trade vs conquest in religious spread",
            "How to narrate Americas contact without teleology yet",
        ],
        visuals=[
            "Animated corridor map",
            "Faith-and-goods layered routes",
            "Port city montage",
        ],
        terms=["Silk Roads", "Indian Ocean world", "Diaspora", "Exchange"],
        dont=[
            "Do not center only Europe.",
            "Do not treat exchange as pure peace—violence travels too.",
        ],
        s_pointer="S1E31; leads to S3E21.",
    ),
    make(
        n=21,
        slug="how-humans-keep-time-deep-dive",
        title="How Humans Keep Time (Deep Dive)",
        logline="Sacred calendars, civil calendars, and the global hour map—in detail, including UTC offsets east and west.",
        from_ep="S3E20 Worlds of Faith and Exchange",
        to_ep="S3E22 Medieval to Early Modern Knowledge",
        deepens="S1 Ep. 32",
        goals=[
            "Explain lunar, solar, and lunisolar calendars.",
            "Show sacred vs civil timekeeping.",
            "Teach time zones and UTC offsets (+east / −west).",
            "Connect clocks to navigation and coordination.",
            "Hand off to medieval–early modern knowledge relay.",
        ],
        acts=[
            ("Cold open", "One Earth, many midnights"),
            ("Act I", "Calendars"),
            ("Act II", "Sacred time"),
            ("Act III", "Hours and zones"),
            ("Act IV", "Baton → knowledge relay"),
        ],
        beats=[
            ("Cold open", "Simultaneous different dates/hours across the globe."),
            ("Act I", "Solar years, lunar months, intercalation problems."),
            ("Act II", "Ritual time binding communities."),
            ("Act III", "Mechanical clocks → standard time → UTC offsets."),
            ("Act IV", "Next: natural philosophy toward scientific revolution."),
        ],
        evidence=[
            ("Earth’s rotation and orbit underpin civil time", "Established"),
            ("Time zones are conventions for coordination", "Established"),
            ("UTC offset sign: east positive, west negative", "Established convention"),
        ],
        myths=[
            ("Calendars are natural facts not conventions", "Astronomy + social choice"),
            ("Time zones measure distance only", "Political and historical too"),
        ],
        debates=[
            "Historical adoption battles for standard time",
            "Calendar reform politics",
        ],
        visuals=[
            "Globe with hour wedges",
            "UTC offset dial (+east / −west)",
            "Sacred calendar overlays",
        ],
        terms=["UTC", "Time zone", "Lunisolar", "Intercalation", "Meridian"],
        dont=[
            "Do not get the UTC sign convention wrong.",
            "Do not mock sacred calendars.",
        ],
        s_pointer="S1E32 depth; leads to S3E22.",
    ),
    make(
        n=22,
        slug="medieval-to-early-modern-knowledge",
        title="Medieval to Early Modern Knowledge",
        logline="The relay from medieval natural philosophy to the brink of the scientific revolution—many civilizations, not one tunnel.",
        from_ep="S3E21 How Humans Keep Time (Deep Dive)",
        to_ep="S3E23 The Scientific Revolution",
        deepens="S1 Ep. 31–33",
        goals=[
            "Show knowledge transmission across languages and empires.",
            "Credit Islamic, Indian, Chinese, and European contributions.",
            "Describe universities, observatories, and craft knowledge.",
            "Arrive at the brink without claiming sudden European magic.",
            "Hand off to the scientific revolution proper.",
        ],
        acts=[
            ("Cold open", "Manuscript relay race"),
            ("Act I", "Medieval natural philosophy"),
            ("Act II", "Cross-civilization exchange"),
            ("Act III", "Institutions and instruments"),
            ("Act IV", "Baton → scientific revolution"),
        ],
        beats=[
            ("Cold open", "A text travels Baghdad → Cordoba → Latin Europe—and other routes."),
            ("Act I", "Aristotelian and other frameworks as working worlds."),
            ("Act II", "Algebra, optics, medicine, astronomy exchanges."),
            ("Act III", "Schools, courts, workshops, observatories."),
            ("Act IV", "Next: Copernicus to Newton as method shift."),
        ],
        evidence=[
            ("Extensive premodern scientific activity across Afro-Eurasia", "Established"),
            ("Translation and commentary traditions matter", "Established"),
            ("A single cause of later European takeoff", "Active debate"),
        ],
        myths=[
            ("Medieval world was a dark age of zero science", "False caricature"),
            ("Science appears only in Europe suddenly", "Long multi-civilization relay"),
        ],
        debates=[
            "Why institutional science accelerates where it does",
            "How to weigh craft vs scholastic knowledge",
        ],
        visuals=[
            "Manuscript relay map",
            "Observatory and workshop montage",
            "Translation chain graphic",
        ],
        terms=["Natural philosophy", "Translation movement", "Scholasticism", "Observatory"],
        dont=[
            "Do not use Dark Ages as a blanket slur.",
            "Do not erase non-European knowledge.",
        ],
        s_pointer="S1E31–33 bridge; leads to S3E23.",
    ),
    make(
        n=23,
        slug="the-scientific-revolution",
        title="The Scientific Revolution",
        logline="Copernicus to Newton—method, instruments, and institutions reshape how nature is questioned.",
        from_ep="S3E22 Medieval to Early Modern Knowledge",
        to_ep="S3E24 Industry, Energy, and the Human Planet",
        deepens="S1 Ep. 33",
        goals=[
            "Narrate key transformations without hero-only history.",
            "Emphasize method, math, instruments, and societies.",
            "Keep continuity with earlier knowledge.",
            "Hand off to industrial energy scaling.",
        ],
        acts=[
            ("Cold open", "Telescope points up; lab bench waits"),
            ("Act I", "New skies"),
            ("Act II", "Method and math"),
            ("Act III", "Institutions"),
            ("Act IV", "Baton → industry"),
        ],
        beats=[
            ("Cold open", "Instrument extends senses; debate follows."),
            ("Act I", "Heliocentrism controversies and evidence climb."),
            ("Act II", "Experiment, mathematics, mechanical philosophy."),
            ("Act III", "Academies, journals, correspondence networks."),
            ("Act IV", "Next: fossil energy multiplies power."),
        ],
        evidence=[
            ("Major early modern transformations in natural knowledge", "Established"),
            ("Newton’s laws as lasting framework (classical domain)", "Established"),
            ("The phrase scientific revolution as one neat event", "Historiographic debate"),
        ],
        myths=[
            ("Science replaces religion overnight", "Complex coexistence and conflict"),
            ("A few lone geniuses invent modernity alone", "Networks and instruments matter"),
        ],
        debates=[
            "How revolutionary vs continuous the period was",
            "Roles of print, patronage, and empire",
        ],
        visuals=[
            "Telescope and pendulum set-pieces",
            "Correspondence network map",
            "Method flowchart: claim → test → revise",
        ],
        terms=["Scientific Revolution", "Heliocentrism", "Experiment", "Academy"],
        dont=[
            "Do not present a clean secular triumph myth.",
            "Do not ignore women and non-elite contributors entirely.",
        ],
        s_pointer="S1E33; leads to S3E24.",
    ),
    make(
        n=24,
        slug="industry-energy-and-the-human-planet",
        title="Industry, Energy, and the Human Planet",
        logline="Fossil energy multiplies human power—and begins planetary-scale change.",
        from_ep="S3E23 The Scientific Revolution",
        to_ep="S3E25 Darwin, Deep Time, and Remaking Life’s Story",
        deepens="S1 Ep. 33",
        goals=[
            "Link coal/steam/oil to productivity and empire.",
            "Show urbanization and labor transformations.",
            "Introduce Anthropocene-adjacent planetary signals carefully.",
            "Hand off to deep time and evolution rewriting humanity’s place.",
        ],
        acts=[
            ("Cold open", "Watt of coal vs muscle"),
            ("Act I", "Energy multipliers"),
            ("Act II", "Factories and cities"),
            ("Act III", "Planetary signals"),
            ("Act IV", "Baton → evolution and deep time"),
        ],
        beats=[
            ("Cold open", "One engine outworks a village of muscles."),
            ("Act I", "Fossil fuels as stored ancient sunlight."),
            ("Act II", "Industry remakes work, class, and cities."),
            ("Act III", "Atmosphere and biosphere begin human-scale change."),
            ("Act IV", "Next: Darwin and geology remake life’s story."),
        ],
        evidence=[
            ("Industrial use of fossil energy transforms economies", "Established"),
            ("Rising CO₂ from fossil fuels", "Established"),
            ("Formal Anthropocene boundary definition", "Active debate"),
        ],
        myths=[
            ("Industry is only machines, not social change", "Labor and cities transform"),
            ("Climate impact begins only recently in the 2000s", "Industrial roots deeper"),
        ],
        debates=[
            "Dating the Anthropocene",
            "How to weigh empire and inequality in industrial takeoff",
        ],
        visuals=[
            "Energy multiplier bars",
            "City growth time-lapse",
            "Keeling-style curve origin story light touch",
        ],
        terms=["Fossil fuel", "Industrial Revolution", "Anthropocene (debated)", "Productivity"],
        dont=[
            "Do not preach; show mechanisms and trade-offs.",
            "Do not pretend planetary impact is speculative only.",
        ],
        s_pointer="S1E33; leads to S3E25; S4 returns to Earth system.",
    ),
    make(
        n=25,
        slug="darwin-deep-time-and-remaking-lifes-story",
        title="Darwin, Deep Time, and Remaking Life’s Story",
        logline="Geology and evolution rewrite humanity’s place in nature—deep time becomes personal.",
        from_ep="S3E24 Industry, Energy, and the Human Planet",
        to_ep="S3E26 Electricity, Computing, and Early Global Nerves",
        deepens="S1 Ep. 33",
        goals=[
            "Connect deep time geology to evolutionary theory.",
            "Explain natural selection accessibly.",
            "Show cultural shock and later synthesis.",
            "Hand off to electricity and information networks.",
        ],
        acts=[
            ("Cold open", "Cliff strata as a clock"),
            ("Act I", "Deep time"),
            ("Act II", "Darwin’s argument"),
            ("Act III", "Reception and synthesis"),
            ("Act IV", "Baton → electric nerves"),
        ],
        beats=[
            ("Cold open", "Layers make human history a thin film."),
            ("Act I", "Uniformitarianism and Earth’s age expand."),
            ("Act II", "Variation, selection, common descent."),
            ("Act III", "Controversies; later genetics join (preview lightly)."),
            ("Act IV", "Next: telegraph to computing as global nerves."),
        ],
        evidence=[
            ("Common descent and evolution of life", "Established"),
            ("Natural selection as a major mechanism", "Established"),
            ("19th-century age-of-Earth estimates", "Historically incomplete vs modern"),
        ],
        myths=[
            ("Evolution means progress up a ladder", "Branching, not ladder"),
            ("Darwin invented deep time alone", "Geology paved the way"),
        ],
        debates=[
            "Historical reception across cultures",
            "How much to preview modern genetics here vs S3E29",
        ],
        visuals=[
            "Strata clock",
            "Tree of life (not ladder)",
            "Selection mini-simulation",
        ],
        terms=["Deep time", "Natural selection", "Common descent", "Uniformitarianism"],
        dont=[
            "Do not revive ladder thinking.",
            "Do not caricature religious responses as one bloc.",
        ],
        s_pointer="S1E33; biology returns in S3E29 and S4.",
    ),
    make(
        n=26,
        slug="electricity-computing-and-early-global-nerves",
        title="Electricity, Computing, and Early Global Nerves",
        logline="From telegraph to early computers—information accelerates before the post-1940 institutional aftermath.",
        from_ep="S3E25 Darwin, Deep Time, and Remaking Life’s Story",
        to_ep="S3E27 After 1940: Institutions of Cooperation",
        deepens="S1 Ep. 33",
        goals=[
            "Trace telegraph, radio, and early computing.",
            "Show information as a new kind of infrastructure.",
            "Stop before full digital present—hand later shrinkage to E28.",
            "Hand off to mid-century cooperation institutions.",
        ],
        acts=[
            ("Cold open", "Pulse across an ocean cable"),
            ("Act I", "Electric messages"),
            ("Act II", "Computation machines"),
            ("Act III", "World as nervous system"),
            ("Act IV", "Baton → post-1940 order"),
        ],
        beats=[
            ("Cold open", "A cable carries a thought under the sea."),
            ("Act I", "Telegraph and radio shrink delay."),
            ("Act II", "From calculators to wartime/early electronic computers."),
            ("Act III", "Coordination and control intensify."),
            ("Act IV", "Next: institutions after 1940."),
        ],
        evidence=[
            ("Electric telecommunication transforms coordination", "Established"),
            ("Early electronic computing emerges mid-20th century", "Established"),
            ("Social effects of acceleration", "Complex / Active debate"),
        ],
        myths=[
            ("The internet appears from nowhere in the 1990s", "Long electrical/computing prelude"),
            ("Information tech is politically neutral by nature", "Always embedded in power"),
        ],
        debates=[
            "Military vs civilian drivers of computing",
            "How much E26 vs E28 should carry the digital story",
        ],
        visuals=[
            "Cable map lighting up",
            "Early computer room reconstruction",
            "Delay-time collapse chart",
        ],
        terms=["Telegraph", "Radio", "Computer", "Latency", "Infrastructure"],
        dont=[
            "Do not dump the entire internet age here.",
            "Do not ignore colonial and military contexts.",
        ],
        s_pointer="S1E33; digital village deepens in S3E28.",
    ),
    make(
        n=27,
        slug="after-1940-institutions-of-cooperation",
        title="After 1940: Institutions of Cooperation",
        logline="What the mid-century order built—UN system, law language, public goods—and its fractures.",
        from_ep="S3E26 Electricity, Computing, and Early Global Nerves",
        to_ep="S3E28 The Shrinking Planet: Media, Networks, Global Village",
        deepens="S1 Ep. 34",
        goals=[
            "Map post-1940 cooperation institutions accessibly.",
            "Show public goods: health, standards, development, peacekeeping ideals.",
            "Admit failures, exclusions, and power politics.",
            "Hand off to media/networks shrinking the planet.",
        ],
        acts=[
            ("Cold open", "Charter signed; mushroom cloud still in memory"),
            ("Act I", "Architecture of order"),
            ("Act II", "Public goods"),
            ("Act III", "Fractures"),
            ("Act IV", "Baton → global village media"),
        ],
        beats=[
            ("Cold open", "Cooperation language born under catastrophe’s shadow."),
            ("Act I", "UN system and related institutions—map, not worship."),
            ("Act II", "Standards, health campaigns, technical agencies."),
            ("Act III", "Cold War, vetoes, inequalities, broken promises."),
            ("Act IV", "Next: jets, satellites, digital nets."),
        ],
        evidence=[
            ("Post-1945 international institutions were created", "Established"),
            ("Some public-goods successes (e.g., aspects of health coordination)", "Established examples"),
            ("Net effectiveness overall", "Active debate"),
        ],
        myths=[
            ("The UN ended war", "Conflicts continue"),
            ("International order is purely altruistic", "Power politics remain"),
        ],
        debates=[
            "Reform vs replacement of institutions",
            "How to measure institutional success",
        ],
        visuals=[
            "Institution org-chart globe",
            "Success/fracture split montage",
            "Charter-to-crisis timeline",
        ],
        terms=["UN system", "Public goods", "International law", "Sovereignty"],
        dont=[
            "Do not produce propaganda for or against the UN.",
            "Do not ignore Global South critiques.",
        ],
        s_pointer="S1E34; leads to S3E28.",
    ),
    make(
        n=28,
        slug="the-shrinking-planet-media-networks-global-village",
        title="The Shrinking Planet: Media, Networks, Global Village",
        logline="Jets, satellites, and digital nets—feeling like one village while inequalities and fractures remain.",
        from_ep="S3E27 After 1940: Institutions of Cooperation",
        to_ep="S3E29 Genes, Medicine, and Planetary Risk",
        deepens="S1 Ep. 34",
        goals=[
            "Show transport and media collapsing distance.",
            "Explain global village feeling vs uneven access.",
            "Connect networks to culture, markets, and politics.",
            "Hand off to biotech and planetary risk.",
        ],
        acts=[
            ("Cold open", "Same song heard on six continents"),
            ("Act I", "Distance collapses"),
            ("Act II", "Media nervous system"),
            ("Act III", "Village illusions"),
            ("Act IV", "Baton → genes and planetary risk"),
        ],
        beats=[
            ("Cold open", "A broadcast or feed makes Earth feel simultaneous."),
            ("Act I", "Aviation, satellites, container shipping."),
            ("Act II", "TV to internet to platforms."),
            ("Act III", "Shared attention ≠ shared power or shared fate equally."),
            ("Act IV", "Next: editable biology and geological-force humans."),
        ],
        evidence=[
            ("Transport and telecom reduced effective distance", "Established"),
            ("Digital networks globalized cultural flows", "Established"),
            ("Global village as equal community", "Metaphor; empirically uneven"),
        ],
        myths=[
            ("Everyone is equally connected", "Access gaps remain"),
            ("More connection automatically means more understanding", "Not guaranteed"),
        ],
        debates=[
            "Platform power and democracy",
            "Cultural homogenization vs hybridization",
        ],
        visuals=[
            "Flight and cable density maps",
            "Latency collapse chart",
            "Uneven light of connectivity at night",
        ],
        terms=["Global village", "Satellite", "Platform", "Latency", "Network"],
        dont=[
            "Do not sell tech utopia.",
            "Do not ignore surveillance and misinformation lightly.",
        ],
        s_pointer="S1E34; leads to S3E29.",
    ),
    make(
        n=29,
        slug="genes-medicine-and-planetary-risk",
        title="Genes, Medicine, and Planetary Risk",
        logline="Biology becomes editable; humans become a geological force—twin modern conditions.",
        from_ep="S3E28 The Shrinking Planet: Media, Networks, Global Village",
        to_ep="S3E30 The Human Story So Far",
        deepens="S1 Ep. 34–35 → S4",
        goals=[
            "Introduce genetics/medicine transformations accessibly.",
            "Pair biotech promise with ethical risk.",
            "Restate humans as Earth-system force.",
            "Hand unfinished questions toward Season 4.",
            "Prepare season synthesis.",
        ],
        acts=[
            ("Cold open", "Double helix beside Earth from space"),
            ("Act I", "Medicine and genes"),
            ("Act II", "Editability"),
            ("Act III", "Planetary risk"),
            ("Act IV", "Baton → season synthesis"),
        ],
        beats=[
            ("Cold open", "Two powers: rewrite life; reshape planet."),
            ("Act I", "Vaccines, antibiotics, genetics—life expectancy shifts."),
            ("Act II", "Editing and engineering raise governance questions."),
            ("Act III", "Climate, biosphere, extinction, weapons—risk portfolio."),
            ("Act IV", "Next: synthesize Season 3; open Frontiers."),
        ],
        evidence=[
            ("Germ theory and modern medicine transformed mortality", "Established"),
            ("DNA as hereditary material; genetic technologies advancing", "Established"),
            ("Humans altering Earth system at planetary scale", "Established"),
            ("Long-term governance of gene editing", "Active debate"),
        ],
        myths=[
            ("Science fiction editing is already unlimited utopia", "Capabilities and limits both real"),
            ("Planetary risk is only climate", "Multiple interacting risks"),
        ],
        debates=[
            "Ethical boundaries of human germline editing",
            "How to prioritize existential vs chronic risks",
        ],
        visuals=[
            "Helix + Earth split emblem",
            "Life-expectancy curve",
            "Risk portfolio dashboard (non-alarmist)",
        ],
        terms=["Genetics", "Gene editing", "Planetary risk", "Earth system"],
        dont=[
            "Do not give actionable weaponization or pathogen enhancement detail.",
            "Do not end in pure despair or pure techno-salvation.",
        ],
        s_pointer="Hands many threads to Season 4 Frontiers.",
    ),
    make(
        n=30,
        slug="the-human-story-so-far",
        title="The Human Story So Far",
        logline="Synthesize Season 3—from primates to planetary risk—and hand unfinished questions to Frontiers.",
        from_ep="S3E29 Genes, Medicine, and Planetary Risk",
        to_ep="Season 4 — Frontiers",
        deepens="S1 Ep. 23–35 synthesis",
        goals=[
            "Retell Season 3 as one causal chain of batons.",
            "Separate Established human-science spine from open debates.",
            "List questions reserved for Season 4.",
            "Close the human depth map without false completion.",
        ],
        acts=[
            ("Cold open", "Primate hand → city light → Earth at night"),
            ("Act I", "Biological arc recap"),
            ("Act II", "Cultural and civilizational arc"),
            ("Act III", "Modern condition"),
            ("Act IV", "Open questions → Season 4"),
        ],
        beats=[
            ("Cold open", "A montage from trees to satellites."),
            ("Act I", "Primates → bipedalism → tools → many humans → sapiens journeys → minds."),
            ("Act II", "Foragers → farming → complexity → cradles → Axial → faiths → knowledge → industry."),
            ("Act III", "Networks, institutions, editable biology, planetary force."),
            ("Act IV", "Frontiers: consciousness, futures, meaning, unfinished science."),
        ],
        evidence=[
            ("Season spine claims remain on their prior ladders", "Mixed — restate honestly"),
            ("Human story is finished", "False"),
        ],
        myths=[
            ("Season 3 answered everything about humans", "Depth map, not omniscience"),
            ("History ends at the present", "Frontiers continue"),
        ],
        debates=[
            "Which open questions deserve Season 4 priority",
            "How to keep humility without paralysis",
        ],
        visuals=[
            "Season 3 subway-map of episodes",
            "Evidence-ladder wall of greatest hits",
            "Door opening to Season 4 title card",
        ],
        terms=["Synthesis", "Baton", "Evidence ladder", "Frontier"],
        dont=[
            "Do not invent new factual claims not earned in prior episodes.",
            "Do not close with prophecy presented as fact.",
        ],
        s_pointer="Season 4 — Frontiers.",
    ),
]


def main():
    assert len(EPS) == 30, len(EPS)
    for i, e in enumerate(EPS):
        next_title = EPS[i + 1]["title"] if i + 1 < len(EPS) else ""
        path = OUT / f"ep-{e['n']:02d}-{e['slug']}.md"
        path.write_text(render(e, next_title), encoding="utf-8")
        print("wrote", path.name)
    # README index
    lines = [
        "# Season 3 — Detailed Episode Treatments",
        "",
        "Phase 3 expansions for **The Human Story** (30 episodes).",
        "",
        "Phase 1 outline: [../season-03-the-human-story.md](../season-03-the-human-story.md)",
        "",
        "| Ep | Title | File |",
        "| --- | --- | --- |",
    ]
    for e in EPS:
        fname = f"ep-{e['n']:02d}-{e['slug']}.md"
        lines.append(f"| {e['n']} | {e['title']} | [{fname}]({fname}) |")
    lines.append("")
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print("wrote README.md")


if __name__ == "__main__":
    main()
