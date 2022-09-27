from extractors import public
from utils.args import get_args
import json

if __name__ == "__main__":
  arg = get_args()
  indent = 4 if arg['indent'] else None
  users = map(public.get, arg['links'])
  if arg['export']:
    with open(arg['export'], 'w') as f:
      f.write(json.dumps([user.__dict__ for user in users], indent=indent))
  else:
    print(json.dumps([user.__dict__ for user in users], indent=indent))