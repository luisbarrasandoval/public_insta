from bs4 import BeautifulSoup
from dto.User import User
import requests

index_data = {
  'title': 15,
  'img': 14,
  'description': 16,
  'link': 17,
}

def instaNumberToNumber(number):
    number = number.replace(',', '')
    if number[-1] == 'k' or number[-1] == 'K':
        return int(float(number[:-1]) * 1000)
    elif number[-1] == 'm' or number[-1] == 'M':
        return int(float(number[:-1]) * 1000000)
    else:
        return int(number)


def get(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    followers = soup.find('meta', property='og:description').get('content').split(' ')[0]
    following = soup.find('meta', property='og:description').get('content').split(' ')[2]
    posts = soup.find('meta', property='og:description').get('content').split(' ')[4]

    

    user = User(
        username=soup.find('meta', property='og:title').get('content').split(' (@')[0],
        followers=instaNumberToNumber(followers),
        following=instaNumberToNumber(following),
        posts=instaNumberToNumber(posts),
        img=soup.find('meta', property='og:image').get('content'),
        url=soup.find('meta', property='og:url').get('content')
    )
    return user
    