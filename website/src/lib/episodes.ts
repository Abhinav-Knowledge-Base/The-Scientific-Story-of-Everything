import fs from 'node:fs';
import path from 'node:path';

export interface EpisodeMetadata {
  id: string; // e.g. season-01/ep-01-before-the-beginning
  seasonNum: number;
  seasonSlug: string;
  seasonTitle: string;
  seasonDescription: string;
  seasonBadge: string;
  epNum: number;
  slug: string;
  title: string;
  cleanTitle: string;
  coreQuestion: string;
  sequentialContext: string;
  referenceDocs: string;
  deepens?: string;
  raw: string;
  wordCount: number;
  readingMinutes: number;
  imagePrompt: string;
  imageSrc: string | null;
  prevEpisode?: { seasonSlug: string; slug: string; title: string } | null;
  nextEpisode?: { seasonSlug: string; slug: string; title: string } | null;
}

export interface SeasonInfo {
  number: number;
  slug: string;
  title: string;
  tagline: string;
  description: string;
  color: string;
  accent: string;
  icon: string;
  episodeCount: number;
  episodes: EpisodeMetadata[];
}

const SEASONS_CONFIG: Record<string, { title: string; tagline: string; description: string; color: string; accent: string; icon: string }> = {
  'season-01': {
    title: 'The Complete Story',
    tagline: '13.8 Billion Years from the Big Bang to Modern Consciousness',
    description: 'The master chronological mental map of all time: Cosmic Dawn, Earth, Life, Macroevolution, Hominins, and the slowed human finale into the modern global network.',
    color: '#3b82f6',
    accent: '#60a5fa',
    icon: '🌌',
  },
  'season-02': {
    title: 'The Deep Universe',
    tagline: 'The Physical, Chemical & Geobiological Engines of Nature',
    description: 'Deep mechanism dives: spacetime geometry, nucleosynthesis, geochemical origins of life, prebiotic membranes, and evolutionary transitions.',
    color: '#06b6d4',
    accent: '#22d3ee',
    icon: '⚛️',
  },
  'season-03': {
    title: 'The Human Story',
    tagline: 'Anthropology, Culture, Mind & Institutional Evolution',
    description: 'Deep hominin evolutionary bush, syntax, foraging bands, agricultural cradles, the Axial Age, world religions, and the Scientific Revolution.',
    color: '#f59e0b',
    accent: '#fbbf24',
    icon: '🏛️',
  },
  'season-04': {
    title: 'Frontiers',
    tagline: 'Open Questions, Existential Boundaries & Deep Time Fate',
    description: 'Astrobiology, machine minds, climate stability, civilizational longevity, the heat death of spacetime, and the overarching series coda.',
    color: '#a855f7',
    accent: '#c084fc',
    icon: '🔭',
  },
};

const MASTER_PROMPTS: Record<string, string> = {
  // Master Hero
  'master-hero': 'Grand cinematic cosmic tapestry showing the continuous unbroken timeline of reality: quantum Big Bang expansion on the left, star formation and swirling protoplanetary accretion disk in the center, primeval oceanic Earth with hydrothermal vents, ancient hominins gazing at the Milky Way, modern illuminated cities and global satellite networks on the right. IMAX 70mm cinematography, National Geographic documentary style, deep cosmic indigo and starlight gold, photorealistic, 16:9.',
  
  // Season 1
  'season-01/ep-01-before-the-beginning': 'Curved 4D spacetime geometry visualized as an undulating relativistic fabric with glowing quantum geodesics against deep cosmic darkness, Einstein-Wheeler spacetime tensor curvature, gravitational ripples, scientifically accurate theoretical physics, cinematic IMAX lighting, 16:9.',
  'season-01/ep-02-the-big-bang': 'Omnipresent metric expansion of the primordial universe at fraction of a second: ultra-hot uniform incandescent plasma expanding uniformly in all directions, blinding energy fluctuations, high-energy particle physics, cosmic dawn, photorealistic, 16:9.',
  'season-01/ep-03-the-first-seconds': 'Primordial nucleosynthesis in the early universe: glowing plasma soup of protons, neutrons, and light nuclei colliding to forge hydrogen and helium, nuclear fusion glow, blinding amber and violet thermodynamics, 16:9.',
  'season-01/ep-04-the-first-atoms': 'The Recombination Era 380,000 years after the Big Bang: neutral hydrogen atoms forming as free electrons bind with protons, the universe turning transparent for the first time, emitting the soft glowing Cosmic Microwave Background radiation, 16:9.',
  'season-01/ep-05-the-cosmic-dark-ages': 'The Cosmic Dark Ages: invisible filaments of dark matter forming an immense three-dimensional gravitational scaffolding across millions of light-years, subtle gravity wells pulling cold neutral gas clouds together, 16:9.',
  'season-01/ep-06-the-first-stars': 'Cosmic Dawn: ignition of the very first massive Population III stars in the early universe, piercing through the dark primordial hydrogen fog, intense ultraviolet reionization bubbles, awe-inspiring stellar nursery, 16:9.',
  'season-01/ep-07-the-birth-of-galaxies': 'Protogalactic assembly in the infant universe: early irregular galaxies colliding and merging along filaments of the cosmic web, glowing gas streams feeding supermassive central black holes, 16:9.',
  'season-01/ep-08-our-milky-way': 'Majestic wide-angle view of the Milky Way spiral galaxy seen from deep intergalactic space: sweeping spiral arms of billions of stars, dark dust lanes, glowing pink emission nebulae, golden galactic bulge, 16:9.',
  'season-01/ep-09-the-birth-of-the-solar-system': 'The primordial solar nebula 4.6 billion years ago: a glowing proto-Sun surrounded by a dense rotating disk of gas and dust, planetesimals and protoplanets colliding and accreting in glowing concentric rings, 16:9.',
  'season-01/ep-10-the-young-earth': 'The young Hadean Earth 4.4 billion years ago shortly after the Moon-forming collision: cooling basalt crust with molten fissures, steam condensing into the first oceans under an amber atmosphere, a giant young Moon looming close in the violet sky, 16:9.',
  'season-01/ep-11-the-first-life': 'Submarine alkaline hydrothermal vent in the primeval Archean ocean: towering porous mineral chimney emitting warm mineral-rich fluids, microscopic compartments harboring the earliest self-replicating chemical systems, bioluminescent deep-sea realism, 16:9.',
  'season-01/ep-12-what-exactly-is-life': 'Conceptual molecular thermodynamics of living systems: a dissipative metabolic protocell maintaining non-equilibrium order against entropy, pumping ions across a lipid bilayer membrane, glowing biochemical gradients, 16:9.',
  'season-01/ep-13-from-chemistry-to-life': 'Prebiotic chemistry transition: catalytic RNA molecules folding in mineral clay micro-pores, molecular self-assembly into protocells, the emergence of the Last Universal Common Ancestor (LUCA), 16:9.',
  'season-01/ep-14-the-first-cells': 'Vast Archean microbial landscape 3.5 billion years ago: dome-shaped stromatolites flourishing along shallow volcanic coastal lagoons under a hazy green-tinted sky, bacterial colonies producing early mats, 16:9.',
  'season-01/ep-15-the-great-oxygenation-event': 'The Great Oxidation Event 2.4 billion years ago: cyanobacteria oxygenating shallow seas, red banded iron formations precipitating onto the ocean floor, global glacial transition into Snowball Earth, 16:9.',
  'season-01/ep-16-the-rise-of-complex-cells': 'Endosymbiotic dawn 1.8 billion years ago: an Asgard archaeon host cell engulfing an aerobic alphaproteobacterium that evolves into the first mitochondrion, origin of the eukaryotic complex cell, 16:9.',
  'season-01/ep-17-multicellular-life': 'The Ediacaran seafloor 570 million years ago: enigmatic soft-bodied frond-like organisms like Dickinsonia and Charnia anchored in quiet marine sediment, strange primordial multicellular life, 16:9.',
  'season-01/ep-18-the-cambrian-explosion': 'The Cambrian Explosion 518 million years ago: sunlit ancient ocean teeming with biodiversity, an Anomalocaris hunting above trilobites, Opabinia, and early chordates darting through sponges, IMAX underwater cinematography, 16:9.',
  'season-01/ep-19-life-conquers-the-land': 'Late Devonian wetland 375 million years ago: Tiktaalik crawling from shallow fresh water onto mud banks with primitive lungs, towering early clubmosses and giant horsetail forests, 16:9.',
  'season-01/ep-20-the-age-of-reptiles': 'Mesozoic Jurassic forest landscape: massive sauropods grazing in misty conifer groves, pterosaurs soaring against dramatic sunset clouds, photorealistic natural history museum grade, 16:9.',
  'season-01/ep-21-mass-extinctions': 'The Cretaceous-Paleogene boundary 66 million years ago: the catastrophic Chicxulub asteroid impact in the Yucatán peninsula, fiery shockwave vaporizing rock, atmospheric firestorm seen from distance, 16:9.',
  'season-01/ep-22-the-rise-of-mammals': 'Early Eocene dawn forest 50 million years ago: small ancestral arboreal primates leaping through lush subtropical jungle canopy, diversification of adaptive mammals, 16:9.',
  'season-01/ep-23-the-human-lineage-begins': 'Late Miocene African woodland-savannah mosaic: early bipedal hominins like Ardipithecus ramidus standing upright on two legs while foraging among trees, anatomical evolutionary transition, 16:9.',
  'season-01/ep-24-the-human-evolutionary-tree': 'The bushy branching hominin tree: Australopithecus and early genus Homo tool-makers shaping Oldowan pebble choppers, collective social band around a fresh find, 16:9.',
  'season-01/ep-25-out-of-africa': 'Early Homo erectus band journeying through the Levant corridor into Eurasia: carrying Acheulean handaxes and smoldering embers, dramatic wide landscape, determination, human migration, 16:9.',
  'season-01/ep-26-the-evolution-of-the-human-mind': 'Paleolithic cave sanctuary illuminated by flickering animal-fat lamps: early Homo sapiens artist painting dynamic charcoal and ochre bison and horses onto limestone cavern walls, symbolic consciousness, 16:9.',
  'season-01/ep-27-the-ice-age': 'Late Pleistocene Last Glacial Maximum: mammoth steppe under snow-dusted tundra, Neanderthals and modern humans hunting cooperatively in mammoth-hide clothing against dramatic glacial mountain backdrop, 16:9.',
  'season-01/ep-28-after-the-ice-prehistoric-worlds': 'Early Holocene transition: monumental carved T-shaped stone pillars of Göbekli Tepe rising on a hill at sunrise, early sedentary hunter-gatherers gathering for ritual and proto-agriculture, 16:9.',
  'season-01/ep-29-the-cradles-of-civilization': 'Ancient Mesopotamian city-state of Ur at the Tigris-Euphrates delta: towering mud-brick ziggurat, irrigated canal agriculture, clay cuneiform tablets, bustling bronze-age civilization, 16:9.',
  'season-01/ep-30-the-axial-age': 'The Axial Age philosophical awakening: ancient scholars, Greek stoics, Indian Vedic thinkers, and Chinese sages in stone courtyards under starry skies, scrolls of moral philosophy, intellectual transformation, 16:9.',
  'season-01/ep-31-faiths-values-and-human-bonds': 'Vast medieval pilgrimage caravan along Silk Road oasis: multicultural travelers, shared moral codes, ancient architectural mosques, temples, and churches connecting diverse humanity, 16:9.',
  'season-01/ep-32-how-humans-keep-time': 'Historical evolution of timekeeping: ancient stone sundials and water clocks transitioning into intricate 17th-century mechanical escapement clocks and marine chronometers, human mastery of time, 16:9.',
  'season-01/ep-33-the-last-five-hundred-years': 'The Scientific Revolution: Galileo observing Jupiter moons with telescope, Newton prism refracting sunlight into rainbow spectrum, early steam engines and printed scientific volumes, 16:9.',
  'season-01/ep-34-after-1940-a-connected-world': 'The modern interconnected Earth: Apollo 8 Earthrise view combined with glowing fiber-optic oceanic cables, satellite constellations, and global data flows linking 8 billion humans, 16:9.',
  'season-01/ep-35-the-story-is-not-finished': 'The cosmic horizon ahead: a human silhouette standing on a high-tech observatory balcony gazing out at the vast expanding cosmic web and the open frontiers of the universe, sense of wonder and unbroken continuity, 16:9.',
};

function getSeasonEpisodes(seasonDir: string, seasonSlug: string): EpisodeMetadata[] {
  const epDir = path.join(seasonDir, 'episodes');
  if (!fs.existsSync(epDir)) return [];

  const files = fs.readdirSync(epDir)
    .filter((f) => f.endsWith('.md') && f !== 'README.md')
    .sort();

  const cfg = SEASONS_CONFIG[seasonSlug] || {
    title: seasonSlug,
    tagline: '',
    description: '',
    color: '#3b82f6',
    accent: '#60a5fa',
    icon: '📚',
  };

  const episodes: EpisodeMetadata[] = [];

  for (const filename of files) {
    const slug = filename.replace(/\.md$/, '');
    const filepath = path.join(epDir, filename);
    const raw = fs.readFileSync(filepath, 'utf-8');

    // Extract title
    const titleMatch = raw.match(/^#\s+(.+)$/m);
    const title = titleMatch ? titleMatch[1].trim() : slug;
    const cleanTitle = title.replace(/^Chapter\s+\d+:\s*/i, '');

    // Extract ep number
    const numMatch = slug.match(/ep-(\d+)/);
    const epNum = numMatch ? parseInt(numMatch[1], 10) : episodes.length + 1;

    // Extract Core Question
    const coreQMatch = raw.match(/\*\*Core Question:\*\*\s*(.+)$/m);
    const coreQuestion = coreQMatch ? coreQMatch[1].trim() : 'How did we get here?';

    // Extract Sequential Context
    const seqMatch = raw.match(/\*\*Sequential Context:\*\*\s*(.+)$/m);
    const sequentialContext = seqMatch ? seqMatch[1].trim() : '';

    // Extract Reference Documents
    const refMatch = raw.match(/\*\*Reference Documents:\*\*\s*(.+)$/m);
    const referenceDocs = refMatch ? refMatch[1].trim() : '';

    // Extract Deepens
    const deepensMatch = raw.match(/\*\*Deepens:\*\*\s*(.+)$/m);
    const deepens = deepensMatch ? deepensMatch[1].trim() : undefined;

    // Word count & reading minutes
    const wordCount = raw.split(/\s+/).filter(Boolean).length;
    const readingMinutes = Math.max(3, Math.ceil(wordCount / 220));

    // Check if an image exists in website/public/assets/images/episodes/
    const imageExtensions = ['.webp', '.png', '.jpg', '.jpeg'];
    let imageSrc: string | null = null;
    const imageBase = path.resolve('public', 'assets', 'images', 'episodes');
    
    for (const ext of imageExtensions) {
      const candidate = `${seasonSlug}-${slug}${ext}`;
      if (fs.existsSync(path.join(imageBase, candidate))) {
        imageSrc = `/assets/images/episodes/${candidate}`;
        break;
      }
    }

    // Curated prompt or generated default
    const promptKey = `${seasonSlug}/${slug}`;
    const imagePrompt = MASTER_PROMPTS[promptKey] || 
      `Cinematic documentary visualization of ${cleanTitle}: authentic scientific realism, National Geographic photography style, dramatic chiaroscuro cosmic lighting, 8k resolution, 16:9 widescreen composition.`;

    episodes.push({
      id: `${seasonSlug}/${slug}`,
      seasonNum: parseInt(seasonSlug.replace('season-0', '').replace('season-', ''), 10),
      seasonSlug,
      seasonTitle: cfg.title,
      seasonDescription: cfg.description,
      seasonBadge: `Season ${parseInt(seasonSlug.replace('season-0', '').replace('season-', ''), 10)}`,
      epNum,
      slug,
      title,
      cleanTitle,
      coreQuestion,
      sequentialContext,
      referenceDocs,
      deepens,
      raw,
      wordCount,
      readingMinutes,
      imagePrompt,
      imageSrc,
    });
  }

  // Hook up prev/next pointers within and across seasons
  return episodes;
}

export function getAllEpisodes(): EpisodeMetadata[] {
  const seasonsBase = path.resolve('..', 'seasons');
  const seasons = ['season-01', 'season-02', 'season-03', 'season-04'];
  let all: EpisodeMetadata[] = [];

  for (const s of seasons) {
    const sDir = path.join(seasonsBase, s);
    const eps = getSeasonEpisodes(sDir, s);
    all = all.concat(eps);
  }

  // Set prev and next links
  for (let i = 0; i < all.length; i++) {
    if (i > 0) {
      all[i].prevEpisode = {
        seasonSlug: all[i - 1].seasonSlug,
        slug: all[i - 1].slug,
        title: all[i - 1].title,
      };
    }
    if (i < all.length - 1) {
      all[i].nextEpisode = {
        seasonSlug: all[i + 1].seasonSlug,
        slug: all[i + 1].slug,
        title: all[i + 1].title,
      };
    }
  }

  return all;
}

export function getAllSeasons(): SeasonInfo[] {
  const all = getAllEpisodes();
  const seasons = ['season-01', 'season-02', 'season-03', 'season-04'];

  return seasons.map((slug) => {
    const cfg = SEASONS_CONFIG[slug];
    const eps = all.filter((e) => e.seasonSlug === slug);
    const sNum = parseInt(slug.replace('season-0', '').replace('season-', ''), 10);

    return {
      number: sNum,
      slug,
      title: cfg.title,
      tagline: cfg.tagline,
      description: cfg.description,
      color: cfg.color,
      accent: cfg.accent,
      icon: cfg.icon,
      episodeCount: eps.length,
      episodes: eps,
    };
  });
}

export function getSeason(slug: string): SeasonInfo | undefined {
  return getAllSeasons().find((s) => s.slug === slug);
}

export function getEpisode(seasonSlug: string, slug: string): EpisodeMetadata | undefined {
  return getAllEpisodes().find((e) => e.seasonSlug === seasonSlug && e.slug === slug);
}

export function getMasterTimelineRaw(): string {
  const p = path.resolve('..', 'timeline.md');
  return fs.existsSync(p) ? fs.readFileSync(p, 'utf-8') : '';
}

export function getGuideRaw(): string {
  const p = path.resolve('..', 'guide.md');
  return fs.existsSync(p) ? fs.readFileSync(p, 'utf-8') : '';
}

export function getContinuityRaw(): string {
  const p = path.resolve('..', 'continuity.md');
  return fs.existsSync(p) ? fs.readFileSync(p, 'utf-8') : '';
}
