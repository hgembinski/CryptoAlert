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
                highlightthickness = 12.5, relief = "flat", height = 200, width = 410).place(x = 350, y = 300, anchor = "center")
    price = Label(priceframe, text = "$0.0000", bg = "grey9",fg = "lime green", font = (None, 75)).place(x = 350, y = 300, anchor = "center")

    #buttons
    settings = Button(root, bg = "#0042FF", activebackground = "dodgerblue2", fg = "antiquewhite1", activeforeground = "antiquewhite1",
                text = "Settings", relief = "raised", width = 10, font = (None, 30, "bold"), command = lambda: settings_screen(root))
    settings.place(x = 350, y = 495, anchor = "center")

    history = Button(root, bg = "#0042FF", activebackground = 'dodgerblue2', fg = "antiquewhite1", activeforeground = "antiquewhite1",
                text = "History", relief = "raised", width = 10, font = (None, 30, "bold"))
    history.place(x = 350, y = 620, anchor = "center")



    root.mainloop()

crypto_alert()
