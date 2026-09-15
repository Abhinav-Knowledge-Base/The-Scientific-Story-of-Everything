#!/usr/bin/env python3
"""Generate Season 4 Phase 3 detailed episode treatments."""
from pathlib import Path
import re

OUT = Path(__file__).resolve().parent / "episodes"
OUT.mkdir(parents=True, exist_ok=True)
OUTLINE = Path(__file__).resolve().parent.parent / "season-04-frontiers.md"


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
    if ep["n"] == 15:
        handoff = (
            "→ **Audience / next telling** — the story continues in what we learn and choose.\n\n"
            "Series Phase 3 complete for Season 4 — Frontiers coda delivered."
        )
    else:
        handoff = f"→ **S4E{ep['n']+1:02d} {next_title}**"

    return f"""# S4E{ep['n']:02d} — {ep['title']}

**Season:** 4 — Frontiers  
**Series question:** *How did we get here?* (unfinished questions)  
**Logline:** {ep['logline']}

**Phase 1 outline:** [../../season-04-frontiers.md](../../season-04-frontiers.md) (Episode {ep['n']})  
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
**Unknown:** See Active debate / Unknown / Speculation rows and open questions.  
**Better evidence:** Sharper observations, experiments, and honest speculation labels.

---

## Baton handoff

{handoff}
"""


def make(**kwargs):
    return kwargs


EPS = [
    make(
        n=1,
        slug="are-we-alone",
        title="Are We Alone?",
        logline="Exoplanets, biosignatures, and the solitude question — without fake precision.",
        from_ep="Season 3 close / Season 1 Episode 35 open questions",
        to_ep="S4E02 Searching for Life in the Solar System",
        deepens="S1 Ep. 35; S2 Ep. 21",
        goals=[
            "Frame the solitude question as empirical, not mystical.",
            "Separate life, complex life, and detectable technology.",
            "Introduce biosignature vs technosignature strategies.",
            "Present the Fermi puzzle carefully, without slogan answers.",
            "Hand off to the near hunt in the Solar System.",
        ],
        acts=[
            ("Cold open", "One pale blue dot becomes a sky of dots"),
            ("Act I", "Worlds everywhere"),
            ("Act II", "What would count as life elsewhere"),
            ("Act III", "The silence problem"),
            ("Act IV", "Baton → local hunt"),
        ],
        beats=[
            ("Cold open", "Exoplanet census lights up — solitude becomes a testable question."),
            ("Act I", "Demographics of planets; habitability as a range, not a binary."),
            ("Act II", "Biosignatures and technosignatures as different bets."),
            ("Act III", "Fermi framing: absence of evidence is not one neat paradox answer."),
            ("Act IV", "Next: Mars, icy moons, Titan — the near hunt."),
        ],
        evidence=[
            ("Exoplanets are common", "Established"),
            ("Life exists elsewhere", "Unknown"),
            ("Where 'Great Filters' sit, if any", "Speculation / Active debate"),
        ],
        myths=[
            ("No aliens yet means we are alone", "Search coverage is tiny"),
            ("Habitable zone equals inhabited", "Necessary conditions are not sufficient"),
        ],
        debates=[
            "Abiogenesis frequency in the universe",
            "Whether silence updates beliefs strongly yet",
        ],
        visuals=[
            "Pale dots multiplying across the sky",
            "Biosignature vs technosignature fork",
            "Fermi puzzle as open flowchart, not riddle punchline",
        ],
        terms=["Exoplanet", "Biosignature", "Technosignature", "Fermi paradox (careful framing)"],
        dont=[
            "Do not invent a precise probability that we are alone.",
            "Do not treat UFO folklore as established contact.",
        ],
        s_pointer="S2E21 origin/habitability threads; continues to S4E02.",
    ),
    make(
        n=2,
        slug="searching-for-life-in-the-solar-system",
        title="Searching for Life in the Solar System",
        logline="Mars, icy moons, Titan — the near hunt made local and testable.",
        from_ep="S4E01 Are We Alone?",
        to_ep="S4E03 Listening and Looking: SETI and Biosignature Science",
        deepens="S1 Ep. 35; S2 origin arc",
        goals=[
            "Survey best Solar System targets with evidence standards.",
            "Explain past water on Mars and ocean-world cases.",
            "Flag organics vs life, and false-positive risks.",
            "Introduce planetary protection ethics.",
            "Hand off to how SETI and biosignature science actually work.",
        ],
        acts=[
            ("Cold open", "Drill bit above an ice crust"),
            ("Act I", "Mars"),
            ("Act II", "Ocean worlds and Titan"),
            ("Act III", "Contamination and false positives"),
            ("Act IV", "Baton → search methods"),
        ],
        beats=[
            ("Cold open", "A plume or sample return fantasy meets hard protocol."),
            ("Act I", "Past habitability of Mars; present subsurface bets."),
            ("Act II", "Europa, Enceladus, and Titan's chemistry as distinct experiments."),
            ("Act III", "Second genesis vs shared ancestry; don't contaminate the answer."),
            ("Act IV", "Next: instruments, strategies, and null results."),
        ],
        evidence=[
            ("Mars once had liquid water environments", "Established"),
            ("Subsurface oceans on some icy moons", "Strong inference / Established for select cases"),
            ("Extant or past life in the Solar System beyond Earth", "Unknown"),
        ],
        myths=[
            ("Organics equal life", "Chemistry can be abiotic"),
            ("Finding microbes on Mars would settle Fermi", "Local ≠ cosmic"),
        ],
        debates=[
            "Best next target for life detection",
            "Second genesis vs panspermia/shared ancestry",
        ],
        visuals=[
            "Icy-moon cutaways with plume sampling",
            "Mars timeline: wet past → cold present",
            "Planetary-protection checklist graphic",
        ],
        terms=["Ocean world", "Planetary protection", "False positive", "Second genesis"],
        dont=[
            "Do not announce hypothetical detections as fact.",
            "Do not ignore contamination ethics.",
        ],
        s_pointer="S2 origin arc; leads to S4E03 methods.",
    ),
    make(
        n=3,
        slug="listening-and-looking-seti-and-biosignature-science",
        title="Listening and Looking: SETI and Biosignature Science",
        logline="How the search actually works — instruments, strategies, evidence standards, and null results.",
        from_ep="S4E02 Searching for Life in the Solar System",
        to_ep="S4E04 Consciousness",
        deepens="S1 Ep. 35; S2 Ep. 26 (methods)",
        goals=[
            "Explain radio/optical SETI and atmospheric spectroscopy accessibly.",
            "Define what would count as evidence.",
            "Review historical false alarms as cautionary tales.",
            "Preview upcoming observatories without hype.",
            "Hand off from cosmic loneliness to minds.",
        ],
        acts=[
            ("Cold open", "A candidate signal — then the checklist"),
            ("Act I", "Listening"),
            ("Act II", "Looking at atmospheres"),
            ("Act III", "Nulls and belief updates"),
            ("Act IV", "Baton → consciousness"),
        ],
        beats=[
            ("Cold open", "Excitement meets verification protocol."),
            ("Act I", "Radio and optical SETI strategies; sky coverage honesty."),
            ("Act II", "Spectroscopic biosignature hunts and ambiguity."),
            ("Act III", "How long silence should (and shouldn't) update beliefs."),
            ("Act IV", "Next: what it means for the universe to feel like something."),
        ],
        evidence=[
            ("Search methods for biosignatures and technosignatures exist and are improving", "Established"),
            ("Confirmed extraterrestrial intelligence signal", "None established"),
            ("How strongly current nulls constrain life elsewhere", "Active debate"),
        ],
        myths=[
            ("SETI already proved we are alone", "Coverage is limited"),
            ("One weird spectral line equals life", "Needs multi-line, multi-test confirmation"),
        ],
        debates=[
            "Bayesian weight of prolonged silence",
            "Best next-generation survey strategies",
        ],
        visuals=[
            "Spectrum fingerprint cards",
            "Survey sky-coverage heatmaps",
            "False-alarm museum wall",
        ],
        terms=["SETI", "Biosignature", "Null result", "Spectroscopy", "Technosignature"],
        dont=[
            "Do not treat unverified anomalies as contact.",
            "Do not oversell upcoming missions as guaranteed answers.",
        ],
        s_pointer="Methods ethos echoes S2; mind arc begins S4E04.",
    ),
    make(
        n=4,
        slug="consciousness",
        title="Consciousness",
        logline="What it means for the universe to feel like something from inside — correlates, theories, and the gap.",
        from_ep="S4E03 Listening and Looking: SETI and Biosignature Science",
        to_ep="S4E05 Other Minds on Earth",
        deepens="S1 Ep. 26, 35; S3 Ep. 8–11",
        goals=[
            "Map neural correlates without claiming the hard problem is solved.",
            "Survey major theories at high level with evidence badges.",
            "Keep worldview windows secondary to the science map.",
            "Hand off to other minds on Earth before machines.",
        ],
        acts=[
            ("Cold open", "Lights on in a brain — then the gap"),
            ("Act I", "Correlates"),
            ("Act II", "Theory map"),
            ("Act III", "Explanatory gap and worldviews"),
            ("Act IV", "Baton → animal minds"),
        ],
        beats=[
            ("Cold open", "Experience accompanies brain processes — why remains open."),
            ("Act I", "What neuroscience can and cannot localize."),
            ("Act II", "Competing frameworks: useful maps, not settled crowns."),
            ("Act III", "Science first; brief comparative worldview window."),
            ("Act IV", "Next: minds that evolved beside ours."),
        ],
        evidence=[
            ("Conscious experience correlates with brain processes", "Established broad"),
            ("A completed theory of consciousness", "Active debate / Incomplete"),
            ("Why experience accompanies physical processes (hard problem)", "Unknown / Philosophical frontier"),
        ],
        myths=[
            ("Imaging a brain fully explains experience", "Correlates ≠ complete explanation"),
            ("Consciousness is only a human luxury", "Comparative questions come next"),
        ],
        debates=[
            "Which theory, if any, is closest",
            "Whether 'why experience' reduces to science or stays partly philosophical",
        ],
        visuals=[
            "Theory map with a gap at the center",
            "Correlate dashboard with humility labels",
            "Worldview window as a side panel, not the main stage",
        ],
        terms=["Neural correlate", "Hard problem", "Phenomenal experience", "Theory of consciousness"],
        dont=[
            "Do not declare the hard problem solved.",
            "Do not collapse the episode into religious advocacy or attack.",
        ],
        s_pointer="S3 mind arc; continues to S4E05.",
    ),
    make(
        n=5,
        slug="other-minds-on-earth",
        title="Other Minds on Earth",
        logline="Animal minds and the ethics of the more-than-human world — a tree of minds, not a ladder.",
        from_ep="S4E04 Consciousness",
        to_ep="S4E06 Intelligence Beyond Biology?",
        deepens="S1 Ep. 26; S3 culture arc",
        goals=[
            "Survey comparative cognition across mammals, birds, cephalopods.",
            "Separate intelligence, sentience, and human-like mind carefully.",
            "Show evolution's multiple experiments with mind.",
            "Raise ethics without turning the episode into a sermon.",
            "Hand off to machine intelligence questions.",
        ],
        acts=[
            ("Cold open", "Octopus and crow solve different puzzles"),
            ("Act I", "Comparative cognition"),
            ("Act II", "Sentience debates"),
            ("Act III", "Ethics of the more-than-human"),
            ("Act IV", "Baton → AI"),
        ],
        beats=[
            ("Cold open", "Different lineages, different minds — no single ladder."),
            ("Act I", "Evidence from behavior, neurology, ecology."),
            ("Act II", "Where measurement ends and uncertainty begins."),
            ("Act III", "What recognition of other minds implies for treatment."),
            ("Act IV", "Next: intelligence beyond biology?"),
        ],
        evidence=[
            ("Many animals show complex cognition", "Established"),
            ("Sentience in specific taxa", "Strong inference for some; Active debate for others"),
            ("Exact inner experience of nonhuman animals", "Unknown"),
        ],
        myths=[
            ("Only humans have minds worth considering", "Comparative evidence contradicts"),
            ("Smarter means more ladder-like toward us", "Branching experiments"),
        ],
        debates=[
            "Which species meet which sentience criteria",
            "How to measure mind without anthropomorphism",
        ],
        visuals=[
            "Tree of minds (not a ladder)",
            "Puzzle-solving montage across taxa",
            "Measurement vs humility dial",
        ],
        terms=["Comparative cognition", "Sentience", "Anthropomorphism", "More-than-human"],
        dont=[
            "Do not invent animal inner monologues as fact.",
            "Do not use a human-top ladder graphic.",
        ],
        s_pointer="S3 culture/mind; leads to S4E06.",
    ),
    make(
        n=6,
        slug="intelligence-beyond-biology",
        title="Intelligence Beyond Biology?",
        logline="AI capabilities, limits, and civilizational stakes — speculation clearly badged.",
        from_ep="S4E05 Other Minds on Earth",
        to_ep="S4E07 The Future of Earth's Climate",
        deepens="S1 Ep. 34; S3 Ep. 26–28",
        goals=[
            "Separate real ML capabilities from myth.",
            "Distinguish intelligence from consciousness.",
            "Introduce alignment and governance accessibly.",
            "Link to human–machine coevolution and S3 networks.",
            "Hand off to Earth climate futures.",
        ],
        acts=[
            ("Cold open", "Tool → partner → unknown continuum"),
            ("Act I", "What AI can and cannot do now"),
            ("Act II", "Intelligence vs consciousness"),
            ("Act III", "Stakes and governance"),
            ("Act IV", "Baton → climate futures"),
        ],
        beats=[
            ("Cold open", "A capability slider with speculation badges."),
            ("Act I", "Pattern learning, limits, and hype cycles."),
            ("Act II", "Performance is not automatically experience."),
            ("Act III", "Alignment, misuse, concentration of power — accessible."),
            ("Act IV", "Next: the planet's climate under human choice."),
        ],
        evidence=[
            ("Machine learning systems have rapidly expanding capabilities", "Established"),
            ("Current systems are conscious", "Speculation / Not established"),
            ("Path and timeline to AGI", "Active debate / Speculation"),
        ],
        myths=[
            ("AI already equals human general mind", "Capabilities are uneven and bounded"),
            ("If it talks fluently, it must feel", "Language ≠ proven consciousness"),
        ],
        debates=[
            "Whether AGI is inevitable, contingent, or misframed",
            "Governance models that match pace of change",
        ],
        visuals=[
            "Tool → partner → unknown continuum",
            "Capability vs consciousness split axes",
            "Governance checklist (non-alarmist, non-naive)",
        ],
        terms=["Machine learning", "AGI (contested)", "Alignment", "Intelligence vs consciousness"],
        dont=[
            "Do not present sci-fi takeover as Established fact.",
            "Do not give actionable harm instructions.",
        ],
        s_pointer="S3E26–28; Earth futures arc opens at S4E07.",
    ),
    make(
        n=7,
        slug="the-future-of-earths-climate",
        title="The Future of Earth's Climate",
        logline="Scenarios under human influence — physics constraints, human choices, irreversible risks.",
        from_ep="S4E06 Intelligence Beyond Biology?",
        to_ep="S4E08 Biosphere Futures",
        deepens="S1 Ep. 35; S2 Ep. 15; S3 Ep. 29",
        goals=[
            "Present projections as scenario fans, not single prophecies.",
            "Tie impacts to S2 climate engines.",
            "Cover mitigation and adaptation without false comfort.",
            "Flag tipping and irreversibility risks honestly.",
            "Hand off to living biosphere futures.",
        ],
        acts=[
            ("Cold open", "Scenario fan opening from today"),
            ("Act I", "Physics constraints"),
            ("Act II", "Impacts"),
            ("Act III", "Choices: mitigate and adapt"),
            ("Act IV", "Baton → biosphere"),
        ],
        beats=[
            ("Cold open", "Multiple futures branch from emissions pathways."),
            ("Act I", "Greenhouse physics and Earth-system feedbacks."),
            ("Act II", "Heat, water, extremes, seas — human stakes."),
            ("Act III", "Mitigation, adaptation, limits; politics labeled as such."),
            ("Act IV", "Next: extinction, restoration, engineered life."),
        ],
        evidence=[
            ("Human greenhouse-gas emissions are warming the climate", "Established"),
            ("Higher emissions pathways bring larger risks", "Established"),
            ("Exact tipping thresholds and timing", "Active debate / Incomplete"),
            ("Political-economic feasibility of pathways", "Not purely scientific — label clearly"),
        ],
        myths=[
            ("Climate futures are pure guesswork", "Constrained by physics and observations"),
            ("One cold winter disproves warming", "Weather ≠ climate trend"),
        ],
        debates=[
            "Climate sensitivity refinement",
            "Roles of technology vs behavior vs institutions",
        ],
        visuals=[
            "Scenario fan graphics",
            "Choice nodes on a pathway map",
            "Earth-system feedback loop board",
        ],
        terms=["Projection", "Mitigation", "Adaptation", "Tipping risk", "Scenario"],
        dont=[
            "Do not pretend outcomes are independent of human choice.",
            "Do not preach; show constraints and trade-offs.",
        ],
        s_pointer="S2E15; S3E29; continues to S4E08.",
    ),
    make(
        n=8,
        slug="biosphere-futures",
        title="Biosphere Futures",
        logline="Extinction, restoration, and engineering the living world — without naive techno-salvation.",
        from_ep="S4E07 The Future of Earth's Climate",
        to_ep="S4E09 The Future of Cooperation",
        deepens="S1 Ep. 35; S3 Ep. 29",
        goals=[
            "Map biodiversity trajectories and drivers.",
            "Show restoration and novel ecosystems honestly.",
            "Balance biotech gifts with ecological risks.",
            "Keep values visible without turning into propaganda.",
            "Hand off to cooperation futures.",
        ],
        acts=[
            ("Cold open", "Empty habitat / refilled habitat split"),
            ("Act I", "Loss drivers"),
            ("Act II", "Restoration and novel ecosystems"),
            ("Act III", "Engineering life"),
            ("Act IV", "Baton → cooperation"),
        ],
        beats=[
            ("Cold open", "Silence in a forest; then a restoration crew."),
            ("Act I", "Habitat loss, climate, exploitation, invasives."),
            ("Act II", "What can recover; what becomes permanently novel."),
            ("Act III", "Biotech ecology: promise, risk, governance."),
            ("Act IV", "Next: institutions for a planetary species."),
        ],
        evidence=[
            ("Human activity is driving elevated extinction rates", "Established"),
            ("Some restoration can recover functions", "Established examples"),
            ("Safe limits of engineering ecosystems/life", "Active debate"),
        ],
        myths=[
            ("Extinction is only prehistoric megafauna news", "Ongoing biodiversity crisis"),
            ("Technology will automatically fix nature", "Not guaranteed; can worsen risks"),
        ],
        debates=[
            "Reversibility of losses",
            "Ethics of de-extinction and gene drives (high-level only)",
        ],
        visuals=[
            "Empty vs refilled habitats",
            "Seed-vault and corridor maps",
            "Risk/gift balance scale for biotech",
        ],
        terms=["Biodiversity", "Restoration", "Novel ecosystem", "Extinction debt"],
        dont=[
            "Do not give actionable ecological-harm or weaponization detail.",
            "Do not sell techno-salvation as Established.",
        ],
        s_pointer="S3E29; leads to S4E09.",
    ),
    make(
        n=9,
        slug="the-future-of-cooperation",
        title="The Future of Cooperation",
        logline="After 1940's institutions — reforming or replacing cooperative systems for a planetary species.",
        from_ep="S4E08 Biosphere Futures",
        to_ep="S4E10 Civilizations That Last",
        deepens="S1 Ep. 34; S3 Ep. 27–28",
        goals=[
            "Extend S3's institutional story into unfinished governance.",
            "Frame climate and AI as coordination tests.",
            "Center inclusion in the 'global village.'",
            "Admit fragility and legitimacy problems.",
            "Hand off to long-term civilization requirements.",
        ],
        acts=[
            ("Cold open", "Village with missing houses"),
            ("Act I", "Inherited architecture"),
            ("Act II", "New coordination tests"),
            ("Act III", "Reform, replace, include"),
            ("Act IV", "Baton → lasting civilizations"),
        ],
        beats=[
            ("Cold open", "A connected planet still has empty seats at the table."),
            ("Act I", "UN-era tools and their limits (recap lightly)."),
            ("Act II", "Climate, pandemics, AI, inequality as stress tests."),
            ("Act III", "Legitimacy, public goods, new forms of cooperation."),
            ("Act IV", "Next: what long-term humanity would require."),
        ],
        evidence=[
            ("Global coordination problems are intensifying", "Strong inference / Established broad"),
            ("Existing institutions sometimes deliver public goods", "Established examples"),
            ("Which future institutional form will work", "Active debate / Speculation"),
        ],
        myths=[
            ("The global village already includes everyone equally", "Access and power remain uneven"),
            ("More technology automatically produces cooperation", "Can also polarize and concentrate power"),
        ],
        debates=[
            "Reform vs replacement of mid-century order",
            "How to build legitimacy across unequal states and peoples",
        ],
        visuals=[
            "Institution blueprint overlays",
            "Village with missing houses",
            "Coordination-test scorecards",
        ],
        terms=["Public goods", "Coordination problem", "Legitimacy", "Global governance"],
        dont=[
            "Do not produce partisan campaign material.",
            "Do not pretend one blueprint is scientifically proven.",
        ],
        s_pointer="S3E27–28; leads to S4E10.",
    ),
    make(
        n=10,
        slug="civilizations-that-last",
        title="Civilizations That Last",
        logline="What long-term humanity would require — resilience, transitions, archives, intergenerational ethics.",
        from_ep="S4E09 The Future of Cooperation",
        to_ep="S4E11 Leaving Earth?",
        deepens="S1 Ep. 35; S3 Ep. 29–30",
        goals=[
            "Survey collapse and resilience patterns without fatalism.",
            "Cover energy/materials transitions and knowledge preservation.",
            "Introduce intergenerational ethics accessibly.",
            "Connect risk literacy to constructive longevity.",
            "Hand off to space settlement dreams vs stewardship.",
        ],
        acts=[
            ("Cold open", "Civilization lifespan bars"),
            ("Act I", "Failure modes and resilience"),
            ("Act II", "Energy, materials, knowledge"),
            ("Act III", "Ethics of the future"),
            ("Act IV", "Baton → leaving Earth?"),
        ],
        beats=[
            ("Cold open", "Many civilizations end; some transform."),
            ("Act I", "Historical patterns; modern risk portfolio."),
            ("Act II", "Transitions that keep options open; archives that outlast crises."),
            ("Act III", "What we owe people not yet born."),
            ("Act IV", "Next: space settlement — dream meet physics."),
        ],
        evidence=[
            ("Complex societies can fail or transform under stress", "Established historical"),
            ("Long-term energy and materials transitions are required for durability", "Strong inference"),
            ("A single recipe for civilizational immortality", "Speculation"),
        ],
        myths=[
            ("Collapse is always sudden apocalypse", "Often uneven, partial, transformational"),
            ("Flourishing means endless growth only", "Definitions contested"),
        ],
        debates=[
            "Dominant near-century risks",
            "How to define and measure flourishing",
        ],
        visuals=[
            "Civilization lifespan bars",
            "Bridge-across-centuries graphic",
            "Archive / seed / knowledge vault montage",
        ],
        terms=["Resilience", "Collapse", "Intergenerational ethics", "Knowledge preservation"],
        dont=[
            "Do not romanticize collapse.",
            "Do not claim prophecy of a specific doomsday date.",
        ],
        s_pointer="S3E29–30; leads to S4E11.",
    ),
    make(
        n=11,
        slug="leaving-earth",
        title="Leaving Earth?",
        logline="Space settlement dreams meet physics, biology, and ethics — escape is not a substitute for stewardship.",
        from_ep="S4E10 Civilizations That Last",
        to_ep="S4E12 The Long Future of Earth",
        deepens="S1 Ep. 35; S3 Ep. 28",
        goals=[
            "Ground Moon/Mars/habitat ideas in bottlenecks.",
            "Explain closed-loop life support challenges.",
            "Keep planetary protection and ethics in frame.",
            "Reject 'abandon Earth' as a moral or practical free pass.",
            "Hand off to Earth's deep future beyond civilization timescales.",
        ],
        acts=[
            ("Cold open", "Fragile can vs blue Earth"),
            ("Act I", "Dreams and physics"),
            ("Act II", "Biology and closed loops"),
            ("Act III", "Ethics and stewardship"),
            ("Act IV", "Baton → long Earth future"),
        ],
        beats=[
            ("Cold open", "A habitat can beside an ocean world."),
            ("Act I", "Delta-v, radiation, cost, industry — bottlenecks."),
            ("Act II", "Life support, reproduction, ecosystems in cans."),
            ("Act III", "Who goes; who stays; contamination; Earth still home."),
            ("Act IV", "Next: planetary chapters until the Sun rewrites the ending."),
        ],
        evidence=[
            ("Humans have temporary presence off Earth", "Established"),
            ("Self-sufficient settlements are currently unrealized", "Established"),
            ("Feasible timelines for large settlements", "Active debate / Speculation vs hype"),
        ],
        myths=[
            ("Mars is a ready backup planet", "Hostile; not a drop-in Earth"),
            ("Spaceflight removes the need to care for Earth", "False ethically and practically"),
        ],
        debates=[
            "Near-term priorities: science outposts vs settlement rhetoric",
            "Ethics of multi-generational confinement off-world",
        ],
        visuals=[
            "Fragile cans vs blue Earth",
            "Bottleneck checklist",
            "Closed-loop schematic with failure points",
        ],
        terms=["Life support", "Closed loop", "Delta-v", "Planetary protection", "Settlement"],
        dont=[
            "Do not sell colony marketing as Established feasibility.",
            "Do not treat Earth as disposable.",
        ],
        s_pointer="S3E28; deep time returns in S4E12.",
    ),
    make(
        n=12,
        slug="the-long-future-of-earth",
        title="The Long Future of Earth",
        logline="Planetary chapters after us — until the Sun rewrites the ending.",
        from_ep="S4E11 Leaving Earth?",
        to_ep="S4E13 The Fate of the Universe",
        deepens="S1 Ep. 35; S2 Earth arc",
        goals=[
            "Zoom from centuries to geologic and stellar timescales.",
            "Explain long-term orbital/climate and biosphere limits.",
            "Describe red-giant-phase habitability loss accessibly.",
            "Place the human window in deep time.",
            "Hand off to cosmic fate.",
        ],
        acts=[
            ("Cold open", "Sun warming dial"),
            ("Act I", "Earth after the near future"),
            ("Act II", "Biosphere limits"),
            ("Act III", "The Sun's rewrite"),
            ("Act IV", "Baton → fate of the universe"),
        ],
        beats=[
            ("Cold open", "A dial turns; oceans feel the long heat."),
            ("Act I", "Gyr-scale climate and geology without human headlines."),
            ("Act II", "Habitability windows narrow."),
            ("Act III", "Red-giant future; Earth's surface story ends."),
            ("Act IV", "Next: how the whole cosmos might end."),
        ],
        evidence=[
            ("The Sun will eventually leave the main sequence and transform Earth", "Established stellar physics"),
            ("Exact remaining duration of surface habitability", "Active debate on details / Incomplete"),
            ("Technological extension of habitability", "Speculation"),
        ],
        myths=[
            ("Earth lasts forever as a garden", "Stellar evolution ends the surface story"),
            ("Human timescales are planetary timescales", "We are a thin film"),
        ],
        debates=[
            "Longevity estimates for complex life",
            "Whether engineering could delay the end meaningfully",
        ],
        visuals=[
            "Sun warming dial",
            "Oceans lost in deep-future animation",
            "Human window as a thin tick on a Gyr bar",
        ],
        terms=["Main sequence", "Red giant", "Habitability window", "Gyr"],
        dont=[
            "Do not give fake precise doomsday years as gospel.",
            "Do not confuse near-term climate with red-giant fate.",
        ],
        s_pointer="S2 Earth/star physics; cosmic endings in S4E13.",
    ),
    make(
        n=13,
        slug="the-fate-of-the-universe",
        title="The Fate of the Universe",
        logline="Dark energy and possible cosmic endings — heat death, rip, vacuum decay — mapped to assumptions.",
        from_ep="S4E12 The Long Future of Earth",
        to_ep="S4E14 Meaning at the Edge of Knowledge",
        deepens="S1 Ep. 35; S2 Ep. 5 (cosmology arc)",
        goals=[
            "Map ending scenarios to physical assumptions.",
            "Badge speculative tiers clearly.",
            "Keep calm awe rather than apocalypse theater.",
            "Name decisive observations that would discriminate futures.",
            "Hand off to meaning at the edge of knowledge.",
        ],
        acts=[
            ("Cold open", "Fate tree with evidence badges"),
            ("Act I", "Expansion and dark energy"),
            ("Act II", "Classic endings"),
            ("Act III", "Speculative catastrophes"),
            ("Act IV", "Baton → meaning"),
        ],
        beats=[
            ("Cold open", "Branches labeled Established / debate / speculation."),
            ("Act I", "Accelerating expansion as the observed hinge."),
            ("Act II", "Heat death as the standard long outlook under common assumptions."),
            ("Act III", "Big rip, vacuum decay — if assumptions change."),
            ("Act IV", "Next: science explains how; humans still ask what it means."),
        ],
        evidence=[
            ("Universe's expansion is accelerating", "Established"),
            ("Heat death under continuing acceleration and standard assumptions", "Strong inference"),
            ("Big rip or vacuum decay as destiny", "Speculation / depends on unknowns"),
            ("Nature of dark energy", "Active debate / Incomplete"),
        ],
        myths=[
            ("Scientists know exactly how the cosmos ends", "Depends on dark energy's nature"),
            ("Vacuum decay is scheduled for next Tuesday", "Not an Established near-term forecast"),
        ],
        debates=[
            "Equation of state of dark energy",
            "Vacuum metastability implications",
        ],
        visuals=[
            "Fate tree with evidence badges",
            "Entropy clock (conceptual)",
            "Observation dial: what would change the branch",
        ],
        terms=["Dark energy", "Heat death", "Big rip", "Vacuum decay", "Entropy"],
        dont=[
            "Do not present speculative endings as Established fact.",
            "Do not turn cosmic fate into pure horror entertainment.",
        ],
        s_pointer="Completes S2 dark-energy preview; meaning in S4E14.",
    ),
    make(
        n=14,
        slug="meaning-at-the-edge-of-knowledge",
        title="Meaning at the Edge of Knowledge",
        logline="Science explains how; humans still ask what it means — widest worldview window, bridge to the coda.",
        from_ep="S4E13 The Fate of the Universe",
        to_ep="S4E15 How Did We Get Here?",
        deepens="S1 Ep. 1, 30–31, 35; S3 Ep. 18–19",
        goals=[
            "Separate empirical claims from meaning questions.",
            "Offer a comparative worldview window without advocacy or attack.",
            "Tie to Axial/faith architecture threads from earlier seasons.",
            "Protect wonder without dogma.",
            "Hand off to the full series coda.",
        ],
        acts=[
            ("Cold open", "Evidence board vs narrative board"),
            ("Act I", "Limits of explanation"),
            ("Act II", "Worldviews as human responses"),
            ("Act III", "Shared ethics and open wonder"),
            ("Act IV", "Baton → series coda"),
        ],
        beats=[
            ("Cold open", "Two boards; a Venn of overlap and remainder."),
            ("Act I", "How far 'how' reaches; where 'why' may not reduce."),
            ("Act II", "Philosophies and religions as responses — descriptive."),
            ("Act III", "Agreement, contradiction, humility."),
            ("Act IV", "Next: How did we get here? — full synthesis."),
        ],
        evidence=[
            ("Science constrains empirical claims about the world", "Established method"),
            ("A single scientifically proven ultimate purpose", "Not Established / category error risk"),
            ("Humans across cultures ask meaning questions", "Established anthropological"),
        ],
        myths=[
            ("Science already answered why we exist", "Explains mechanisms; meaning remains contested"),
            ("Asking meaning is anti-science", "Different question types can coexist"),
        ],
        debates=[
            "Whether 'why' reduces to 'how'",
            "How to teach wonder without dogma in public science",
        ],
        visuals=[
            "Evidence board vs narrative board → Venn",
            "Quiet comparative worldview panels",
            "Open-wonder final frame (no slogan answer)",
        ],
        terms=["Meaning", "Worldview window", "Empirical claim", "Explanatory limit"],
        dont=[
            "Do not evangelize or attack religions.",
            "Do not smuggle a final metaphysical answer as Established science.",
        ],
        s_pointer="S1 Ep. 30–31; S3 Ep. 18–19; coda is S4E15.",
    ),
    make(
        n=15,
        slug="how-did-we-get-here",
        title="How Did We Get Here?",
        logline="Final synthesis of the entire project — and an invitation to continue.",
        from_ep="S4E14 Meaning at the Edge of Knowledge",
        to_ep="Audience / next telling of the story",
        deepens="Entire series",
        goals=[
            "Retell the full causal chain with S2–S4 depth echoing.",
            "Unite title and refrain on screen.",
            "Restate the standing research agenda as open.",
            "End with responsibility of knowledge — charge to the audience.",
            "Close Phase 3 for Season 4 without false completion of science.",
        ],
        acts=[
            ("Cold open", "Master timeline zoom from Planck-ish fog to now"),
            ("Act I", "Cosmos to life"),
            ("Act II", "Mind to village"),
            ("Act III", "Frontiers still open"),
            ("Act IV", "Baton to the audience"),
        ],
        beats=[
            ("Cold open", "The complete timeline breathes once."),
            ("Act I", "Cosmos → elements → Earth → life → evolution."),
            ("Act II", "Humans → prehistory → cradles → Axial → faiths/time → science → post-1940 village."),
            ("Act III", "Alone? minds? climate? cosmos? meaning? — still open."),
            ("Act IV", "The story continues in what we learn and choose; final title card."),
        ],
        evidence=[
            ("Series spine claims remain on their prior ladders", "Mixed — restate honestly"),
            ("The story is finished", "False"),
        ],
        myths=[
            ("A TV series can close science", "It can only map and invite"),
            ("Knowing the past removes responsibility for the future", "Knowledge increases stakes"),
        ],
        debates=[
            "How to tell the story next",
            "Which unknowns deserve the next generation's best effort",
        ],
        visuals=[
            "Complete master timeline",
            "Baton passed to silhouette audience",
            "Final title + refrain card: How Did We Get Here?",
        ],
        terms=["Synthesis", "Master timeline", "Research agenda", "Refrain"],
        dont=[
            "Do not invent new Established claims not earned earlier.",
            "Do not end with prophecy sold as fact.",
        ],
        s_pointer="Returns to S1 Ep. 1 with earned understanding; series coda.",
    ),
]


def link_outline():
    text = OUTLINE.read_text(encoding="utf-8")
    files = {e["n"]: f"ep-{e['n']:02d}-{e['slug']}.md" for e in EPS}
    if "Phase 3 detailed treatments" not in text:
        needle = "5. Series coda (Ep. 15)"
        idx = text.find(needle)
        if idx >= 0:
            end = text.find("\n", idx)
            insert = (
                "\n\n**Phase 3 detailed treatments:** "
                "[season-04/episodes/](season-04/episodes/README.md) — Episodes 1–15 complete."
            )
            text = text[:end] + insert + text[end:]

    lines = text.splitlines(keepends=True)
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        m = re.match(r"^## Episode (\d+)", line)
        if m:
            n = int(m.group(1))
            fname = files[n]
            k = i + 1
            while k < len(lines) and lines[k].strip() == "":
                out.append(lines[k])
                k += 1
            if k < len(lines) and lines[k].startswith("**Detailed treatment:**"):
                i = k - 1
            else:
                out.append("\n")
                out.append(
                    f"**Detailed treatment:** [season-04/episodes/{fname}](season-04/episodes/{fname})\n"
                )
                out.append("\n")
                i = k - 1
        i += 1
    OUTLINE.write_text("".join(out), encoding="utf-8")


def main():
    assert len(EPS) == 15, len(EPS)
    for i, e in enumerate(EPS):
        next_title = EPS[i + 1]["title"] if i + 1 < len(EPS) else ""
        path = OUT / f"ep-{e['n']:02d}-{e['slug']}.md"
        path.write_text(render(e, next_title), encoding="utf-8")
        print("wrote", path.name)

    lines = [
        "# Season 4 - Detailed Episode Treatments",
        "",
        "Phase 3 expansions for **Frontiers** (15 episodes).",
        "",
        "Phase 1 outline: [../season-04-frontiers.md](../season-04-frontiers.md)",
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
    link_outline()
    print("updated outline")


if __name__ == "__main__":
    main()
