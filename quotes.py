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
    {
        "type": "story",
        "text": (
            "James Dyson made 5,127 prototypes of his bagless vacuum cleaner before one worked. "
            "It took fifteen years. His wife supported the family on a teacher's salary while he kept failing. "
            "Every prototype taught him something the previous one hadn't. "
            "When he finally launched, competitors laughed — then copied him. "
            "Dyson is now one of the most valuable companies in the UK. "
            "'I wanted to give up almost every day,' he said. 'But you have to keep going.'"
        ),
        "author": "James Dyson, inventor and entrepreneur",
        "tone": "both",
        "theme": "hard work",
    },
    {
        "type": "story",
        "text": (
            "Sylvester Stallone was so broke he sold his dog for $25 because he couldn't afford to feed it. "
            "After watching a Muhammad Ali fight, he went home and wrote the screenplay for Rocky in three and a half days. "
            "Producers offered to buy it — but only if Stallone wasn't in it. He refused. "
            "He was rejected over 1,500 times. He eventually got his deal, bought his dog back for $3,000, "
            "and Rocky won three Academy Awards including Best Picture. "
            "Know what you're worth. Don't sell it."
        ),
        "author": "Sylvester Stallone, Rocky",
        "tone": "both",
        "theme": "courage",
    },
    {
        "type": "story",
        "text": (
            "Colonel Harland Sanders was 65 years old when his restaurant was shut down by a new highway. "
            "He had $105 from his first Social Security check. "
            "He drove across America trying to sell his fried chicken recipe to restaurants. "
            "He was rejected 1,009 times before someone said yes. "
            "Kentucky Fried Chicken now has over 25,000 locations in 145 countries. "
            "It is genuinely never too late."
        ),
        "author": "Colonel Harland Sanders, KFC founder",
        "tone": "warm",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Walt Disney was fired from the Kansas City Star newspaper in 1919. "
            "The editor said he 'lacked imagination and had no good ideas.' "
            "His first animation studio went bankrupt. "
            "He was turned down 302 times when trying to finance Disneyland. "
            "He later said: 'All our dreams can come true, if we have the courage to pursue them.' "
            "The person who called you unimaginative does not get to write your ending."
        ),
        "author": "Walt Disney, founder of The Walt Disney Company",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Thomas Edison's teachers told him he was 'too stupid to learn anything.' "
            "He was fired from his first two jobs for being 'non-productive.' "
            "When a reporter asked him how it felt to fail 1,000 times before inventing the light bulb, "
            "Edison replied: 'I didn't fail 1,000 times. The light bulb was an invention with 1,000 steps.' "
            "He held 1,093 patents by the time he died. "
            "Reframe the failures. They are the process."
        ),
        "author": "Thomas Edison, inventor",
        "tone": "both",
        "theme": "intellectual perseverance",
    },
    {
        "type": "story",
        "text": (
            "Vincent Van Gogh sold exactly one painting during his lifetime — to a friend, for a small sum. "
            "He was mocked, institutionalized, and largely unknown. "
            "He wrote over 800 letters to his brother Theo, documenting his obsession with color and light. "
            "He produced over 2,000 works in ten years before dying at 37. "
            "His paintings now sell for hundreds of millions of dollars. "
            "The work was never for the market. The work was for the truth."
        ),
        "author": "Vincent Van Gogh, painter",
        "tone": "both",
        "theme": "purpose",
    },
    {
        "type": "story",
        "text": (
            "Abraham Lincoln lost his job, failed in business twice, had a nervous breakdown, "
            "and was defeated in eight separate elections before becoming President of the United States. "
            "The timeline from first political defeat to the Oval Office spanned 28 years. "
            "He later said: 'My great concern is not whether you have failed, but whether you are content with your failure.' "
            "The record of defeats is not the story. What you do next is."
        ),
        "author": "Abraham Lincoln, 16th President of the United States",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Stephen Hawking was diagnosed with ALS at 21 and given two years to live. "
            "He lived to 76. He lost his ability to speak and was confined to a wheelchair, "
            "communicating through a single cheek muscle twitching against a sensor. "
            "He wrote A Brief History of Time, held Newton's chair at Cambridge, "
            "and fundamentally changed our understanding of black holes and cosmology. "
            "'However difficult life may seem,' he said, 'there is always something you can do and succeed at.' "
            "Do not negotiate with your constraints. Work inside them."
        ),
        "author": "Stephen Hawking, theoretical physicist",
        "tone": "both",
        "theme": "hard work",
    },
    {
        "type": "story",
        "text": (
            "Katherine Johnson calculated orbital trajectories for NASA by hand at a time when "
            "electronic computers were new and untrusted. "
            "When John Glenn was about to orbit Earth in 1962, he refused to fly "
            "unless 'the girl' — Katherine — personally verified the computer's numbers. "
            "She did. He flew. She worked at NASA until she was 33, "
            "as a Black woman in the segregated South, doing mathematics that held human lives. "
            "She was given the Presidential Medal of Freedom at age 97. "
            "Precision is its own form of courage."
        ),
        "author": "Katherine Johnson, NASA mathematician",
        "tone": "both",
        "theme": "intellectual perseverance",
    },
    {
        "type": "story",
        "text": (
            "Rosalind Franklin's X-ray diffraction images of DNA were the clearest evidence "
            "of DNA's double helix structure ever captured. "
            "Her image — Photo 51 — was shown to Watson and Crick without her knowledge or consent. "
            "It was central to their Nobel Prize-winning discovery. She received no credit. "
            "She died at 37 of ovarian cancer, never knowing how pivotal her work had been. "
            "The Nobel committee does not get to decide what your contribution was worth. "
            "Do the work. The truth catches up."
        ),
        "author": "Rosalind Franklin, chemist and X-ray crystallographer",
        "tone": "both",
        "theme": "intellectual perseverance",
    },
    {
        "type": "story",
        "text": (
            "Frederick Douglass was born into slavery and taught himself to read "
            "by trading bread with white children who could. "
            "Reading showed him the distance between what he was told he was "
            "and what he actually was. He escaped at 20, wrote his autobiography, "
            "became one of the most powerful orators in American history, "
            "and advised Abraham Lincoln during the Civil War. "
            "'Once you learn to read,' he said, 'you will be forever free.' "
            "The mind they cannot take is the one you build."
        ),
        "author": "Frederick Douglass, abolitionist and statesman",
        "tone": "both",
        "theme": "courage",
    },
    {
        "type": "story",
        "text": (
            "Paulo Coelho burned his manuscript for The Alchemist after writing it. "
            "Then rewrote it. It was rejected by every publisher he approached. "
            "A small Brazilian press finally printed 900 copies. "
            "It sold so poorly they declined to print more. "
            "Coelho found another publisher. The book has now sold over 65 million copies "
            "and been translated into 80 languages — the most translated book by a living author. "
            "The world is slow to recognize what it needs most."
        ),
        "author": "Paulo Coelho, The Alchemist",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Roger Bannister was a medical student with only 45 minutes a day to train "
            "when he decided to attempt the 4-minute mile — "
            "a barrier that had stood for centuries and that physiologists said was physically impossible for humans. "
            "On May 6, 1954, he ran it in 3:59.4. "
            "Within 46 days, someone else broke his record. Within a year, three runners broke it in the same race. "
            "The barrier was never physical. It was belief. "
            "Once one person shows it can be done, everyone knows it can be done."
        ),
        "author": "Roger Bannister, first person to run a sub-4-minute mile",
        "tone": "both",
        "theme": "courage",
    },
    {
        "type": "story",
        "text": (
            "Haruki Murakami was 29 years old, watching a baseball game, when he suddenly knew he could write a novel. "
            "He had no training, no plan, no literary connections. "
            "He went home and started. "
            "He now wakes at 4am every day, writes for five to six hours, then runs 10km. "
            "He has done this for decades. He has run 33 marathons. "
            "'If you only do the things you enjoy,' he says, 'you can't keep running a marathon.' "
            "The discipline is the dream made daily."
        ),
        "author": "Haruki Murakami, novelist and marathon runner",
        "tone": "both",
        "theme": "consistency",
    },
    {
        "type": "story",
        "text": (
            "Jonas Salk developed the first effective polio vaccine in 1955 "
            "after years of research that most experts called impossible. "
            "When asked who owned the patent, he said: 'The people. Could you patent the sun?' "
            "He gave it away. No royalties. No fortune. "
            "His decision made the vaccine available to hundreds of millions of children worldwide. "
            "He was asked later if he regretted it. He said the only reward worth having was the work itself."
        ),
        "author": "Jonas Salk, developer of the polio vaccine",
        "tone": "both",
        "theme": "purpose",
    },
    {
        "type": "story",
        "text": (
            "Temple Grandin was nonverbal until age four and was diagnosed with autism at a time "
            "when doctors recommended institutionalization. "
            "Her mother refused. She went on to earn a PhD in animal science and revolutionize "
            "the design of livestock handling facilities — improving the lives of animals worldwide. "
            "She later said: 'The world needs different kinds of minds to work together.' "
            "The brain that thinks differently is not a broken brain. It is a different tool."
        ),
        "author": "Temple Grandin, animal scientist and autism advocate",
        "tone": "warm",
        "theme": "self-doubt",
    },
    {
        "type": "story",
        "text": (
            "Malala Yousafzai was shot in the head by the Taliban at age 15 "
            "for speaking publicly about girls' right to education. "
            "She survived, recovered, and spoke at the United Nations one year later — "
            "on her 16th birthday. "
            "'They thought that the bullet would silence us,' she said. 'But they failed. "
            "Weakness, fear and hopelessness died. Strength, power, and courage was born.' "
            "She became the youngest Nobel Peace Prize laureate in history. "
            "They cannot silence what you decide to stand for."
        ),
        "author": "Malala Yousafzai, Nobel Peace Prize Laureate",
        "tone": "both",
        "theme": "courage",
    },
    {
        "type": "story",
        "text": (
            "Chadwick Boseman was diagnosed with stage 3 colon cancer in 2016. "
            "He told no one in Hollywood. "
            "Over the next four years — as his cancer progressed to stage 4 — "
            "he filmed Black Panther, Avengers: Infinity War, Endgame, and Da 5 Bloods, "
            "often going straight from chemotherapy to set. "
            "He died in 2020. No one on set knew what he was carrying. "
            "Some people show up completely, even when it costs them everything."
        ),
        "author": "Chadwick Boseman, actor",
        "tone": "both",
        "theme": "hard work",
    },
    {
        "type": "story",
        "text": (
            "Ernest Shackleton's ship Endurance was crushed by Antarctic pack ice in 1915, "
            "stranding 28 men on one of the most remote and hostile places on Earth. "
            "For nearly two years, Shackleton kept every single one of his men alive — "
            "through Antarctic winters, open-ocean crossings in a 22-foot boat, "
            "and a mountain crossing with no equipment. "
            "He never lost a man. He later said the key was never letting the men see him give up hope — "
            "not because he felt it, but because he knew they needed him not to. "
            "Leadership sometimes means performing confidence until it becomes real."
        ),
        "author": "Ernest Shackleton, Antarctic explorer",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Fyodor Dostoevsky was led to a firing squad in 1849 for political crimes. "
            "He stood in the snow, blindfolded, listening to the shots kill the men beside him. "
            "Seconds before his turn, a messenger arrived with a commutation: Siberian labor camp instead. "
            "He spent four years in brutal conditions. He came back and wrote Crime and Punishment, "
            "The Brothers Karamazov, and The Idiot. "
            "He said the experience taught him that a single minute of life was worth more than anything. "
            "You have more minutes left than you think. Use them."
        ),
        "author": "Fyodor Dostoevsky, novelist",
        "tone": "both",
        "theme": "purpose",
    },
    {
        "type": "story",
        "text": (
            "Serena Williams won the 2017 Australian Open — her 23rd Grand Slam title — while eight weeks pregnant. "
            "The following year, she nearly died during childbirth from a pulmonary embolism. "
            "She returned to competitive tennis 10 months later. "
            "In 2022, she reached the third round at Wimbledon, aged 40, ranked 1,204th in the world. "
            "She later said: 'I really think a champion is defined not by their wins but by how they can recover when they fall.' "
            "The recovery is the career."
        ),
        "author": "Serena Williams, 23-time Grand Slam champion",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Simone Biles was placed in foster care at age three. "
            "She grew up to become the most decorated gymnast in history — "
            "with 37 World and Olympic medals. "
            "At the Tokyo Olympics, she withdrew from the team final to protect her mental health, "
            "saying she didn't want to risk a serious injury. "
            "The world watched an athlete at the peak of her power choose herself. "
            "She returned the next day to win a bronze medal on beam. "
            "Knowing when to stop is not weakness. It is the hardest form of discipline."
        ),
        "author": "Simone Biles, Olympic gymnast",
        "tone": "warm",
        "theme": "rest & recovery",
    },
    {
        "type": "story",
        "text": (
            "Rumi was a respected Islamic scholar and theologian in his 30s when he met the wandering mystic Shams of Tabriz. "
            "The friendship transformed him entirely. When Shams disappeared — possibly killed — "
            "Rumi collapsed into grief. Then he began to write. "
            "The Masnavi, composed in his grief, is considered one of the greatest works of Persian literature. "
            "He dictated 25,000 verses. "
            "The loss did not end the work. The loss became the work."
        ),
        "author": "Rumi, 13th-century poet and mystic",
        "tone": "both",
        "theme": "purpose",
    },
    {
        "type": "story",
        "text": (
            "Soichiro Honda applied for an engineering position at Toyota after World War II and was rejected. "
            "With no income, he began making small motorcycles out of army surplus engines in his shed. "
            "Neighbors laughed. His wife sold her jewelry to fund supplies. "
            "Honda Motor Company is now one of the largest motorcycle and automobile manufacturers in the world. "
            "When asked about failure, he said: 'Success is 99% failure.' "
            "Toyota's rejection was the founding document of Honda."
        ),
        "author": "Soichiro Honda, founder of Honda Motor Company",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Yo-Yo Ma entered Harvard at 15. But it was the years before that shaped him: "
            "as a child prodigy, he practiced cello so obsessively his parents had to remind him to eat. "
            "He later went through a crisis of meaning — wondering why he played at all. "
            "He came out the other side with an answer: music is not performance, it is communication. "
            "He has since collaborated with everyone from bluegrass musicians to Argentinian tango masters "
            "to Mongolian horsehead fiddlers. "
            "'The only way to do something in depth,' he says, 'is to commit.' "
            "Depth is not narrowness. It is the way through to everything else."
        ),
        "author": "Yo-Yo Ma, cellist",
        "tone": "warm",
        "theme": "purpose",
    },
    {
        "type": "story",
        "text": (
            "Chris Gardner was homeless and sleeping in a San Francisco BART bathroom with his toddler son "
            "while completing an unpaid stockbroker internship. "
            "He had hidden his situation from his employer for months. "
            "He passed the licensing exam, got the job, and eventually founded his own brokerage firm. "
            "Years later he told an interviewer: 'Don't ever let someone tell you that you can't do something. "
            "Not even me.' "
            "The hardest part was not the poverty. It was not letting the poverty become the story."
        ),
        "author": "Chris Gardner, entrepreneur and investor",
        "tone": "both",
        "theme": "hard work",
    },
    {
        "type": "story",
        "text": (
            "Maya Angelou kept a hotel room in every city she ever lived in — "
            "not to sleep, but to write. She'd arrive at 6:30am with a legal pad, a Bible, a bottle of sherry, "
            "and a deck of cards. She'd write until 2pm, go home, and not look at it until the next day. "
            "She said a comfortable environment was the enemy of honest writing. "
            "'You can't use up creativity,' she said. 'The more you use, the more you have.' "
            "Build the ritual. Show up to the ritual. Let the ritual do the work."
        ),
        "author": "Maya Angelou, poet and author",
        "tone": "both",
        "theme": "consistency",
    },
    {
        "type": "story",
        "text": (
            "The Mars Perseverance rover landing in 2021 required what NASA engineers called "
            "'seven minutes of terror' — the time it takes to descend through the Martian atmosphere, "
            "during which the rover is entirely on its own. No human can intervene. "
            "The team had spent years designing, testing, and failing in simulations. "
            "Every system had to work the first time, in a place no one had ever been. "
            "It landed perfectly. "
            "Preparation is the only form of control available. Do everything you can before you let go."
        ),
        "author": "NASA Perseverance Rover Team",
        "tone": "sharp",
        "theme": "intellectual perseverance",
    },
    {
        "type": "story",
        "text": (
            "Chimamanda Ngozi Adichie left Nigeria at 19 for America, knowing no one, "
            "to study communications and political science — subjects she wasn't passionate about. "
            "She switched to creative writing. Her first novel, Purple Hibiscus, was rejected dozens of times. "
            "Half of a Yellow Sun won the Orange Prize for Fiction. "
            "Her TED talk 'We Should All Be Feminists' has been viewed over 8 million times. "
            "She says the danger of a single story is that it becomes the only story. "
            "Your story is not the one they told about you."
        ),
        "author": "Chimamanda Ngozi Adichie, novelist",
        "tone": "both",
        "theme": "courage",
    },
    {
        "type": "story",
        "text": (
            "Galileo Galilei published his support of the Copernican model — "
            "that the Earth moves around the Sun — in 1632. "
            "The Inquisition forced him to recant on his knees. He spent the rest of his life under house arrest. "
            "Legend says that as he rose from his knees he muttered: 'And yet it moves.' "
            "He kept doing science in his final years, conducting experiments on motion and gravity "
            "that laid the groundwork for Newton. "
            "What is true does not stop being true because someone powerful refuses to accept it."
        ),
        "author": "Galileo Galilei, astronomer and physicist",
        "tone": "both",
        "theme": "intellectual perseverance",
    },

    # ── NEW STORIES ──────────────────────────────────────────────────────────
    {
        "type": "story",
        "text": (
            "Wilma Rudolph contracted polio as a child and wore a metal brace on her leg until she was twelve. "
            "Doctors told her she would never walk normally. "
            "She became the fastest woman in the world. "
            "At the 1960 Rome Olympics she won three gold medals in sprinting — the first American woman to do so. "
            "She said: 'The doctors told me I would never walk, but my mother told me I would. "
            "I believed my mother.' "
            "Choose carefully whose voice you let define the possible."
        ),
        "author": "Wilma Rudolph, three-time Olympic gold medalist",
        "tone": "warm",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "William Kamkwamba was 14 years old when a famine forced him to drop out of school in Malawi. "
            "He could no longer afford the $80 annual fee. "
            "He walked to the local library and taught himself physics and engineering from donated textbooks. "
            "Using scrap metal, bicycle parts, and wood from the blue gum trees, he built a windmill "
            "that brought electricity to his family's home for the first time. "
            "He was eventually discovered, sponsored through school, and earned a degree from Dartmouth. "
            "The library was free. The decision to walk in was everything."
        ),
        "author": "William Kamkwamba, engineer and author of The Boy Who Harnessed the Wind",
        "tone": "both",
        "theme": "hard work",
    },
    {
        "type": "story",
        "text": (
            "Grace Hopper was a rear admiral in the US Navy and one of the first programmers of the Harvard Mark I computer. "
            "When a moth caused a relay failure, she taped it into the logbook and wrote 'first actual case of bug being found.' "
            "She coined the term 'debugging.' "
            "She also invented the first compiler — a program that translates human-readable code into machine language — "
            "when colleagues insisted it was impossible for a machine to translate language. "
            "'The most dangerous phrase in the language is: we've always done it this way,' she said. "
            "Question the obvious. That is where the work lives."
        ),
        "author": "Grace Hopper, computer scientist and US Navy Rear Admiral",
        "tone": "sharp",
        "theme": "intellectual perseverance",
    },
    {
        "type": "story",
        "text": (
            "David Bowie reinvented himself so thoroughly and so many times "
            "that no single version of him became a cage. "
            "Ziggy Stardust. Aladdin Sane. The Thin White Duke. Major Tom. "
            "Each was a full commitment — a new sound, new look, new collaborators. "
            "He said: 'I don't know where I'm going from here, but I promise it won't be boring.' "
            "He kept making new music until 69, releasing Blackstar two days before he died of cancer — "
            "a final album he had been quietly working on while terminally ill. "
            "The work was the answer to the fear."
        ),
        "author": "David Bowie, musician",
        "tone": "both",
        "theme": "creativity",
    },
    {
        "type": "story",
        "text": (
            "Agatha Christie had dyslexia and struggled painfully in school. "
            "She taught herself to type by hunting letters one at a time. "
            "She is the best-selling fiction writer in history — only the Bible and Shakespeare have sold more. "
            "She wrote 66 detective novels and 14 short story collections, often while raising a daughter alone. "
            "She said she was simply interested in the puzzle of how things could go wrong, "
            "and curious enough to follow it to the end. "
            "Curiosity outlasts talent every time."
        ),
        "author": "Agatha Christie, best-selling novelist of all time",
        "tone": "warm",
        "theme": "consistency",
    },
    {
        "type": "story",
        "text": (
            "Donna Strickland won the Nobel Prize in Physics in 2018 for her work on laser pulses. "
            "At the time of the announcement, she was not a full professor — just an associate professor "
            "at the University of Waterloo. "
            "Before the Nobel, Wikipedia had rejected a page about her because her work was deemed 'not notable enough.' "
            "She is only the third woman in history to win the Nobel Prize in Physics. "
            "The institution's assessment of your status has nothing to do with the quality of your work."
        ),
        "author": "Donna Strickland, Nobel Laureate in Physics",
        "tone": "sharp",
        "theme": "intellectual perseverance",
    },
    {
        "type": "story",
        "text": (
            "Rita Levi-Montalcini was barred from university in 1938 under Mussolini's racial laws. "
            "She set up a small laboratory in her bedroom and continued her neuroscience research using chicken embryos. "
            "During the Nazi occupation of Florence she conducted experiments while hiding from the Gestapo. "
            "She won the Nobel Prize in Physiology or Medicine in 1986, at age 77. "
            "She continued going to her lab every day until she was 100. "
            "She died at 103. "
            "'Above all, don't fear difficult moments,' she said. 'The best comes from them.'"
        ),
        "author": "Rita Levi-Montalcini, Nobel Laureate in Physiology or Medicine",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Bob Ross spent 20 years in the US Air Force rising to master sergeant — "
            "a job, he said, that required him to 'be mean, make people scrub toilets, clean the latrine.' "
            "He vowed if he ever left, he would never scream at anyone again. "
            "He left. He became the soft-spoken painting instructor who told 3.7 million weekly viewers "
            "there were no mistakes, only happy accidents. "
            "He filmed 403 episodes of The Joy of Painting and donated almost every canvas. "
            "The discipline to be gentle is harder than the discipline to be hard."
        ),
        "author": "Bob Ross, painter and television host",
        "tone": "warm",
        "theme": "purpose",
    },
    {
        "type": "story",
        "text": (
            "Isabel Allende wrote her first novel as a letter to her dying grandfather in Chile, "
            "while living in exile in Venezuela. She had no intention of writing a novel. "
            "She just didn't want him to die before she could tell him things. "
            "The letter grew into The House of the Spirits, one of the defining works of Latin American literature. "
            "She has since written 26 books. She starts every new one on January 8th — the same date she started that letter. "
            "Ritual is how you honor what matters."
        ),
        "author": "Isabel Allende, author of The House of the Spirits",
        "tone": "warm",
        "theme": "purpose",
    },
    {
        "type": "story",
        "text": (
            "David Goggins weighed 300 pounds, was working as a pest exterminator, "
            "and had failed Navy SEAL training twice. "
            "A doctor told him he had a congenital heart defect and shouldn't attempt it again. "
            "He attempted it again. He passed. "
            "He later ran 100-mile ultramarathons, set a world record for pull-ups (4,030 in 17 hours), "
            "and finished the Badwater 135 — considered the world's toughest foot race — multiple times. "
            "'The most important conversations you'll ever have,' he says, 'are the ones you have with yourself.' "
            "The story you tell yourself about what you can do becomes the ceiling. Change the story."
        ),
        "author": "David Goggins, ultramarathon runner and retired Navy SEAL",
        "tone": "sharp",
        "theme": "hard work",
    },
    {
        "type": "story",
        "text": (
            "Astrid Lindgren invented Pippi Longstocking in 1941 to entertain her daughter Karin, "
            "who was home sick with pneumonia and asked for a story about a girl who could do anything. "
            "Lindgren told her about Pippi — the strongest girl in the world, who lived alone, "
            "had a horse on her porch, and answered to no one. "
            "When she submitted the manuscript, it was initially rejected. "
            "A different publisher accepted it. It became one of the most beloved children's books ever written. "
            "The best ideas often start as a gift for someone you love."
        ),
        "author": "Astrid Lindgren, author of Pippi Longstocking",
        "tone": "warm",
        "theme": "creativity",
    },
    {
        "type": "story",
        "text": (
            "Hedy Lamarr was one of the biggest Hollywood stars of the 1940s. "
            "What the studios did not know was that she spent her nights inventing. "
            "Working with composer George Antheil, she co-invented a frequency-hopping signal "
            "to prevent torpedo guidance systems from being jammed during World War II. "
            "The military ignored it. The patent expired. "
            "Decades later, her invention became the foundation for Wi-Fi, GPS, and Bluetooth. "
            "She never received a cent. 'Films have a certain place in a certain time period,' she said. "
            "'Technology is forever.'"
        ),
        "author": "Hedy Lamarr, actress and inventor",
        "tone": "both",
        "theme": "intellectual perseverance",
    },
    {
        "type": "story",
        "text": (
            "Roald Amundsen prepared for years to be the first to reach the South Pole. "
            "He studied Inuit survival techniques. He trained with sled dogs. He chose skiers. "
            "His rival Robert Scott brought motorized sleds, horses, and inadequate cold-weather gear. "
            "Amundsen arrived at the pole on December 14, 1911. "
            "He left a tent and a note for Scott, who arrived 33 days later. "
            "Scott and his entire team died on the return journey. "
            "Preparation is not the opposite of courage. It is courage made practical."
        ),
        "author": "Roald Amundsen, first person to reach the South Pole",
        "tone": "sharp",
        "theme": "hard work",
    },
    {
        "type": "story",
        "text": (
            "James Baldwin left America in 1948 because, he said, it was either leave or be destroyed by it. "
            "He wrote from Paris — broke, cold, sometimes hungry — "
            "and produced Go Tell It on the Mountain, Giovanni's Room, and Notes of a Native Son. "
            "He came back for the Civil Rights Movement, spoke alongside Martin Luther King, "
            "and kept writing through grief, rage, and love. "
            "'Not everything that is faced can be changed,' he said, "
            "'but nothing can be changed until it is faced.' "
            "The writing is the facing."
        ),
        "author": "James Baldwin, novelist and activist",
        "tone": "both",
        "theme": "courage",
    },
    {
        "type": "story",
        "text": (
            "Yayoi Kusama began having hallucinations as a child — flowers speaking to her, "
            "dots multiplying across her vision. "
            "She turned the visions into art: dots, nets, infinity rooms. "
            "At 27 she moved to New York with almost no money and built a reputation in the avant-garde scene. "
            "At 44, she checked herself voluntarily into a psychiatric hospital in Tokyo. "
            "She has lived there ever since — and walks to her studio across the street every day to make art. "
            "'I fight pain, anxiety, and fear every day,' she says, 'and the only method I have found that relieves it is to keep creating.' "
            "The work is not a distraction from the struggle. It is the response to it."
        ),
        "author": "Yayoi Kusama, artist",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Wangari Maathai was told by the Kenyan government, by foreign donors, and by her own husband "
            "that planting trees was too small an idea to matter. "
            "She started the Green Belt Movement in 1977 with a group of rural women. "
            "They planted trees — one at a time, across decades. "
            "By 2004, they had planted 47 million trees and restored entire ecosystems. "
            "She was arrested, beaten, imprisoned. "
            "That year she became the first African woman and first environmentalist to win the Nobel Peace Prize. "
            "Big enough is whatever you plant and keep watering."
        ),
        "author": "Wangari Maathai, Nobel Peace Prize Laureate",
        "tone": "both",
        "theme": "consistency",
    },
    {
        "type": "story",
        "text": (
            "Ruth Bader Ginsburg graduated top of her class from Harvard Law School "
            "and tied for first at Columbia Law. "
            "Not a single New York law firm would hire her — she was a woman, a mother, and Jewish. "
            "A professor had to personally beg a judge to take her as a clerk. "
            "She spent the next decades dismantling sex discrimination law one case at a time, "
            "arguing before the Supreme Court. She later joined it. "
            "She worked on opinions hours after chemotherapy. She did twenty push-ups a day at 84. "
            "'Fight for the things you care about,' she said, 'but do it in a way that will lead others to join you.'"
        ),
        "author": "Ruth Bader Ginsburg, US Supreme Court Justice",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Tererai Trent grew up in rural Zimbabwe without access to school. "
            "She was married at 11, had three children by 18. "
            "A visiting American development worker asked her what her dreams were. "
            "She wrote them on a piece of paper, put them in a tin, and buried the tin in the earth. "
            "'I will go to America. I will get a bachelor's degree. A master's. A PhD.' "
            "She achieved every one. When she did, she went back to Zimbabwe and dug up the tin. "
            "She has since built schools there. "
            "Write the dream down. Then get started."
        ),
        "author": "Tererai Trent, educator and activist",
        "tone": "warm",
        "theme": "purpose",
    },
    {
        "type": "story",
        "text": (
            "Octavia Butler grew up poor in Pasadena, was told she had no writing talent, "
            "and was working a series of menial jobs when she began waking at 3am to write before her shift. "
            "She taped a note to her typewriter: 'I will be a bestselling writer. I will.' "
            "She became one of the most celebrated science fiction writers in history, "
            "winning both the Hugo and Nebula awards — the genre's highest honors. "
            "She was the first science fiction writer to receive the MacArthur 'Genius' Fellowship. "
            "'First forget inspiration,' she said. 'Habit is more dependable. Habit will sustain you whether you're inspired or not.'"
        ),
        "author": "Octavia Butler, science fiction author",
        "tone": "sharp",
        "theme": "consistency",
    },
    {
        "type": "story",
        "text": (
            "Isaac Asimov wrote or edited over 500 books in his lifetime — "
            "across science fiction, history, chemistry, the Bible, Shakespeare, and humor. "
            "He wrote every single day, including weekends and holidays. "
            "When asked how he produced so much, he said: "
            "'I don't know. I don't think about it. Writing is my only recreation.' "
            "He wasn't prolific because he was disciplined. He was prolific because writing was where he wanted to be. "
            "Find the work that doesn't feel like escaping from work. Do it every day."
        ),
        "author": "Isaac Asimov, author of over 500 books",
        "tone": "both",
        "theme": "consistency",
    },
    {
        "type": "story",
        "text": (
            "Roald Dahl wrote in a small brick shed at the bottom of his garden — same shed, same chair, same yellow legal pads, "
            "same six pencils sharpened to exactly the same length each morning. "
            "He wrote from 10am to 12pm, then again from 4pm to 6pm, every day. "
            "The children who read his books had no idea they were made in a garden shed, "
            "by a man who refused to start until conditions were exactly as he required. "
            "'A writer of fiction,' he said, 'lives in fear. Each new day demands new ideas.' "
            "The ritual was the answer to the fear."
        ),
        "author": "Roald Dahl, author of Charlie and the Chocolate Factory",
        "tone": "both",
        "theme": "consistency",
    },
    {
        "type": "story",
        "text": (
            "Pele grew up so poor in Bauru, Brazil that he could not afford a football. "
            "He played with a grapefruit stuffed into a sock, or a ball made of rags. "
            "He was 15 when he joined Santos FC. At 17, he became the youngest player "
            "to score in a World Cup final. He won the World Cup three times. "
            "He is still the only player to do so. "
            "He said the difference between success and failure was not talent — "
            "it was whether you kept showing up after you failed. "
            "You cannot stop a person who will not stop."
        ),
        "author": "Pelé, three-time FIFA World Cup champion",
        "tone": "both",
        "theme": "hard work",
    },
    {
        "type": "story",
        "text": (
            "Wislawa Szymborska worked as a poetry editor at a Krakow literary journal for decades, "
            "virtually unknown outside Poland. "
            "She published fewer than 400 poems in her entire lifetime — "
            "tearing up anything she felt did not meet her standard. "
            "In 1996, she won the Nobel Prize in Literature. "
            "She said she threw away far more than she kept. "
            "'I don't know,' she would say whenever asked a question — and meant it as a philosophy. "
            "The willingness not to know, to keep questioning, was what made the poems worth anything."
        ),
        "author": "Wislawa Szymborska, Nobel Laureate in Literature",
        "tone": "warm",
        "theme": "intellectual perseverance",
    },
    {
        "type": "story",
        "text": (
            "Langston Hughes discovered he wanted to write poetry at 13, "
            "after his teacher told him to read Carl Sandburg. "
            "He worked as a busboy in a Washington D.C. hotel when he was 24, "
            "still unknown. One evening he left three of his poems beside the plate "
            "of the famous poet Vachel Lindsay, who was dining there. "
            "Lindsay read them aloud at a public reading that night and announced he had discovered a genius. "
            "Hughes woke up famous. "
            "He spent the next five decades writing the Harlem Renaissance into existence. "
            "Leave the work where it can be found."
        ),
        "author": "Langston Hughes, poet of the Harlem Renaissance",
        "tone": "both",
        "theme": "courage",
    },
    {
        "type": "story",
        "text": (
            "Lynn Conway was fired from IBM in 1968 after announcing she was a transgender woman. "
            "She was erased from her own research record. She started over, completely, under a new name. "
            "She went on to co-develop the VLSI design rules that made modern microchip manufacturing possible — "
            "the foundation of every computer chip built in the last 40 years. "
            "Her contributions were uncredited for decades. "
            "She said: 'People often underestimate the ability of individuals to reinvent themselves "
            "and to be transformed by new experiences.' "
            "The reinvention was not a setback. It was the work."
        ),
        "author": "Lynn Conway, computer scientist and VLSI pioneer",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Wole Soyinka was imprisoned in solitary confinement for 22 months during the Nigerian Civil War — "
            "in a cell so small he could not stand upright. "
            "He was given no books, no paper, no contact with other humans. "
            "He scratched notes onto scraps of toilet paper and between the lines of a Bible "
            "that was eventually smuggled to him. "
            "He kept writing in his head even when he had nothing to write on. "
            "He was released, the notes were recovered, and he became the first African to win the Nobel Prize in Literature. "
            "'You cannot imprison a mind that refuses to be imprisoned.'"
        ),
        "author": "Wole Soyinka, Nobel Laureate in Literature",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "story",
        "text": (
            "Siddharth Mukherjee wrote The Emperor of All Maladies — "
            "a biography of cancer that won the Pulitzer Prize — "
            "while completing a hematology-oncology fellowship at Dana-Farber Cancer Institute. "
            "He was working 80-hour weeks in the hospital. He wrote on nights and weekends for four years. "
            "He said the book was a way of understanding the patients he was losing — "
            "a way to sit with the disease long enough to see it clearly. "
            "The hardest work often grows out of the hardest circumstances. "
            "Let the question you cannot stop thinking about become the project."
        ),
        "author": "Siddharth Mukherjee, oncologist and Pulitzer Prize winner",
        "tone": "both",
        "theme": "intellectual perseverance",
    },
    {
        "type": "story",
        "text": (
            "Niklas Luhmann was a German sociologist who had no formal training in the discipline. "
            "Over 40 years, he built a Zettelkasten — a slip-box of interconnected handwritten notes — "
            "containing 90,000 index cards. "
            "Each idea was linked to others; none was isolated. "
            "From this system he produced 70 books and 400 scholarly articles. "
            "When asked how he was so productive, he said: 'I never force myself to do anything I don't feel like doing. "
            "I only do what comes easily. I only write when I immediately know how to do it. "
            "If I falter for a moment, I put the matter aside and do something else.' "
            "The system did the heavy lifting. He just showed up and followed the connections."
        ),
        "author": "Niklas Luhmann, sociologist",
        "tone": "warm",
        "theme": "consistency",
    },
    {
        "type": "story",
        "text": (
            "Anton Chekhov practiced medicine as a country doctor his entire adult life "
            "while writing plays and short stories that would redefine both forms. "
            "He said: 'Medicine is my lawful wife and literature is my mistress.' "
            "He visited the penal colony on Sakhalin Island at his own expense to document the conditions of prisoners, "
            "walking 4,000 miles across Siberia to get there. "
            "He died of tuberculosis at 44 — and in that time produced work that is still studied and performed worldwide. "
            "'If you are afraid of loneliness, do not marry,' he wrote. "
            "'If you are afraid of the work, do not begin. If you begin, do not stop.'"
        ),
        "author": "Anton Chekhov, playwright and short story writer",
        "tone": "both",
        "theme": "hard work",
    },
    {
        "type": "story",
        "text": (
            "Kobe Bryant arrived at the gym at 4am. His trainer, Rob Roms, once showed up for a 6am session "
            "to find Kobe already drenched in sweat — he had been there since 4. "
            "He asked Kobe how many shots he had made that morning. "
            "Kobe said: '800.' "
            "He won five NBA championships. He was still watching game film on his phone when a helicopter "
            "took him to his daughter's basketball game on the morning he died. "
            "'Those times when you get up early and work hard, those times when you stay up late "
            "and work hard — that is actually the dream.' "
            "The work is not the path to the dream. The work is the dream."
        ),
        "author": "Kobe Bryant, five-time NBA champion",
        "tone": "sharp",
        "theme": "consistency",
    },
    {
        "type": "story",
        "text": (
            "Michael Jordan was cut from his high school varsity team as a sophomore. "
            "He went home, locked himself in his room, and cried. "
            "Then he used the embarrassment as fuel — arriving before anyone else, staying later. "
            "He said he pictured that rejection list every time he didn't want to train. "
            "He won six NBA championships and five MVP awards. "
            "He later said: 'I've failed over and over and over again in my life. And that is why I succeed.' "
            "Failure is not the opposite of success. It is the raw material."
        ),
        "author": "Michael Jordan, six-time NBA champion",
        "tone": "both",
        "theme": "resilience",
    },

    # ── NEW QUOTES ───────────────────────────────────────────────────────────
    {
        "type": "quote",
        "text": "Discipline is choosing between what you want now and what you want most.",
        "author": "Augusta F. Kantra",
        "tone": "sharp",
        "theme": "consistency",
    },
    {
        "type": "quote",
        "text": "The difference between ordinary and extraordinary is that little 'extra.'",
        "author": "Jimmy Johnson",
        "tone": "sharp",
        "theme": "hard work",
    },
    {
        "type": "quote",
        "text": "It is during our darkest moments that we must focus to see the light.",
        "author": "Aristotle",
        "tone": "warm",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "The only limit to our realization of tomorrow is our doubts of today.",
        "author": "Franklin D. Roosevelt",
        "tone": "both",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.",
        "author": "Ralph Waldo Emerson",
        "tone": "warm",
        "theme": "courage",
    },
    {
        "type": "quote",
        "text": "Life is not measured by the number of breaths we take, but by the moments that take our breath away.",
        "author": "Maya Angelou",
        "tone": "warm",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "One day or day one. You decide.",
        "author": "Paulo Coelho",
        "tone": "sharp",
        "theme": "finishing",
    },
    {
        "type": "quote",
        "text": "The only way out is through.",
        "author": "Robert Frost",
        "tone": "sharp",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "You are never too old to set another goal or to dream a new dream.",
        "author": "C.S. Lewis",
        "tone": "warm",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "Small steps in the right direction can turn out to be the biggest step of your life.",
        "author": "Ancient wisdom",
        "tone": "warm",
        "theme": "consistency",
    },
    {
        "type": "quote",
        "text": "If you want to fly, you have to give up everything that weighs you down.",
        "author": "Toni Morrison",
        "tone": "both",
        "theme": "courage",
    },
    {
        "type": "quote",
        "text": "No matter how you feel, get up, dress up, show up, and never give up.",
        "author": "Regina Brett",
        "tone": "sharp",
        "theme": "consistency",
    },
    {
        "type": "quote",
        "text": "Turn your wounds into wisdom.",
        "author": "Oprah Winfrey",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "You are braver than you believe, stronger than you seem, and smarter than you think.",
        "author": "A.A. Milne, Winnie the Pooh",
        "tone": "warm",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "The brick walls are there for a reason. They're not there to keep us out. They're there to give us a chance to show how badly we want something.",
        "author": "Randy Pausch, The Last Lecture",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "If you're presenting yourself with confidence, you can pull off pretty much anything.",
        "author": "Katy Perry",
        "tone": "sharp",
        "theme": "courage",
    },
    {
        "type": "quote",
        "text": "Nothing in life is to be feared, it is only to be understood.",
        "author": "Marie Curie",
        "tone": "both",
        "theme": "intellectual perseverance",
    },
    {
        "type": "quote",
        "text": "We keep moving forward, opening new doors, and doing new things, because we're curious.",
        "author": "Walt Disney",
        "tone": "warm",
        "theme": "creativity",
    },
    {
        "type": "quote",
        "text": "The future belongs to those who believe in the beauty of their dreams.",
        "author": "Eleanor Roosevelt",
        "tone": "warm",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "I am not a product of my circumstances. I am a product of my decisions.",
        "author": "Stephen Covey",
        "tone": "sharp",
        "theme": "hard work",
    },
    {
        "type": "quote",
        "text": "The question isn't who is going to let me; it's who is going to stop me.",
        "author": "Ayn Rand",
        "tone": "sharp",
        "theme": "courage",
    },
    {
        "type": "quote",
        "text": "Happiness is not something ready made. It comes from your own actions.",
        "author": "Dalai Lama",
        "tone": "warm",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "In order to carry a positive action we must develop here a positive vision.",
        "author": "Dalai Lama",
        "tone": "warm",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "It is not what happens to you, but how you respond to it that matters.",
        "author": "Epictetus",
        "tone": "sharp",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "The impediment to action advances action. What stands in the way becomes the way.",
        "author": "Marcus Aurelius",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "Dwell on the beauty of life. Watch the stars, and see yourself running with them.",
        "author": "Marcus Aurelius",
        "tone": "warm",
        "theme": "rest & recovery",
    },
    {
        "type": "quote",
        "text": "You have survived every difficult day so far. You are 100% successful at getting through hard days.",
        "author": "Anonymous",
        "tone": "warm",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "The first step is you have to say that you can.",
        "author": "Will Smith",
        "tone": "sharp",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "If you're going to be thinking anyway, you might as well think big.",
        "author": "Donald Trump... originally. But the sentiment is universal.",
        "tone": "sharp",
        "theme": "courage",
    },
    {
        "type": "quote",
        "text": "Tough times never last, but tough people do.",
        "author": "Robert H. Schuller",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "It's not about how hard you hit. It's about how hard you can get hit and keep moving forward.",
        "author": "Rocky Balboa (Sylvester Stallone)",
        "tone": "sharp",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "Success is not how high you have climbed, but how you make a positive difference to the world.",
        "author": "Roy T. Bennett",
        "tone": "warm",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "The best way to predict the future is to create it.",
        "author": "Abraham Lincoln",
        "tone": "sharp",
        "theme": "finishing",
    },
    {
        "type": "quote",
        "text": "Believe you can and you're halfway there.",
        "author": "Theodore Roosevelt",
        "tone": "warm",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "We generate fears while we sit. We overcome them by action.",
        "author": "Dr. Henry Link",
        "tone": "sharp",
        "theme": "courage",
    },
    {
        "type": "quote",
        "text": "Limitations live only in our minds. But if we use our imaginations, our possibilities become limitless.",
        "author": "Jamie Paolinetti",
        "tone": "warm",
        "theme": "creativity",
    },
    {
        "type": "quote",
        "text": "Whatever you are, be a good one.",
        "author": "Abraham Lincoln",
        "tone": "sharp",
        "theme": "hard work",
    },
    {
        "type": "quote",
        "text": "Spread love everywhere you go. Let no one ever come to you without leaving happier.",
        "author": "Mother Teresa",
        "tone": "warm",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "When you reach the end of your rope, tie a knot in it and hang on.",
        "author": "Franklin D. Roosevelt",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "If you look at what you have in life, you'll always have more. If you look at what you don't have, you'll never have enough.",
        "author": "Oprah Winfrey",
        "tone": "warm",
        "theme": "purpose",
    },
    {
        "type": "quote",
        "text": "Do not wait to strike till the iron is hot, but make it hot by striking.",
        "author": "William Butler Yeats",
        "tone": "sharp",
        "theme": "finishing",
    },
    {
        "type": "quote",
        "text": "The secret of success is to do the common things uncommonly well.",
        "author": "John D. Rockefeller",
        "tone": "sharp",
        "theme": "hard work",
    },
    {
        "type": "quote",
        "text": "There is nothing permanent except change.",
        "author": "Heraclitus",
        "tone": "both",
        "theme": "resilience",
    },
    {
        "type": "quote",
        "text": "The two hardest things to handle in life are failure and success.",
        "author": "Anonymous",
        "tone": "both",
        "theme": "self-doubt",
    },
    {
        "type": "quote",
        "text": "I'd rather attempt to do something great and fail than to attempt to do nothing and succeed.",
        "author": "Robert H. Schuller",
        "tone": "sharp",
        "theme": "courage",
    },
    {
        "type": "quote",
        "text": "Life is what we make it, always has been, always will be.",
        "author": "Grandma Moses",
        "tone": "warm",
        "theme": "purpose",
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
