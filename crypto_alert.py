# Haiden Gembinski
# CryptoAlert
# Allows for real-time tracking of a selected cryptocurrency's USD price
# as well as configurable sound/email alrts once the price hits a custom threshold.
# Crypto choice, price alert threshold, and alert options can all be found under "settings".


import ca_gui
from ca_gui import *
import ca_scraping
from ca_scraping import *
import ca_settings
from ca_settings import *
import time

#main function / main page of GUI
def crypto_alert():
    settings_file = "settings.txt"
    settings = ca_settings(settings_file)
    current_price = get_price(settings.get_url())
    last_price = ""
    color = "white"
    counter = 0

    #GUI init
    root = tkinter.Tk()
    gui = ca_gui(root, settings)

    gui.set_crypto(settings.get_symbol() + " - " + settings.get_coin())
    gui.set_price("$" + current_price)
    resize_font(root, gui.get_font(), gui.get_price_label())

    if settings.get_alert_type() == "Percent":
        gui.set_alert_text("Alerting when the price changes by: " + settings.get_alert_number() + "%!")
    elif settings.get_alert_type() == "Flat":
        if settings.get_alert_sign() == "=":
            phrase = "is equal to $"
        elif settings.get_alert_sign() == "<":
            phrase = "is less than $"
        elif settings.get_alert_sign() == ">":
            phrase = "is greater than $"

        gui.set_alert_text("Alerting when the price " + phrase + settings.get_alert_number() + "!")

    if settings.get_sound_status() == "True":
        gui.set_sound_alert_text("I will play a sound!")
    
    if settings.get_email_status() == "True":
        gui.set_email_alert_text("I will send an email to:")
        gui.set_email_text(settings.get_email())


    def update():
        nonlocal last_price, current_price, color, counter
        if last_price != current_price:
            last_price = current_price

        current_price = get_price(settings.get_url())
        
        if float(current_price) > float(last_price):
            gui.set_price_color("lime green")
            color = "green"
        elif float(current_price) < float(last_price):
            color = "red"
            gui.set_price_color("red")
        
        gui.set_price("$" + current_price)
        print(counter)
        print("Current Price: " + current_price)
        print("Last Price: " + last_price)
        print("Color: " + color)
        print("------------------------")
        counter = counter + 1
        root.after(30000, update)


    update()
    root.mainloop()

crypto_alert()
