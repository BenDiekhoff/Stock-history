import yfinance as yf
import pandas as pd
import csv, json

jsonDict = {}

#Useful if you want to print the entire dataframe instead of the head and tail
pd.set_option("display.max_rows", None, "display.max_columns", None)

with open("nasdaqSymbols.txt","r") as f:
    symbols = f.read().splitlines()

for symbol in symbols:
    csvPath = f"CSVstonks/{symbol}.csv"
    jsonPath = f"JSONstonks/{symbol}.json"
    
    #Creates a dataframe from yahoo finance
    data = yf.download(symbol, start="1980-01-01", end="2021-01-01")
    #Puts data from dataframe in a csv and json file
    if not data.empty:
        """to_csv didn't like the PRN symbol so I removed it from the
        nasdaq lists"""
        data.to_csv(csvPath)    
        
        """for some reason a lot of the dataframes don't play nice with the
        to_json function and the program permanently hangs"""
        #data.to_json (jsonPath,indent=4, date_format='iso', date_unit='s') 
            
# print(type(data))
# print(data)


