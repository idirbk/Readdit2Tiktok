import praw
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Access environment variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
user_agent = os.getenv('USER_AGENT')

# Initialisez l'API Reddit avec vos informations d'authentification
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)


# Liste des subreddits choisis
subreddits = [
    "AskReddit",
    "nosleep",
    "tifu",
    "WritingPrompts",
    "ProRevenge",
    "LetsNotMeet",
    "talesfromtechsupport",
    "Glitch_in_the_Matrix",
    "UnresolvedMysteries",
    "creepy"
]

# Récupérez les 10 meilleures histoires de chaque subreddit choisi
for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)
    top_stories = subreddit.top(limit=10)

    print(f"--- Histoires populaires de r/{subreddit_name} ---")

    # Parcourez les histoires et affichez leur titre et leur contenu
    for story in top_stories:
        print('Titre:', story.title)
        print('Contenu:', story.selftext)
        print('---')
