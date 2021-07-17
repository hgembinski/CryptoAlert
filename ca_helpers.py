#Haiden Gembinski
#Helper functions for crypto alert
#(Mostly for handling files and input verification)

import re
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

#load settings from file and return them as a list
def load_settings(file):
    settings = []

    #defaults for settings variables
    coin = ""
    symbol = ""
    url = ""
    alert_type = ""
    alert_sign = "="
    alert_number = 0
    is_sound = "False"
    is_email = "False"
    email = ""

    if path.exists(file) and path.isfile(file): #if the settings file exists, update settings from file
        with open(file) as f:
            settings_list = f.read().splitlines()
            coin = settings_list[0]
            symbol = settings_list[1]
            url = settings_list[2]
            alert_type = settings_list[3]
            alert_sign = settings_list[4]
            alert_number = settings_list[5]
            is_sound = settings_list[6]
            is_email = settings_list[7]
            email = settings_list[8]

    settings.extend([coin, symbol, url, alert_type, alert_sign, alert_number, is_sound, is_email, email])
    return settings

#check validity of email
def check_email(email):
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    if (re.match(regex, email)):
        return True

    return False