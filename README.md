# Public Instagram
usage: `python3 main.py -u username1 username2 -o json -e output.json`<br>
```
Extract data from a instagram profile

options:
  -h, --help            show this help message and exit
  -u USERS [USERS ...], --users USERS [USERS ...]
                        list of usernames
  -f FILE, --file FILE  file with usernames
  -e EXPORT, --export EXPORT
                        export data to file
  -i, --indent          indent json
  -v, --version         show program's version number and exit
```

Example: `python main.py -u cristiano leomessi -i`
<br>
<b>Output:<b>
```json
[
    {
        "username": "Cristiano Ronaldo",
        "followers": 539000000,
        "following": 539,
        "posts": 3363,
        "img": "https://scontent.cdninstagram.com/v/t51.2885-15/278931269_360124899498969_9006978846103417088_n.jpg?stp=dst-jpg_s100x100&_nc_cat=1&ccb=1-7&_nc_sid=8ae9d6&_nc_ohc=h665U0mkOtQAX_wjVuc&_nc_ht=scontent.cdninstagram.com&oh=00_AT84J_Urt_x4O8DHrGR0X81reKhnACsBeQ3Z9ZseD56bHA&oe=63384103",
        "url": "https://www.instagram.com/cristiano/"
    },
    {
        "username": "Leo Messi",
        "followers": 404000000,
        "following": 313,
        "posts": 913,
        "img": "https://scontent.cdninstagram.com/v/t51.2885-15/43818140_2116018831763532_3803033961098117120_n.jpg?stp=dst-jpg_s100x100&_nc_cat=1&ccb=1-7&_nc_sid=8ae9d6&_nc_ohc=80OQtr1mMxIAX_amPAO&_nc_ht=scontent.cdninstagram.com&oh=00_AT-SRUZ4BBZnys-XWxcN_Y2OuEnKD88eLiVOWcg6iKLlSQ&oe=6337C97F",
        "url": "https://www.instagram.com/leomessi/"
    }
]
```