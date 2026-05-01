$ cat /home/user/MisakiDate/quotes.py

import random

# type: "quote" | "story"
# tone: "warm" | "sharp" | "both"
# theme: "finishing" | "hard work" | "resilience" | "self-doubt" | "intellectual perseverance"

ITEMS = [

    # ── SHARP ───────────────────────────────────────────────────────────────
    {
        "type": "quote",
        "text": "A good dissertation is a done dissertation.",
        "author": "Every PhD supervisor, ever",
        "tone": "sharp",
        "theme": "finishing",
    },
    {
        "type": "quote",
        "text": "Inspiration is for amateurs. The rest of us just show up and get to work.",
        "author": "Chuck Close, painter",
        "tone": "sharp",
        "theme": "hard work",
    },
    {
        "type": "quote",
        "text": "The perfect is the enemy of the good. Submit the chapter.",
        "author": "Voltaire (adapted)",
        "tone": "sharp",
        "theme": "finishing",
    },
    {
        "type": "quote",
        "text": "You don't need motivation. You need discipline. Motivation is a feeling; discipline is a decision.",
        "author": "Jocko Willink",
        "tone": "sharp",
        "theme": "hard work",
    },
    {
        "type": "quote",
        "text": "If you're going through hell, keep going.",
        "author": "Winston Churchill",
        "tone": "sharp",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "Finish the work. The feelings come later.",
        "author": "Common writer's maxim",
        "tone": "sharp",
        "theme": "finishing",
    },
    {
        "type": "quote",
        "text": "Your manuscript is both good and original. Unfortunately, the parts that are good are not original, and the parts that are original are not good. Now go fix it.",
        "author": "Samuel Johnson (adapted)",
        "tone": "sharp",
        "theme": "intellectual perseverance",
    },
    {
        "type": "quote",
        "text": "It does not matter how slowly you go as long as you do not stop.",
        "author": "Confucius",
        "tone": "sharp",
        "theme": "hard work",
    },
    {
        "type": "quote",
        "text": "Stop waiting to feel ready. You won't. Start anyway.",
        "author": "Research folklore",
        "tone": "sharp",
        "theme": "finishing",
    },
    {
        "type": "quote",
        "text": "The dissertation is not your magnum opus. It is your union card. Write it, defend it, move on.",
        "author": "PhD program tradition",
        "tone": "sharp",
        "theme": "finishing",
    },
    {
        "type": "quote",
        "text": "Do the work. Especially when you don't want to. Especially then.",
        "author": "Steven Pressfield",
        "tone": "sharp",
        "theme": "hard work",
    },
    {
        "type": "quote",
        "text": "Every day that you don't write is a day you decided your research didn't matter.",
        "author": "Paul Silvia, How to Write a Lot",
        "tone": "sharp",
        "theme": "hard work",
    },

    # ── WARM ────────────────────────────────────────────────────────────────
    {
        "type": "quote",
        "text": "You are allowed to be both a work in progress and worthy of respect, right now, today.",
        "author": "Adapted from Sophia Bush",
        "tone": "warm",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "Not knowing the answer is not failure. Not knowing the answer is the beginning of research.",
        "author": "Research tradition",
        "tone": "warm",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "Between stimulus and response there is a space. In that space is your power to choose. Today, choose to keep going.",
        "author": "Viktor E. Frankl (adapted)",
        "tone": "warm",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "You don't have to be fearless. You just can't let the fear make your decisions for you.",
        "author": "Brené Brown",
        "tone": "warm",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "The fact that you are still here, still trying, still caring — that is not nothing. That is everything.",
        "author": "Anonymous",
        "tone": "warm",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "Confusion is not a sign that you are failing. It is a sign that you are thinking.",
        "author": "Research tradition",
        "tone": "warm",
        "theme": "intellectual perseverance",
    },
    {
        "type": "quote",
        "text": "The most courageous act is still to think for yourself. Aloud.",
        "author": "Coco Chanel",
        "tone": "warm",
        "theme": "intellectual perseverance",
    },
    {
        "type": "quote",
        "text": "You have been assigned this mountain so that you can show others it can be moved.",
        "author": "Mel Robbins",
        "tone": "warm",
        "theme": "resilience",
    },

    # ── BOTH (warm + sharp) ──────────────────────────────────────────────────
    {
        "type": "quote",
        "text": "Research is what I'm doing when I don't know what I'm doing. That feeling means you are in the right place.",
        "author": "Wernher von Braun (adapted)",
        "tone": "both",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "I am not afraid of storms, for I am learning how to sail my ship.",
        "author": "Louisa May Alcott",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "It always seems impossible until it's done.",
        "author": "Nelson Mandela",
        "tone": "both",
        "theme": "finishing",
    },
    {
        "type": "quote",
        "text": "The cure for impostor syndrome is finishing the work. You cannot argue with a submitted thesis.",
        "author": "Academic tradition",
        "tone": "both",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "Hard work beats talent when talent doesn't work hard. In research, hard thinking beats brilliance when brilliance stops showing up.",
        "author": "Tim Notke (adapted)",
        "tone": "both",
        "theme": "hard work",
    },
    {
        "type": "quote",
        "text": "You don't rise to the level of your goals. You fall to the level of your systems. Build the system.",
        "author": "James Clear, Atomic Habits",
        "tone": "both",
        "theme": "hard work",
    },

    # ── REAL-LIFE STORIES ────────────────────────────────────────────────────
    {
        "type": "story",
        "text": (
            "Katalin Karikó spent decades working on mRNA at the University of Pennsylvania. "
            "She was demoted, lost her funding, and colleagues told her to abandon the idea. "
            "She kept working anyway — in a smaller office, with fewer resources. "
            "In 2023, her work became the foundation of the COVID-19 vaccines that saved millions of lives, "
            "and she won the Nobel Prize in Medicine. The work was always right. The world just wasn't ready yet."
        ),
        "author": "Katalin Karikó, Nobel Laureate",
        "tone": "both",
        "theme": "intellectual perseverance",
    },
    {
        "type": "story",
        "text": (
            "Richard Feynman hit a creative wall in the late 1940s. Burnt out and doubting his ability, "
            "he made a decision: he would play with physics purely for pleasure, with no pressure to produce. "
            "He watched a plate wobble in the air at Cornell's cafeteria and started calculating its spin — just because it was fun. "
            "That playful calculation led directly to the work that won him the Nobel Prize. "
            "Permission to play is not a distraction from serious work. Sometimes it is the work."
        ),
        "author": "Richard Feynman, Nobel Laureate in Physics",
        "tone": "warm",
        "theme": "intellectual perseverance",
    },
    {
        "type": "story",
        "text": (
            "Darwin had the core idea for natural selection in 1838. He did not publish it for 20 years. "
            "He was terrified of being wrong, of the controversy, of what it would mean. "
            "He kept refining, kept doubting, kept going back to his notebooks. "
            "When he finally published in 1859 — only because a rival was about to — it changed everything. "
            "The self-doubt did not stop the work. The work outlasted the self-doubt."
        ),
        "author": "Charles Darwin, On the Origin of Species",
        "tone": "both",
        "theme": "self-doubt",
    },
    {
        "type": "story",
        "text": (
            "Barbara McClintock's work on genetic transposition was so far ahead of its time "
            "that the scientific community largely ignored her for thirty years. "
            "She kept doing the research anyway — methodically, rigorously, alone in her lab. "
            "In 1983, at age 81, she was awarded the Nobel Prize in Physiology or Medicine. "
            "She said she never stopped because the corn told her things no one else was listening for yet. "
            "Stay curious. The field catches up."
        ),
        "author": "Barbara McClintock, Nobel Laureate",
        "tone": "warm",
        "theme": "intellectual perseverance",
    },
    {
        "type": "story",
        "text": (
            "Kazuo Ishiguro wrote The Remains of the Day in four weeks. "
            "He and his wife called it 'the Crash' — he wrote from 9am to 10:30pm every day, "
            "no visitors, no phone calls, rough drafts only, no going back. "
            "The goal was simple: get the whole thing out, imperfect and alive, before the internal critic arrived. "
            "It won the Booker Prize. Sometimes the way through is to stop being careful and just finish."
        ),
        "author": "Kazuo Ishiguro, Nobel Laureate in Literature",
        "tone": "sharp",
        "theme": "finishing",
    },
    {
        "type": "story",
        "text": (
            "George Orwell wrote Nineteen Eighty-Four while dying of tuberculosis on the remote Scottish island of Jura. "
            "He was too ill to be moved to hospital. He typed in bed, feverish, knowing he might not survive to see it published. "
            "He finished it. He died seven months after it came out. "
            "The conditions were never going to be right. He wrote it anyway."
        ),
        "author": "George Orwell, 1984",
        "tone": "sharp",
        "theme": "hard work",
    },
    {
        "type": "story",
        "text": (
            "Viktor Frankl survived three years in Nazi concentration camps — including Auschwitz. "
            "His wife, parents, and brother were killed. His manuscript was destroyed. "
            "After liberation, he rewrote Man's Search for Meaning in nine days. "
            "He said the act of writing was itself an act of meaning-making — "
            "proof that something survives even when everything is taken. "
            "You still have the thinking. You still have the work."
        ),
        "author": "Viktor E. Frankl, psychiatrist and Holocaust survivor",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Marie Curie was not allowed to attend university in Poland because she was a woman. "
            "She worked as a governess for years, sending money to fund her sister's education in Paris, "
            "with an agreement that her sister would do the same for her later. "
            "She eventually got to Paris, earned degrees in both physics and mathematics, "
            "and became the first person — man or woman — to win two Nobel Prizes in two different sciences. "
            "The barriers were real. She moved through them one year at a time."
        ),
        "author": "Marie Curie, two-time Nobel Laureate",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Toni Morrison wrote Beloved while working full-time as an editor at Random House and raising two children alone. "
            "She wrote before dawn, before her sons woke up, before the day took everything. "
            "She said she had to learn to write in stolen hours, which meant she could never wait for the right mood. "
            "The mood had to be irrelevant. Beloved won the Pulitzer Prize and the Nobel. "
            "The hours were small. The work was not."
        ),
        "author": "Toni Morrison, Nobel Laureate in Literature",
        "tone": "sharp",
        "theme": "hard work",
    },
    {
        "type": "story",
        "text": (
            "Andrew Wiles spent seven years in secret trying to prove Fermat's Last Theorem — "
            "a problem that had defeated mathematicians for 358 years. "
            "When he finally announced a proof, a flaw was found. Most people would have stopped. "
            "He went back in, alone, for another year. He fixed it. "
            "He later said: 'There is no shortcut. You just have to go into the room and think.' "
            "The room is your desk. Go sit in it."
        ),
        "author": "Andrew Wiles, mathematician",
        "tone": "both",
        "theme": "intellectual perseverance",
    },
    {
        "type": "story",
        "text": (
            "Barbara Tuchman had no PhD, no academic post, no institutional backing. "
            "She researched and wrote history from her home, driven purely by the need to understand. "
            "Her book The Guns of August won the Pulitzer Prize and was read by JFK during the Cuban Missile Crisis. "
            "She proved that the credential is not the work, and the institution is not the standard. "
            "The standard is the thinking."
        ),
        "author": "Barbara Tuchman, two-time Pulitzer Prize winner",
        "tone": "both",
        "theme": "intellectual perseverance",
    },
]


def get_random_item() -> dict:
    return random.choice(ITEMS)


def get_item_by_tone(tone: str) -> dict:
    filtered = [i for i in ITEMS if i["tone"] in (tone, "both")]
    return random.choice(filtered) if filtered else get_random_item()


def get_item_by_theme(theme: str) -> dict:
    filtered = [i for i in ITEMS if i["theme"] == theme]
    return random.choice(filtered) if filtered else get_random_item()
