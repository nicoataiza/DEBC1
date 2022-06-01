import configparser

config = configparser.ConfigParser()
config.read('config.ini')

host = config['mysql']['host']
print(host)