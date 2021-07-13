# Haiden Gembinski
# CryptoAlert
# Allows for real-time tracking of a selected cryptocurrency's USD price
# as well as configurable sound/email alrts once the price hits a custom threshold.
# Crypto choice, price alert threshold, and alert options can all be found under "settings".

from bs4 import BeautifulSoup
import requests
import pandas
import json
import time
import ca_gui
from ca_gui import *

#main function / main page of GUI
def crypto_alert():
    #settings
    coin = "None"
    price = 0
    alert_type = "None"
    alert_number = 0
    is_sound = False
    is_email = False
    email = ""

    #initial GUI setup
    root = tkinter.Tk()
    root.title("CryptoAlert")
    root.geometry("700x750")
    root.resizable(False, False)
    root.config(bg = "azure", highlightbackground = "#000F46", highlightcolor = "#000F46", highlightthickness = 10)

    #text elements
    title = Label(root, text = "CryptoAlert", bg = '#000F46', fg = "white", width = 12,
                font = (None, 40)).place(x = 350, y = 50, anchor = "s")
    cryptoname = Label(root, text = "No Coin Selected", bg = "azure", fg = "#000F46",
                font = (None, 35, "bold")).place(x = 350, y = 125, anchor = "center")

    #price ticker
    priceframe = Frame(root, bg = 'grey9', highlightbackground = "#000F46", highlightcolor = "#000F46",
                highlightthickness = 12.5, relief = "flat", height = 200, width = 500).place(x = 350, y = 300, anchor = "center")
    price = Label(priceframe, text = "$00000.00", bg = "grey9",fg = "antiquewhite1", width = 8,
                font = (None, 75)).place(x = 350, y = 300, anchor = "center")

    #alert display
    alert_display = Label(root, text = "No Alert Set!", bg = "azure", fg = "#000F46",
                font = (None, 25)).place(x = 350, y = 430, anchor = "center")
    sound_display = Label(root, text = "I will not play a sound!", bg = "azure", fg = "#000F46",
                font = (None, 25)).place(x = 350, y = 480, anchor = "center")
    email_display = Label(root, text = "I will not send an email!", bg = "azure", fg = "#000F46",
                font = (None, 25)).place(x = 350, y = 530, anchor = "center")
    email_address_display = Label(root, text = "", bg = "azure", fg = "#000F46",
                font = (None, 20)).place(x = 350, y = 570, anchor = "center")

    #buttons
    settings = Button(root, bg = "#0042FF", activebackground = "dodgerblue2", fg = "antiquewhite1", activeforeground = "antiquewhite1",
                text = "Settings", relief = "raised", width = 10, font = (None, 30, "bold"), 
                command = lambda: settings_screen(root, coin, price, alert_type, alert_number, is_sound, is_email, email))
    settings.place(x = 500, y = 650, anchor = "center")

    history = Button(root, bg = "#0042FF", activebackground = 'dodgerblue2', fg = "antiquewhite1", activeforeground = "antiquewhite1",
                text = "History", relief = "raised", width = 10, font = (None, 30, "bold"))
    history.place(x = 200, y = 650, anchor = "center")



    root.mainloop()

crypto_alert()
