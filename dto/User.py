from dataclasses import dataclass
from datetime import datetime
import json

# serialize json

@dataclass
class User():
    username: str
    followers: int
    following: int
    posts: int
    img: str
    url: str
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # toCsv = lambda self: f"{self.username},{self.followers},{self.following},{self.posts},{self.img},{self.url},{self.date}"