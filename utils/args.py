import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Extract data from a instagram profile', usage='python3 main.py -u username1 username2 -o json -e output.json')
    parser.add_argument("-u", "--users", help="list of usernames", nargs='+')
    parser.add_argument("-f", "--file", help="file with usernames")
    parser.add_argument("-e", "--export", help='export data to file')
    parser.add_argument("-i", "--indent", help='indent json', action='store_true')
    parser.add_argument("-v", "--version", action='version', version='%(prog)s 1.0')
    args = parser.parse_args()

    if args.users:
      users = ['https://www.instagram.com/' + user + '/' for user in args.users]
    elif args.file:
      with open(args.file) as f:
        users = f.read().splitlines()
    else:
      parser.print_help()
      exit()

    return {
      'links': users,
      'export': args.export,
      'indent': args.indent
    }
