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

def resize_font(root, current_font, label):
    font_size = current_font.cget("size")
    width = label.winfo_width()

    if width > 425:
        current_font.configure(size = font_size - 1)
        root.update()
        resize_font(root, current_font, label)

    if width < 400:
        current_font.configure(size = font_size + 1)
        root.update()
        resize_font(root, current_font, label)
    
    label.config(fg = "antiquewhite1") #actually show the text once it's properly sized