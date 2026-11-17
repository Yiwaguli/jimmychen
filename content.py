"""All the words and picture choices for the site live in this file.

After editing, run:  python3 build.py

Block types used in each work's "blocks" list
  img(name, alt, cap=None)          one picture (files live in assets/works/<slug>/<name>.jpg)
  {"t": "image", "img": img(...), "pos": "full" | "right" | "left" | "center", "text": [...]}
  {"t": "split", "img": img(...), "text": [...], "flip": False, "ratio": (62, 38)}
  {"t": "row", "imgs": [img(...), ...], "tight": False}
  {"t": "text", "text": [...], "pos": "inset" | "center"}
  {"t": "videos", "items": [(youtube_id, caption), ...]}
"""


def img(name, alt, cap=None):
    return {"name": name, "alt": alt, "cap": cap}


SITE = {
    "name": "Jimmy Chen",
    "description": "Jimmy Chen is an artist and PhD researcher at the Creative Computing Institute, "
    "University of the Arts London, working across posthumanism, queer theory and multi-sensory HCI.",
    "url": "https://yiwaguli.github.io/jimmychen/",
    "nav": [("Works", ""), ("About", "about/"), ("CV", "cv/"), ("Contact", "contact/")],
}

ABOUT = {
    "lede": "Jimmy Chen is an artist and PhD researcher at the Creative Computing Institute, "
    "University of the Arts London, working across posthumanism, queer theory and multi-sensory HCI.",
    "text": [
        "His practice moves between film, speculative worldbuilding, virtual reality, 3D prototyping, "
        "scent, sound and live performance. Across these media it keeps returning to the senses that "
        "screens tend to leave out: smell, taste, touch and the felt weight of things. Earlier works "
        "used food, pheromones and edible objects to imagine how bodies might communicate beyond words. "
        "More recent work turns towards fungi, robotics and contemporary ritual.",
        "His doctoral research, &lsquo;Queering with Fungi&rsquo;, explores multispecies relations through "
        "auto-ethnography and critical biodata interaction. Through embodied and non-representational "
        "methodologies, his practice challenges normative paradigms, disrupting extractivist "
        "technologies and advocating for radical reattunement.",
        "His work has been selected for Ars Electronica (2026) and Being Human Festival (2026), and "
        "presented at several academic conferences. He holds an MA in Digital Direction from the Royal "
        "College of Art and teaches as an Associate Lecturer at the Creative Computing Institute.",
    ],
}

CONTACT = {
    "lede": "For exhibitions, performances, collaborations and research conversations, please get in touch.",
    "rows": [
        ("Email", '<a href="mailto:cjm990603@gmail.com">cjm990603@gmail.com</a>'),
        ("Instagram", '<a href="https://www.instagram.com/yiwaguli/" rel="noopener me">@yiwaguli</a>'),
    ],
}

# Each section: (heading, [(year, entry), ...]). Leave the year empty ("") when it is not known.
CV = [
    (
        "Education",
        [
            ("Current", "PhD, Creative Computing Institute, University of the Arts London<br>"
                        "<em>Queering with Fungi: Myceliating queer kinship and belonging through non-representational sensing</em>"),
            ("2022&ndash;2023", "MA Digital Direction, Royal College of Art, London"),
            ("", "Undergraduate degree in Economics, Hangzhou Normal University"),
        ],
    ),
    (
        "Teaching",
        [
            ("2026&ndash;", "Associate Lecturer, Creative Computing Institute, University of the Arts London<br>"
                            "BSc (Hons) Computer Science: Research, Knowledge Exchange and Enterprise unit"),
            ("2021&ndash;2023", "Assistant Tutor, Rosso Arts &amp; Design Education Institution, Hangzhou"),
        ],
    ),
    (
        "Exhibitions and performances",
        [
            ("2026", '<a href="../works/ritual-robotics-the-fungal-act-01/"><em>Ritual Robotics: The Fungal Act 01</em></a>, '
                     "Being Human Festival, Lethaby Gallery, London"),
            ("2026", '<a href="../works/ritual-robotics-act-01/"><em>Ritual Robotics: Act 01</em></a>, Ars Electronica, Linz'),
        ],
    ),
    (
        "Talks, conferences and workshops",
        [
            ("2026", "&lsquo;Queering with Fungi: Myceliating Queer Kinship and Belonging through Multisensory Immersion&rsquo;, "
                     "<em>No Future? Hopeful Worldings in Haunted Times</em>, ASLE-UKI Postgraduate Conference, University of Chichester"),
            ("", "&lsquo;Queering with Fungi&rsquo;, UAL Summer Symposium, University of the Arts London"),
            ("2025", "Visiting Research Panelist, graduate conference, Mahindra Humanities Center, Harvard University"),
            ("", "Contributor and facilitator, <em>Rethinking Anthropocentrism: New Technologies and More-than-Human Sensing</em>, workshop, Leiden"),
        ],
    ),
    (
        "Selected works",
        [
            ("2026", '<a href="../works/ritual-robotics-the-fungal-act-01/"><em>Ritual Robotics: The Fungal Act 01</em></a>, performance'),
            ("2026", '<a href="../works/ritual-robotics-act-01/"><em>Ritual Robotics: Act 01</em></a>, participatory performance, with Joseph Whitmore'),
            ("2023", '<a href="../works/journey-to-the-reishi/"><em>Journey to the Reishi</em></a>, multisensory VR'),
            ("2023", '<a href="../works/armpit-kingdom/"><em>Armpit Kingdom</em></a>, multisensory VR and immersive exhibition, with Jing Sun and Shihui Liu'),
            ("2022", '<a href="../works/ann/"><em>Ann</em></a>, short film'),
            ("2021", '<a href="../works/delicious-me/"><em>Delicious Me</em></a>, 3D prototyping and photography'),
            ("2020", '<a href="../works/schrodingers-cake/"><em>Schr&ouml;dinger&rsquo;s Cake</em></a>, short film'),
        ],
    ),
    (
        "Other experience",
        [
            ("", "Perfumery Consultant, John Lewis &amp; Partners"),
        ],
    ),
]

WORKS = [
    # ------------------------------------------------------------------
    {
        "slug": "ritual-robotics-the-fungal-act-01",
        "title": "Ritual Robotics: The Fungal Act 01",
        "year": "2026",
        "medium": "Performance, digital puppetry, creative robotics",
        "where": "Lethaby Gallery, 6 November 2026, as part of the Being Human Festival",
        "summary": "A performance of foraging and cultivation, in which sensor gloves turn the movement of two bodies into sound.",
        "cover": img("cover", "Two performers in pale robes crouch over a bed of dried leaves on a gallery floor, beneath a projection reading Ritual Robotics: The Fungal Act 01."),
        "blocks": [
            {"t": "image", "pos": "full", "img": img("cover", "Two performers in pale robes and black gloves crouch over a bed of dried leaves on a gallery floor, beneath a large projection reading Ritual Robotics: The Fungal Act 01.")},
            {"t": "text", "pos": "inset", "text": [
                "<em>The Fungal Act 01</em> is an alternative version of <a href=\"../ritual-robotics-act-01/\"><em>Ritual Robotics: Act 01</em></a>, first performed at Ars Electronica in 2026. Here the ritual turns towards fungi, following Jimmy&rsquo;s pursuit of a more-than-human embodiment made in collaboration with them.",
                "The script opens with the movements of mushroom foraging. The performers wear sensor gloves that stream the rotation and acceleration of their hands to Ableton Live, where the data becomes sound. That sound in turn shapes how the performers move.",
            ]},
            {"t": "row", "imgs": [
                img("mask", "A masked performer raises both gloved hands in front of a projection of hands breaking apart mushroom substrate."),
                img("costume-open", "A performer holds a robe open towards a seated audience, its inside covered with drawings and patches."),
            ]},
            {"t": "videos", "items": [("4Edu4XOB7yY", None)]},
            {"t": "split", "flip": True, "ratio": (46, 54), "img": img("kneeling", "Two performers kneel close together in their robes, seen from behind, with leaves scattered on the floor."), "text": [
                "The second stage of the act is cultivation. Mushroom substrate is prepared and divided by the performers on stage, and the glass containers become a new site for the mushrooms to grow, afterwards, in Jimmy&rsquo;s home.",
                "The piece is an attempt to bring contemporary ritual, digital technology, robotics and the more-than-human together in one narrative performance. It stages a negotiation between digital technology and more-than-human embodiment.",
            ]},
            {"t": "row", "imgs": [
                img("costume", "A performer in a half mask stands with arms outstretched, showing the full width of a pale hand-made robe.", "Costume"),
                img("audience", "Seen from behind the audience, a performer raises a fist in front of the projected title of the performance.", "Lethaby Gallery, 6 November 2026"),
            ]},
            {"t": "videos", "items": [("_CI4yj54wxo", None), ("m45L8IzswLE", None)]},
        ],
        "credits": [
            ("Performers", "Jimmy Chen, Luke Taylor"),
            ("Sensor gloves", "Jimmy Chen, Ruiyang Wang, Joseph Whitmore"),
            ("Costume and sound", "Jimmy Chen"),
            ("Photography", "Jamie Pazmino"),
        ],
        "links": [
            ("Being Human Festival 2026: Being More-Than-Human, Fictions and Frictions", "https://www.eventbrite.co.uk/e/being-more-than-human-fictions-frictions-tickets-2003773587741?aff=odcleoeventsincollection"),
            ("Photographs on Instagram", "https://www.instagram.com/p/DfnHn4IEaMd/?img_index=1"),
        ],
    },
    # ------------------------------------------------------------------
    {
        "slug": "ritual-robotics-act-01",
        "title": "Ritual Robotics: Act 01",
        "year": "2026",
        "medium": "Stage and performance design, digital puppetry, creative robotics",
        "where": "Ars Electronica 2026, Linz",
        "summary": "A participatory ritual on a labyrinth, where folk tradition meets digital puppetry and robotics.",
        "cover": img("cover", "Three performers in white overalls and hand-made masks raise objects built from festival waste, on a pink stage in a city square."),
        "blocks": [
            {"t": "split", "ratio": (50, 50), "img": img("cover", "Three performers in white overalls and hand-made masks raise objects built from festival waste, on a pink stage in a city square."), "text": [
                "<em>Ritual Robotics: Act 01</em> stages a participatory contemporary ritual in which folk tradition meets digital puppetry and robotics. It resists a future where digital technology isolates people rather than connecting them, and works instead to deepen communal practice for change.",
                "The ritual takes place on a single labyrinth. Each audience member receives a performing object built from festival waste, and together they wind from the centre of the labyrinth outward and back again. A guided sequence leads the way at first. After that, the group continues through intuition, movement and digital technology.",
            ]},
            {"t": "row", "imgs": [
                img("labyrinth-wide", "Performers in white overalls move across a pink floor marked with the white lines of a labyrinth."),
                img("labyrinth", "Three masked performers spread out across the labyrinth, with a bundle of twigs lying at its centre."),
            ]},
            {"t": "videos", "items": [("9qak9KlIISI", None)]},
            {"t": "row", "imgs": [
                img("exchange", "Two masked performers face each other and pass an object between their hands."),
                img("duet", "Two performers circle each other on the labyrinth, one holding a puppet-like object."),
                img("audience", "The performance seen from the audience, with the crowd seated around the pink stage.", "Ars Electronica 2026, Linz"),
            ]},
            {"t": "videos", "items": [("AYMcpO0_U1Q", None)]},
        ],
        "credits": [
            ("Co-lead artists", "Joseph Whitmore, Jimmy Chen"),
            ("Choreographic collaborator and performer", "Diana Alina Serbanescu"),
            ("Creative technologist", "Ruiyang Wang"),
        ],
        "links": [
            ("Ritual Robotics at Ars Electronica", "https://ars.electronica.art/negotiatinghumanity/en/view/ritual-robotics-38e38ddb450c8138ab85e255de82b1bb/"),
        ],
    },
    # ------------------------------------------------------------------
    {
        "slug": "journey-to-the-reishi",
        "title": "Journey to the Reishi",
        "year": "2023",
        "medium": "Multisensory VR, game",
        "where": None,
        "summary": "A multisensory VR journey that carries the spirit of a Reishi mushroom back to the forest it came from.",
        "cover": img("cover", "A forest path rendered as a cloud of points, glowing green where light falls through the trees."),
        "blocks": [
            {"t": "image", "pos": "full", "img": img("cover", "A forest path rendered as a cloud of coloured points, glowing green where light falls through the dark trees.")},
            {"t": "text", "pos": "inset", "text": [
                "<em>Journey to the Reishi</em> investigates how Eastern medical culture and Western science might coexist, by taking seriously an animistic interpretation of how Reishi is used. It draws on the Hmong practice of guiding souls back to their origin, and connects that practice to the traditional use of Reishi. In this reading, the perceived decline in the mushroom&rsquo;s efficacy may come from the entrapment of its soul.",
                "The study follows Anna Tsing&rsquo;s <em>The Mushroom at the End of the World</em> (2015) in attending to how the Western scientific paradigm has influenced and controlled Eastern indigenous cultures and beliefs. From an animistic perspective, cultivated Reishi might regain its medicinal properties once it is returned to its place of origin.",
            ]},
            {"t": "row", "imgs": [
                img("reishi-1", "Several dark, lacquered Reishi mushrooms on a metal tray."),
                img("reishi-2", "Close view of a Reishi mushroom, its cut stem showing a pale interior.", "Locally sourced Reishi"),
            ]},
            {"t": "split", "ratio": (58, 42), "img": img("reishi-pot", "A glazed clay medicine pot with a large Reishi resting in its mouth, beside a small dish of sliced Reishi."), "text": [
                "The research began with the mushroom itself: growing Reishi from a kit, sourcing local Reishi and its extract, and learning its taste and smell.",
                "Photogrammetry then became a metaphor for spirit generation. The Reishi was scanned and visualised as a point cloud, a body made of light. A forest was scanned in the same way, and transformed into the origin that the spirit travels back to.",
            ]},
            {"t": "row", "imgs": [
                img("forest-scanning", "A hand holds a phone that is scanning fallen logs on a forest floor.", "Scanning the forest"),
                img("vr-scene-1", "A giant Reishi made of golden points rises among point-cloud trees in the VR scene.", "The spirit of the Reishi in VR"),
            ]},
            {"t": "image", "pos": "full", "img": img("vr-scene-2", "A Reishi mushroom made of glowing points stands like a tree in a dark red landscape, with a controller beam pointing towards it.")},
            {"t": "text", "pos": "inset", "text": [
                "The work unfolds in three steps. Visitors first taste and smell locally sourced Reishi, as a prelude to the journey. They then feel the spirit of the Reishi and the weight of its ever-changing form. Finally they put on a headset and accompany the spirit home, on a VR journey led by an unreliable narrator.",
            ]},
            {"t": "row", "imgs": [
                img("tasting", "A dropper adds Reishi extract to a glass of water, next to a dish of sliced Reishi.", "Step 1. Interact with the Reishi"),
                img("spirit-hand", "A hand hovers beneath a screen showing the Reishi as a drifting cloud of points.", "Step 2. Feel the spirit of Reishi"),
                img("vr-visitor", "A visitor wearing a VR headset holds a Reishi mushroom in both hands.", "Step 3. Journey to the Reishi"),
            ]},
            {"t": "image", "pos": "full", "img": img("setup-wide", "The installation on a wooden desk: two screens, a VR headset, a clay pot of Reishi, a dish and a glass.")},
            {"t": "row", "tight": True, "imgs": [
                img("setup", "The two screens and VR headset of the installation, seen from the side."),
                img("pot-desk", "The clay pot and dish of Reishi on the desk, lit warmly, with the screens behind."),
            ]},
            {"t": "row", "imgs": [
                img("exhibition-1", "A visitor in a white jacket wears the headset in front of a screen showing the point-cloud Reishi."),
                img("exhibition-2", "A visitor wears the headset beside a screen showing the scanned forest.", "Exhibition"),
            ]},
            {"t": "videos", "items": [("WC7AlOk8E98", None)]},
        ],
        "credits": [("Artist", "Jimmy Chen")],
        "links": [],
    },
    # ------------------------------------------------------------------
    {
        "slug": "armpit-kingdom",
        "title": "Armpit Kingdom",
        "year": "2023",
        "medium": "Multisensory VR, worldbuilding, immersive exhibition",
        "where": None,
        "summary": "An imagined society in which human pheromones reshape how people communicate, date and desire.",
        "cover": img("cover", "Poster for Aroma, the host club of Armpit Kingdom: four computer-generated hosts pose with their arms raised."),
        "blocks": [
            {"t": "image", "pos": "full", "img": img("cover", "Poster for Aroma, the host club of Armpit Kingdom: four computer-generated hosts pose with their arms raised against a dark red ground, with the words Smell, Love, Born.")},
            {"t": "text", "pos": "inset", "text": [
                "<em>Armpit Kingdom</em> explores the possibility of using human pheromones as chemosensory signals to communicate and interact, drawing on the long-standing use of pheromones by animals to coexist with nature. It imagines a society in which communication is revolutionised by the scientific discovery and application of human pheromones. We call this world Armpit Kingdom.",
                "In this fictional society, pheromones, closely linked to the chemical signals of armpit odour, are celebrated as vital to social interaction, including intimacy. Traditional concepts of gender and sexual orientation are abandoned, and people embrace their olfactory instincts to form new ways of being.",
            ]},
            {"t": "row", "keep": True, "imgs": [
                img("poster-asuka", "Character poster for Asuka, ranked number two at Aroma."),
                img("poster-keity", "Character poster for Keity, ranked number four at Aroma."),
                img("poster-rei", "Character poster for Rei, ranked number three at Aroma."),
                img("poster-taku", "Character poster for Taku, a host at Aroma.", "The hosts of Aroma Club"),
            ]},
            {"t": "split", "flip": True, "ratio": (60, 40), "img": img("smell-sample-1", "Hands cut the underarm section out of a white T-shirt with scissors.", "Collecting smell samples from worn clothing"), "text": [
                "Intimacy in Armpit Kingdom takes its cue from Japanese host club culture. The project envisions a virtual dating experience at Aroma Club, where visitors step away from visually driven social norms and choose with their noses.",
                "Smell samples were collected from worn clothing and presented in dishes beneath the poster of each host, so that every character in the virtual club could also be met as a scent.",
            ]},
            {"t": "row", "imgs": [
                img("smell-sample-2", "Printed character posters above four dishes of fabric samples labelled with the hosts' names."),
                img("smell-sample-3", "Three dishes labelled Asuka, Taku and Rei, each paired with a dish of fabric.", "Smell samples paired with each host"),
            ]},
            {"t": "row", "imgs": [
                img("animation-swab", "3D animation: a swab is held to the armpit of a computer-generated body."),
                img("animation-beaker", "3D animation: a swab is stirred in a beaker on a tiled surface.", "Concept product animation"),
            ]},
            {"t": "row", "imgs": [
                img("vr-scene-1", "The VR environment: a traditional Japanese courtyard at night, lit from within."),
                img("vr-scene-2", "The VR environment: an interior of sliding screens opening onto a lit room.", "Aroma Club in VR"),
            ]},
            {"t": "split", "ratio": (60, 40), "img": img("vr-testing", "A man wearing a VR headset tests the environment at a desk with a laptop.", "Testing the VR environment"), "text": [
                "Through this immersive experience the study critically examines the role of scent in modern society and its ties to consumerism and gender bias. It imagines the kind of society that might emerge if we embraced our olfactory instincts without the influence of normative social values.",
            ]},
            {"t": "row", "imgs": [
                img("exhibition-1", "A visitor points at a large screen showing a swab held to a virtual armpit."),
                img("exhibition-2", "Two visitors stand at screens in a darkened exhibition room."),
            ]},
            {"t": "row", "tight": True, "imgs": [
                img("exhibition-4", "A visitor stands in front of a large screen facing one of the virtual hosts."),
                img("exhibition-5", "The exhibition room, with screens, tablets and a small lamp on a table of posters.", "Exhibition"),
            ]},
            {"t": "videos", "items": [("c9TR2-P6ZjY", None)]},
        ],
        "credits": [
            ("Artists", "Jimmy Chen, Jing Sun, Shihui Liu"),
            ("VR environment and interaction design", "Jimmy Chen"),
            ("Animation", "Jing Sun"),
            ("Graphic design", "Shihui Liu"),
        ],
        "links": [],
    },
    # ------------------------------------------------------------------
    {
        "slug": "ann",
        "title": "Ann",
        "year": "2022",
        "medium": "Short film, speculative worldbuilding",
        "where": None,
        "summary": "A mother seeks forgiveness from her deceased daughter by sharing a meal across the real and digital worlds.",
        "cover": img("cover", "Film still: a woman in black stands with her head bowed beneath a wall lamp, beside a vase of yellow tulips."),
        "blocks": [
            {"t": "image", "pos": "full", "img": img("cover", "Film still: a woman in black stands with her head bowed beneath a glowing wall lamp, beside a vase of yellow tulips.")},
            {"t": "text", "pos": "inset", "text": [
                "<em>Ann</em> is the story of a mother seeking forgiveness from her deceased daughter through food.",
                "The film belongs to the TeleFood project, which explores food as a medium for connecting the real and digital worlds. It is set in a world where a big-tech Eastern company, The TeleFood Company, can upload the consciousness of a deceased person into the digital world. The living and the uploaded can then communicate without words, through the shared experience of food.",
            ]},
            {"t": "row", "imgs": [
                img("still-supermarket", "Film still: the mother reads a packet of meat in a supermarket aisle."),
                img("still-walking", "Film still: the mother walks along a city pavement beside a busy road."),
                img("still-home", "Film still: the mother enters a front door with a bag of shopping and flowers.", "Buying food and mourning for the daughter"),
            ]},
            {"t": "row", "tight": True, "imgs": [
                img("still-table-empty", "Film still: an empty glass jar on a table set with a patterned cloth."),
                img("still-tulips", "Film still: yellow tulips in a vase on the dining table."),
                img("still-incense", "Film still: a stick of incense burns in a bowl beside an empty rice bowl."),
            ]},
            {"t": "text", "pos": "inset", "text": [
                "Food is a strong medium of communication, even where the virtual and the real intertwine. The project looks at the role of food in Eastern ritual culture, where a dish can carry a ritual, an apology or a blessing, and it argues that future forms of communication may become personalised and multisensory rather than verbal or visual alone.",
            ]},
            {"t": "row", "imgs": [
                img("still-cooking", "Film still: hands cut pork into cubes on a red chopping board."),
                img("still-device", "Film still: the mother sits at the table and examines a white headset."),
                img("still-headset", "Film still: the mother seen from behind, wearing the white headset.", "Preparing food and communicating with the daughter"),
            ]},
            {"t": "image", "pos": "full", "img": img("still-sorry", "Film still: the mother in profile wearing the headset in a dark room, with the subtitle I am really sorry.")},
            {"t": "row", "imgs": [
                img("still-eating", "Film still: the mother eats alone at the table, wearing the headset."),
                img("still-remove", "Film still: the mother lifts the headset from her head."),
                img("still-photo", "Film still: photographs and flowers on a round table by a window."),
            ]},
            {"t": "row", "imgs": [
                img("brainwave", "A woman wearing an electrode headband looks at a 3D printer.", "Inspiration: brainwave sensing"),
                img("storyboard-1", "First page of the hand-drawn storyboard for Ann."),
                img("storyboard-2", "Second page of the hand-drawn storyboard for Ann.", "Storyboard"),
            ]},
            {"t": "videos", "items": [("49Jf-gLLp9Q", None)]},
        ],
        "credits": [
            ("Main artist and film director", "Jimmy Chen"),
            ("Actor", "Sheyl"),
            ("Camera", "Harry and Yun"),
        ],
        "links": [],
    },
    # ------------------------------------------------------------------
    {
        "slug": "delicious-me",
        "title": "Delicious Me",
        "year": "2021",
        "medium": "3D prototyping, photography",
        "where": None,
        "summary": "Edible sex toys that tie the human desire for meat to the desire for sex.",
        "cover": img("cover", "A figure in a pink bull mask and lab coat stands beneath four pink objects hanging from a white rail, against a pink wall."),
        "blocks": [
            {"t": "image", "pos": "full", "img": img("cover", "A figure in a pink bull mask and lab coat stands beneath four pink 3D-printed objects hanging from a white rail, against a pink wall.")},
            {"t": "text", "pos": "inset", "text": [
                "Based on the subtle connection between vorarephilia and carnism, <em>Delicious Me</em> links the human desire for meat to the desire for sex. It explores the paradox of carnivorous human nature through a set of edible sex toys.",
                "The project starts from furry fandom culture and from vorarephilia, a sexual fetish of swallowing or being swallowed. The design of meat, that is, of animals, is projected onto edible sex toys: a horn for the bull, a tail for the pig, a comb and an egg for the chicken, a foetus for the human.",
            ]},
            {"t": "image", "pos": "full", "img": img("concept", "Diagram: a human body, four species (bull, pig, chicken, human) and their matching sex toys, followed by the swallowing system in which a body swallows a toy and evolves into the species.", "Characters, sex toys and the swallowing system")},
            {"t": "text", "pos": "inset", "text": [
                "By swallowing the sex toy of a different species, you evolve into that species. The system proposes a relationship between humans and nature: as we swallow nature, nature swallows us.",
            ]},
            {"t": "row", "imgs": [
                img("picking-1", "A man in a lab coat reaches for a ring-shaped toy hanging from the rail."),
                img("picking-2", "The man holds up a studded toy and inspects it.", "Picking"),
            ]},
            {"t": "row", "imgs": [
                img("picking-3", "The man tilts his head back and lowers the studded toy towards his open mouth."),
                img("swallowing", "Close view of an open mouth about to take in the pink studded toy.", "Swallowing"),
            ]},
            {"t": "row", "imgs": [
                img("evolving", "A bare-chested figure wearing the bull mask, facing the camera.", "Evolving"),
                img("replacing-1", "Close view of a hand holding a curved pink toy against a bare stomach."),
                img("replacing-2", "The masked figure offers the curved toy in both open hands.", "Replacing"),
            ]},
        ],
        "credits": [("Main artist and photographer", "Jimmy Chen")],
        "links": [],
    },
    # ------------------------------------------------------------------
    {
        "slug": "schrodingers-cake",
        "title": "Schr&ouml;dinger&rsquo;s Cake",
        "plain_title": "Schrödinger’s Cake",
        "year": "2020",
        "medium": "Short film",
        "where": None,
        "summary": "An experimental short film with several endings, about a cake its protagonist is destined not to eat.",
        "cover": img("cover", "Film still: a white cake topped with fruit, a jug of milk and a fork on a white table."),
        "blocks": [
            {"t": "image", "pos": "full", "img": img("title", "Film still: a young woman sits behind a small white cake and a glass of milk, under the title A Thought Experiment About Destiny.")},
            {"t": "text", "pos": "inset", "text": [
                "<em>Schr&ouml;dinger&rsquo;s Cake</em> starts from the uncertainty principle in quantum physics. It takes the observer effect, in which the act of observing a system changes it, and places it in an everyday, macroscopic setting. The result is a thought experiment about fate seen from the position of the observer, and a way of discussing fate through science.",
                "The outcome is an experimental short film with multiple endings. It tells the story of whether its protagonist can eat a cake that she is destined not to eat.",
            ]},
            {"t": "row", "imgs": [
                img("cover", "Film still: a white cake topped with fruit, a jug of milk and a fork on a white table."),
                img("cake-split", "Film still, split screen: the untouched cake on the left, the protagonist eating it on the right."),
            ]},
            {"t": "row", "tight": True, "imgs": [
                img("sleep-1", "Film still, split screen: the protagonist asleep in bed in two different positions."),
                img("sleep-2", "Film still, split screen: a figure hidden under the duvet on the left, an empty bed on the right."),
            ]},
            {"t": "text", "pos": "inset", "text": [
                "Fatalism and its opposite are views of fate particular to human society, and most discussion of destiny rests on theology or metaphysics, from traditional Chinese fortune-telling to Western tarot. The film approaches the same subject through scientific theory instead, to see whether the conclusions change, and whether people&rsquo;s views on fate change with them.",
            ]},
            {"t": "row", "imgs": [
                img("observer", "Film still: a leopard gecko enters the frame beside the word Observer."),
                img("interference", "Film still: close view of the gecko's eye above the caption Interference begins.", "The observer"),
            ]},
            {"t": "row", "tight": True, "imgs": [
                img("gecko-milk", "Film still: the gecko beside a glass of milk."),
                img("gecko-fork", "Film still: the gecko lying across a black fork."),
                img("gecko-phone", "Film still: the gecko climbing over a phone."),
            ]},
            {"t": "videos", "items": [("qrJLIYijNL0", None)]},
        ],
        "credits": [
            ("Artist and director", "Jimmy Chen"),
            ("Performer", "Can Lin"),
        ],
        "links": [],
    },
]
