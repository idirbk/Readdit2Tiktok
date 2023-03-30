import requests


Subreddit = 'AskReddit'


url = f'https://www.reddit.com/r/{Subreddit}/top.json?limit=10'
headers = {'User-agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
data = response.json()

for post in data['data']['children']:
    print("##################################################################")
    print(post['data']['title'])

    print('--- COMMENTS ---')
    post_id = post['data']['id']
    comments_url = f'https://www.reddit.com/r/AskReddit/comments/{post_id}.json'
    response = requests.get(comments_url, headers=headers)
    comments_data = response.json()
    for comment in comments_data[1]['data']['children']:
        if 'data' in comment :
            if 'body' in comment['data'] :
                print(comment['data']['body'])
                print('----------------')
