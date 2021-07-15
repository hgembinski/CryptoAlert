#Haiden Gembinski
#Helper functions for crypto alert
#(Mostly for handling files and input verification)

from os import path
import pandas as pd

#convert csv file to dict with name column as key
def csv_to_dict(file):
    if path.exists(file) and path.isfile(file):
        data = pd.read_csv(file, index_col = False, squeeze = False)
        dict = data.set_index("name").T.to_dict("list")
    else:
        dict = {"Update to load list of coins!": ("None", "None")}
    
    return dict

#check validity of coin input -> if it exists in the dictionary of coins
def check_coin(coin, dict):
    coin_name = coin.split(" ", 1) #get the spelled-out coin name from the string
    
    if coin_name in dict and coin_name != "Update to load list of coins!":
        return True
    else:
        return False