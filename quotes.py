import random

QUOTES = [
    {
        "text": "Between stimulus and response there is a space. In that space is our power to choose our response. In our response lies our growth and our freedom.",
        "author": "Viktor E. Frankl",
        "theme": "resilience",
    },
    {
        "text": "You don't have to control your thoughts. You just have to stop letting them control you.",
        "author": "Dan Millman",
        "theme": "personal growth",
    },
    {
        "text": "The curious paradox is that when I accept myself just as I am, then I can change.",
        "author": "Carl Rogers",
        "theme": "psychology",
    },
    {
        "text": "We are more often frightened than hurt; and we suffer more from imagination than from reality.",
        "author": "Seneca",
        "theme": "resilience",
    },
    {
        "text": "Do not judge me by my successes, judge me by how many times I fell down and got back up again.",
        "author": "Nelson Mandela",
        "theme": "resilience",
    },
    {
        "text": "What lies behind us and what lies before us are tiny matters compared to what lies within us.",
        "author": "Ralph Waldo Emerson",
        "theme": "personal growth",
    },
    {
        "text": "The greatest discovery of my generation is that a human being can alter his life by altering his attitudes.",
        "author": "William James",
        "theme": "psychology",
    },
    {
        "text": "Hardships often prepare ordinary people for an extraordinary destiny.",
        "author": "C.S. Lewis",
        "theme": "resilience",
    },
    {
        "text": "Growth is painful. Change is painful. But nothing is as painful as staying stuck somewhere you don't belong.",
        "author": "Mandy Hale",
        "theme": "personal growth",
    },
    {
        "text": "The only journey is the one within.",
        "author": "Rainer Maria Rilke",
        "theme": "personal growth",
    },
    {
        "text": "You must do the things you think you cannot do.",
        "author": "Eleanor Roosevelt",
        "theme": "resilience",
    },
    {
        "text": "In the middle of difficulty lies opportunity.",
        "author": "Albert Einstein",
        "theme": "resilience",
    },
    {
        "text": "Knowing yourself is the beginning of all wisdom.",
        "author": "Aristotle",
        "theme": "psychology",
    },
    {
        "text": "The privilege of a lifetime is to become who you truly are.",
        "author": "Carl Jung",
        "theme": "psychology",
    },
    {
        "text": "Out of your vulnerabilities will come your strength.",
        "author": "Sigmund Freud",
        "theme": "psychology",
    },
    {
        "text": "Rock bottom became the solid foundation on which I rebuilt my life.",
        "author": "J.K. Rowling",
        "theme": "resilience",
    },
    {
        "text": "The most common form of despair is not being who you are.",
        "author": "Søren Kierkegaard",
        "theme": "personal growth",
    },
    {
        "text": "We cannot solve our problems with the same thinking we used when we created them.",
        "author": "Albert Einstein",
        "theme": "psychology",
    },
    {
        "text": "Life doesn't get easier or more forgiving; we get stronger and more resilient.",
        "author": "Steve Maraboli",
        "theme": "resilience",
    },
    {
        "text": "The wound is the place where the Light enters you.",
        "author": "Rumi",
        "theme": "personal growth",
    },
]


def get_random_quote() -> dict:
    return random.choice(QUOTES)


def get_quote_by_theme(theme: str) -> dict:
    themed = [q for q in QUOTES if q["theme"] == theme]
    return random.choice(themed) if themed else get_random_quote()
