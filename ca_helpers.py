#Haiden Gembinski
#Helper functions for crypto alert
#(Mostly for handling files and input verification)

import re
from os import path, remove
import pandas as pd
import winsound
from winsound import *

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

#delete file
def delete_file(file):
    if path.exists(file) and path.isfile(file):
        remove(file)

#resize font to fit ticker frame
def resize_font(root, current_font, label):
    if label.cget("text") == "":
        return

    font_size = current_font.cget("size")
    width = label.winfo_width()

    label.config(fg = label.cget("bg"))

    if width > 400:
        current_font.configure(size = font_size - 1)
        root.update()
        resize_font(root, current_font, label)

    if width < 370:
        current_font.configure(size = font_size + 1)
        root.update()
        resize_font(root, current_font, label)
    
    label.config(fg = "antiquewhite1") #actually show the text once it's properly sized

#returns true if current_price meets the criteria to fire an alert
def alert_check(settings, initial_price, current_price):
    if initial_price != "" and initial_price != "0":
        price = float(current_price.replace(",",""))

        if settings.get_alert_type() == "Percent":
            initial = float(initial_price.replace(",",""))
            percent = float(settings.get_alert_number()) / 100
            bound = initial * percent

            if price >= (initial + bound) or price <= (initial - bound):
                return True

        elif settings.get_alert_type() == "Flat":
            if settings.get_alert_sign() == "<":
                if price < float(settings.get_alert_number().replace(",","")):
                    return True

            elif settings.get_alert_sign() == ">":
                if price > float(settings.get_alert_number().replace(",","")):
                    return True

            return

        return False

#writes the alert info to top of history file, adjusting current entries as needed
def to_history(file, entry):
    if path.exists(file) and path.isfile(file): #if existing history file
        with open(file, "r") as f:
            history_array = [entry]
            
            for line in f:
                history_array.append(line.strip())

            while len(history_array) < 13:
                history_array.append('-,-,-,-,-')  #fill lines with dashes if less than ten entries

            while len(history_array) > 13:
                history_array.pop() #remove the last entry if there is more than ten entries

        with open(file, 'w') as f:
            for line in history_array:
                f.write(line + "\n")

    else:
        with open(file, "w") as f:
            history_array = [entry]

            while len(history_array) < 13:
                history_array.append('-,-,-,-,-')
            
            for line in history_array:
                f.write(line + "\n")





def play_sound():
    Beep(440, 200)
    Beep(440, 100)
    Beep(440, 100)
    Beep(494, 600)