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
]


def get_random_item() -> dict:
    return random.choice(ITEMS)


def get_item_by_tone(tone: str) -> dict:
    filtered = [i for i in ITEMS if i["tone"] in (tone, "both")]
    return random.choice(filtered) if filtered else get_random_item()


def get_item_by_theme(theme: str) -> dict:
    filtered = [i for i in ITEMS if i["theme"] == theme]
    return random.choice(filtered) if filtered else get_random_item()
