import requests
import sys
import json


def main():
    if len(sys.argv) < 2:
        sys.exit('Missing command-line argument ')
    try:
        bitcoin_num = float(sys.argv[1])
        multiplier = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()['bpi']['USD']['rate']
        list1 = multiplier.split(',')
        multiplier = float(''.join(list1)) * bitcoin_num
        
        print(f"${multiplier:,.4f}")
        
    except (requests.RequestException , ValueError ):
        sys.exit('Command-line argument is not a number ')
main()
