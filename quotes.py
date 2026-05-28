import random

# type: "quote" | "story"
# tone: "warm" | "sharp" | "both"
# theme: "finishing" | "hard work" | "resilience" | "self-doubt" |
#         "intellectual perseverance" | "creativity" | "courage" |
#         "consistency" | "rest & recovery" | "purpose"

ITEMS = [

    # ── SHARP QUOTES ────────────────────────────────────────────────────────
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
    {
        "type": "quote",
        "text": "Someone busier than you is running right now.",
        "author": "Running community saying",
        "tone": "sharp",
        "theme": "consistency",
    },
    {
        "type": "quote",
        "text": "You have exactly the same number of hours in a day as everyone who has ever achieved something extraordinary.",
        "author": "Common maxim",
        "tone": "sharp",
        "theme": "hard work",
    },
    {
        "type": "quote",
        "text": "Don't wish it were easier. Wish you were better.",
        "author": "Jim Rohn",
        "tone": "sharp",
        "theme": "hard work",
    },
    {
        "type": "quote",
        "text": "Complaining about a problem without proposing a solution is called whining.",
        "author": "Teddy Roosevelt",
        "tone": "sharp",
        "theme": "courage",
    },
    {
        "type": "quote",
        "text": "Your future self is watching you right now through your memories.",
        "author": "Aubrey de Grey",
        "tone": "sharp",
        "theme": "consistency",
    },
    {
        "type": "quote",
        "text": "The resistance you feel is proportional to the importance of the work.",
        "author": "Steven Pressfield, The War of Art",
        "tone": "sharp",
        "theme": "courage",
    },
    {
        "type": "quote",
        "text": "Small disciplines repeated with consistency every day lead to great achievements gained slowly over time.",
        "author": "John C. Maxwell",
        "tone": "sharp",
        "theme": "consistency",
    },
    {
        "type": "quote",
        "text": "Either you run the day or the day runs you.",
        "author": "Jim Rohn",
        "tone": "sharp",
        "theme": "consistency",
    },
    {
        "type": "quote",
        "text": "The amateur waits for inspiration. The professional steals it.",
        "author": "Austin Kleon, Steal Like an Artist",
        "tone": "sharp",
        "theme": "creativity",
    },

    # ── WARM QUOTES ─────────────────────────────────────────────────────────
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
    {
        "type": "quote",
        "text": "Rest when you're weary. Refresh and renew yourself, your body, your mind, your spirit. Then get back to work.",
        "author": "Ralph Marston",
        "tone": "warm",
        "theme": "rest & recovery",
    },
    {
        "type": "quote",
        "text": "Almost everything will work again if you unplug it for a few minutes, including you.",
        "author": "Anne Lamott",
        "tone": "warm",
        "theme": "rest & recovery",
    },
    {
        "type": "quote",
        "text": "You are not behind. You are exactly where you need to be.",
        "author": "Anonymous",
        "tone": "warm",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "Vulnerability is not winning or losing; it's having the courage to show up and be seen when we have no control over the outcome.",
        "author": "Brené Brown",
        "tone": "warm",
        "theme": "courage",
    },
    {
        "type": "quote",
        "text": "Progress, not perfection.",
        "author": "Recovery tradition",
        "tone": "warm",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "You are enough just as you are. And you can always grow.",
        "author": "Carl Rogers",
        "tone": "warm",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "Every expert was once a beginner. Every pro was once an amateur.",
        "author": "Robin Sharma",
        "tone": "warm",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "Be gentle with yourself. You are a child of the universe, no less than the trees and the stars.",
        "author": "Max Ehrmann, Desiderata",
        "tone": "warm",
        "theme": "rest & recovery",
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
        "text": "You don't rise to the level of your goals. You fall to the level of your systems. Build the system.",
        "author": "James Clear, Atomic Habits",
        "tone": "both",
        "theme": "consistency",
    },
    {
        "type": "quote",
        "text": "The cave you fear to enter holds the treasure you seek.",
        "author": "Joseph Campbell",
        "tone": "both",
        "theme": "courage",
    },
    {
        "type": "quote",
        "text": "You don't have to be great to start, but you have to start to be great.",
        "author": "Zig Ziglar",
        "tone": "both",
        "theme": "finishing",
    },
    {
        "type": "quote",
        "text": "What you do every day matters more than what you do once in a while.",
        "author": "Gretchen Rubin",
        "tone": "both",
        "theme": "consistency",
    },
    {
        "type": "quote",
        "text": "The world breaks everyone, and afterward, some are strong at the broken places.",
        "author": "Ernest Hemingway",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "A person who never made a mistake never tried anything new.",
        "author": "Albert Einstein",
        "tone": "both",
        "theme": "courage",
    },
    {
        "type": "quote",
        "text": "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
        "tone": "both",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "The meaning of life is to find your gift. The purpose of life is to give it away.",
        "author": "Pablo Picasso",
        "tone": "both",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "It is not the mountain we conquer, but ourselves.",
        "author": "Edmund Hillary",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "Creativity is intelligence having fun.",
        "author": "Albert Einstein",
        "tone": "both",
        "theme": "creativity",
    },
    {
        "type": "quote",
        "text": "The two most important days in your life are the day you were born and the day you find out why.",
        "author": "Mark Twain",
        "tone": "both",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "Fall seven times, stand up eight.",
        "author": "Japanese proverb",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "Whether you think you can or you think you can't, you're right.",
        "author": "Henry Ford",
        "tone": "both",
        "theme": "courage",
    },
    {
        "type": "quote",
        "text": "The secret of getting ahead is getting started.",
        "author": "Mark Twain",
        "tone": "both",
        "theme": "finishing",
    },
    {
        "type": "quote",
        "text": "Energy and persistence conquer all things.",
        "author": "Benjamin Franklin",
        "tone": "both",
        "theme": "hard work",
    },
    {
        "type": "quote",
        "text": "Done is better than perfect.",
        "author": "Sheryl Sandberg",
        "tone": "both",
        "theme": "finishing",
    },
    {
        "type": "quote",
        "text": "Endure. In enduring, grow strong.",
        "author": "J.D. Salinger",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "The real voyage of discovery consists not in seeking new landscapes, but in having new eyes.",
        "author": "Marcel Proust",
        "tone": "both",
        "theme": "creativity",
    },
    {
        "type": "quote",
        "text": "You must be the change you wish to see in the world.",
        "author": "Mahatma Gandhi",
        "tone": "both",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "I can't go back to yesterday because I was a different person then.",
        "author": "Lewis Carroll",
        "tone": "both",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "Start where you are. Use what you have. Do what you can.",
        "author": "Arthur Ashe",
        "tone": "both",
        "theme": "hard work",
    },
    {
        "type": "quote",
        "text": "Knowing is not enough; we must apply. Willing is not enough; we must do.",
        "author": "Johann Wolfgang von Goethe",
        "tone": "both",
        "theme": "finishing",
    },
    {
        "type": "quote",
        "text": "Great things are not done by impulse, but by a series of small things brought together.",
        "author": "Vincent Van Gogh",
        "tone": "both",
        "theme": "consistency",
    },
    {
        "type": "quote",
        "text": "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived.",
        "author": "Ralph Waldo Emerson",
        "tone": "both",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "We suffer more in imagination than in reality.",
        "author": "Seneca",
        "tone": "both",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "Waste no more time arguing about what a good person should be. Be one.",
        "author": "Marcus Aurelius",
        "tone": "sharp",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "You have power over your mind, not outside events. Realize this, and you will find strength.",
        "author": "Marcus Aurelius",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "Difficulties strengthen the mind, as labor does the body.",
        "author": "Seneca",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "First say to yourself what you would be; and then do what you have to do.",
        "author": "Epictetus",
        "tone": "sharp",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "It never gets easier. You just get better.",
        "author": "Athletic tradition",
        "tone": "both",
        "theme": "hard work",
    },
    {
        "type": "quote",
        "text": "Comparison is the thief of joy.",
        "author": "Theodore Roosevelt",
        "tone": "warm",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "The best time to plant a tree was 20 years ago. The second best time is now.",
        "author": "Chinese proverb",
        "tone": "both",
        "theme": "finishing",
    },
    {
        "type": "quote",
        "text": "You will never always be motivated. You have to learn to be disciplined.",
        "author": "Anonymous",
        "tone": "sharp",
        "theme": "consistency",
    },
    {
        "type": "quote",
        "text": "Sometimes the most productive thing you can do is rest.",
        "author": "Mark Black",
        "tone": "warm",
        "theme": "rest & recovery",
    },
    {
        "type": "quote",
        "text": "Creativity requires the courage to let go of certainties.",
        "author": "Erich Fromm",
        "tone": "both",
        "theme": "creativity",
    },
    {
        "type": "quote",
        "text": "An idea that is not dangerous is unworthy of being called an idea at all.",
        "author": "Oscar Wilde",
        "tone": "sharp",
        "theme": "intellectual perseverance",
    },
    {
        "type": "quote",
        "text": "The ones who are crazy enough to think they can change the world are the ones who do.",
        "author": "Steve Jobs",
        "tone": "both",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "Pain is temporary. Quitting lasts forever.",
        "author": "Lance Armstrong",
        "tone": "sharp",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "You don't find the happy life. You make it.",
        "author": "Camilla Eyring Kimball",
        "tone": "both",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "If you're not failing, you're not pushing your limits, and if you're not pushing your limits, you're not maximizing your potential.",
        "author": "Ray Dalio",
        "tone": "both",
        "theme": "courage",
    },
    {
        "type": "quote",
        "text": "Be not afraid of going slowly. Be only afraid of standing still.",
        "author": "Chinese proverb",
        "tone": "warm",
        "theme": "consistency",
    },
    {
        "type": "quote",
        "text": "Act as if what you do makes a difference. It does.",
        "author": "William James",
        "tone": "warm",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "You don't have to see the whole staircase, just take the first step.",
        "author": "Martin Luther King Jr.",
        "tone": "warm",
        "theme": "courage",
    },
    {
        "type": "quote",
        "text": "The harder I work, the luckier I get.",
        "author": "Samuel Goldwyn",
        "tone": "sharp",
        "theme": "hard work",
    },
    {
        "type": "quote",
        "text": "Twenty years from now you will be more disappointed by the things you didn't do than by the ones you did.",
        "author": "Mark Twain",
        "tone": "both",
        "theme": "courage",
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
        "theme": "creativity",
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
    {
        "type": "story",
        "text": (
            "J.K. Rowling was a single mother on welfare when she wrote the first Harry Potter book in Edinburgh cafés, "
            "using her daughter's nap times as writing windows. The manuscript was rejected by 12 publishers. "
            "The 13th said yes. She later said the rock-bottom period was also the foundation — "
            "she had nothing left to lose, so she was free to write exactly what she wanted. "
            "Constraints can be permission in disguise."
        ),
        "author": "J.K. Rowling, Harry Potter series",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Beethoven began losing his hearing in his late 20s — a catastrophe for a musician. "
            "By 1814 he was almost entirely deaf. "
            "His Ninth Symphony, one of the most celebrated works in Western music, was composed in complete silence. "
            "He never heard a single note of it performed. "
            "At the premiere, he had to be turned around to see the standing ovation he couldn't hear. "
            "The work does not require ideal conditions. Only commitment."
        ),
        "author": "Ludwig van Beethoven",
        "tone": "both",
        "theme": "hard work",
    },
    {
        "type": "story",
        "text": (
            "Michael Jordan was cut from his high school varsity basketball team as a sophomore. "
            "He went home, locked himself in his room, and cried. "
            "Then he came back — harder, earlier, longer than anyone else on the junior varsity team. "
            "He later said that every time he wanted to stop training, he pictured that list without his name on it. "
            "Rejection is data. Use it."
        ),
        "author": "Michael Jordan, six-time NBA champion",
        "tone": "sharp",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Vera Rubin spent her career studying the rotation curves of galaxies and finding results "
            "that defied existing physics. Colleagues dismissed her data for years. "
            "She kept measuring, kept publishing, kept pushing. "
            "Her work became the primary observational evidence for dark matter — "
            "one of the most significant discoveries in 20th-century cosmology. "
            "She never won the Nobel Prize before she died. The universe confirmed her anyway."
        ),
        "author": "Vera Rubin, astronomer",
        "tone": "both",
        "theme": "intellectual perseverance",
    },
    {
        "type": "story",
        "text": (
            "Winston Churchill failed the entrance exam for the Royal Military College twice before passing on the third attempt. "
            "He was defeated in his first election for Parliament, then defeated again. "
            "He became Prime Minister of Britain at age 65 — considered too old and too difficult by most of his party. "
            "He led the country through its darkest hours and is now regarded as one of the greatest leaders in modern history. "
            "The timeline is not what matters. The arrival is."
        ),
        "author": "Winston Churchill, Prime Minister of the United Kingdom",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Oprah Winfrey was fired from her first television job as a news anchor and told she was "
            "'unfit for TV.' She had grown up in extreme poverty and faced abuse throughout her childhood. "
            "She went on to build the most successful talk show in history and become the first Black female billionaire. "
            "She later said: 'Every stumble is a lesson. The question is whether you pick it up or step over it.'"
        ),
        "author": "Oprah Winfrey, media executive",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Eliud Kipchoge, the greatest marathon runner in history, trains with a group in Kenya "
            "where every session is logged in a notebook. He runs 120 miles a week, every week, for months. "
            "He says the secret is not the big race — it is showing up for the small, invisible sessions "
            "when no one is watching and nothing is at stake. "
            "'Only the disciplined ones in life are free,' he says. The race is just the exhibition."
        ),
        "author": "Eliud Kipchoge, marathon world record holder",
        "tone": "sharp",
        "theme": "consistency",
    },
    {
        "type": "story",
        "text": (
            "Frida Kahlo was in a near-fatal bus accident at 18 that left her with a shattered spine, "
            "collarbone, ribs, and pelvis. She spent months in a full-body cast. "
            "Her mother had a mirror mounted on the ceiling above her bed so she could see herself. "
            "She began painting self-portraits from that position. "
            "She went on to become one of the most celebrated artists of the 20th century. "
            "The constraint became the canvas."
        ),
        "author": "Frida Kahlo, artist",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Stephen King threw the first draft of Carrie in the trash. "
            "His wife Tabitha retrieved it, read it, and told him to keep going. "
            "It had been rejected 30 times. "
            "Carrie became his first published novel and launched one of the most prolific careers in fiction. "
            "King now writes 2,000 words every single day — including Christmas, his birthday, and the Fourth of July. "
            "'The first draft of anything is just you telling yourself the story,' he says. Tell it anyway."
        ),
        "author": "Stephen King, author",
        "tone": "both",
        "theme": "consistency",
    },
    {
        "type": "story",
        "text": (
            "Nikola Tesla arrived in New York in 1884 with four cents in his pocket, a poem, and a letter of recommendation. "
            "He was cheated by partners, had his lab burn down twice, and died broke and alone. "
            "Yet his inventions — AC electricity, the induction motor, radio transmission — "
            "are the invisible infrastructure of modern civilization. "
            "He worked not for recognition, but because the work demanded to exist. "
            "Do it for the work."
        ),
        "author": "Nikola Tesla, inventor",
        "tone": "both",
        "theme": "purpose",
    },
    {
        "type": "story",
        "text": (
            "Nelson Mandela served 27 years in prison on Robben Island. "
            "During that time, he studied, organized, debated, and led — from inside a cell. "
            "He emerged not bitter but resolute, and led South Africa's transition from apartheid to democracy. "
            "He said: 'I never lose. I either win or learn.' "
            "The circumstances do not determine the outcome. The person does."
        ),
        "author": "Nelson Mandela, President of South Africa",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Albert Einstein did not speak until he was four years old. His teachers called him 'mentally slow.' "
            "He failed his first university entrance exam. He couldn't get an academic job after graduating "
            "and worked as a patent clerk. "
            "In 1905 — his 'miracle year' — he published four papers that transformed physics forever, "
            "including the theory of special relativity. He was 26. "
            "The world's timeline for your potential is not the right one."
        ),
        "author": "Albert Einstein, Nobel Laureate in Physics",
        "tone": "warm",
        "theme": "self-doubt",
    },
    {
        "type": "story",
        "text": (
            "Maya Angelou had a traumatic childhood that left her mute for five years. "
            "She worked as a cook, a streetcar conductor, and a nightclub dancer before she became a writer. "
            "I Know Why the Caged Bird Sings was rejected by every publisher she approached before it was finally accepted. "
            "She went on to become one of the most celebrated poets and memoirists in American history. "
            "'You may not control all the events that happen to you,' she said, "
            "'but you can decide not to be reduced by them.'"
        ),
        "author": "Maya Angelou, poet and author",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Kobe Bryant was known to be the first one in the gym and the last to leave — every day, for 20 years. "
            "He once asked a trainer what time it was after a workout. '3am,' the trainer said. "
            "'Good,' Kobe said, 'I'll be back here at 7.' "
            "He won five NBA championships and became one of the greatest players in history. "
            "When asked his secret, he said simply: 'I never asked anyone to work harder than me.' "
            "The standard is set by what you do when no one is watching."
        ),
        "author": "Kobe Bryant, NBA champion",
        "tone": "sharp",
        "theme": "consistency",
    },
    {
        "type": "story",
        "text": (
            "Claude Monet developed cataracts in both eyes in the 1910s and slowly went nearly blind. "
            "Terrified of losing his sight completely, he kept painting — his colors growing more distorted, "
            "his brushstrokes more frantic. "
            "The Water Lilies series, now housed in the Orangerie in Paris and considered among the greatest "
            "paintings in existence, were made almost entirely while he could barely see. "
            "The limitation became the vision."
        ),
        "author": "Claude Monet, painter",
        "tone": "both",
        "theme": "creativity",
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
