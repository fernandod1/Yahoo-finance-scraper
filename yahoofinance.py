import re
import sys
import requests

# Copyright (c) 2020 Fernando
# Url: https://github.com/fernandod1/
# License: MIT

def writefile(filename, value):
    try:
        f= open(filename, "w+",  encoding="utf-8")
        f.write(value)
        f.close()
        print(f"Values saved in {filename} file.")
    except:
        print(f"Could not write to {filename} file.")

def scrapdata():
    headers = {
        "Referer": 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    r = requests.get(f"https://finance.yahoo.com/quote/AAPL?p=AAPL", headers=headers)    
    openvalue = re.search(r'\"AAPL\":{\"sourceInterval\":(.*?),\"regularMarketOpen\":{\"raw\":(.*?),\"', r.text)
    if openvalue is not None:
        openvalue = openvalue.group(2)
        print(f"OPEN: {openvalue}")
    else:
        openvalue = ""
        print("NO OPEN value found")
    previousvalue = re.search(r'\"summaryDetail\":{\"previousClose\":{\"raw\":(.*?),\"', r.text)
    if previousvalue is not None:
        previousvalue = previousvalue.group(1)
        print(f"PREVIOUS: {previousvalue}") 
    else:
        print("NO PREVIOUS value found")
        previousvalue = ""
    data = 'OPEN: '+str(openvalue)+'\nPREVIOUS: '+str(previousvalue)
    return data


def main():
    filename = "financevalues.txt"
    value = scrapdata()
    writefile(filename, value)

if __name__ == "__main__":

    main()

