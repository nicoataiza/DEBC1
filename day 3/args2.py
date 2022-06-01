import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--search_word', help='word for twitter search')
parser.add_argument('--google_search', default ="Google", help='word for twitter search')

args = parser.parse_args()
print(args.search_word)