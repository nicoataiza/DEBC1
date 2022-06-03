import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--source', help ='Indicate what source of information', default='reports')
parser.add_argument('--date', help ='date for querying data')
args = parser.parse_args()

#check
print(args.source)
print(args.date)
print(args)