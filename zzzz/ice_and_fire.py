# !usr/bin/env python3

import requests

AOIF = 'https://www.anapioficeandfire.com/api'

def main():
    ## Send HTTPS GET to the API of ICE and Fire
    gotresp = requests.get(AOIF)

    ## Decode the response
    got_dj = gotresp.json()

    ## print the response
    print(got_dj)
    
    ## display only the keys within
    ## the dictionary by using dict.keys()
    ## great for seeing what keys are available for lookup
    print(got_dj.keys())
    

if __name__ == "__main__":
    main()

