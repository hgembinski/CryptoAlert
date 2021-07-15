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

#check validity of email
def check_email(email):
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    if (re.match(regex, email)):
        return True

    return False