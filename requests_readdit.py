
import praw

reddit = praw.Reddit(client_id='kcsMkzolc0ZCRAMvz7di-w',
                     client_secret='6yop0cRbeQPRBj4_mSn3Qf55aXL9Ig',
                     user_agent='Mozilla/5.0')

subreddit = reddit.subreddit('LetsNotMeet')
hot_posts = subreddit.hot(limit=10)

for post in hot_posts:
    print(post.title)
    print('Score:', post.score)
    print('URL:', post.url)
    print('id:', post.id)
    print('text: \n', post.selftext)
    print('date', post.created_utc)
    

    
