import requests
import sys
import json
import emoji

def main():
    name = input('Input: ') 
    print(emoji.emojize(name , language = 'alias'))  

main()
