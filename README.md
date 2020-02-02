# Yahoo finance scraper
This python script scraps "Open" and "Previous Close" values from Yahoo Finance Apple Inc.
 https://finance.yahoo.com/quote/AAPL?p=AAPL or any other company and save them in a local text file.

REQUIREMENTS:

Python V3, modules requests and re.

CONFIGURATION:

Open "yahoofinance.py", modify line number 38 to indicate desired full path of output file generated:

filename = "financevalues.txt"

EXECUTE:

To execute script under Windows, open console window and write:

python yahoofinance.py

