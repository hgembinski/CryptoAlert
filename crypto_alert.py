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
    initial = ""
    counter = 0
    counter2 = 0
    start = ""
    #GUI init
    root = tkinter.Tk()
    gui = ca_gui(root, settings)


    def update():
        nonlocal settings, last_price, current_price, initial, counter, counter2, start
        counter = counter + 1

        if start == "":
            start = time.time()

        if settings.get_is_new():
            current_price = get_price(settings.get_url())
            set_ticker(root, settings, gui, current_price)
            set_alert_info(settings, gui)
            initial = current_price
            settings.set_is_new(False)
            counter = 60

        if counter > 60:
            counter = 0
            if last_price != current_price:
                last_price = current_price

            current_price = get_price(settings.get_url())
            
            if float(current_price.replace(",","")) > float(last_price.replace(",","")):
                gui.set_price_color("lime green")
            elif float(current_price.replace(",","")) < float(last_price.replace(",","")):
                gui.set_price_color("red")
            
            gui.set_price("$" + current_price)
            print("------------------------")
            print(counter2)
            print("Initial Price: " + initial)
            print("Current Price: " + current_price)
            print("Last Price: " + last_price)
            counter = counter + 1
            end = time.time()
            print("Elapsed time: " + str(end - start))
            start = time.time()
            end = 0
        
        root.after(500, update)


    update()
    root.mainloop()

def set_alert_info(settings, gui):
    if settings.get_alert_type() == "Percent":
        gui.set_alert_text("Alerting when the price changes by: " + str(settings.get_alert_number()) + "%!")
    elif settings.get_alert_type() == "Flat":
        if settings.get_alert_sign() == "=":
            phrase = "is equal to $"
        elif settings.get_alert_sign() == "<":
            phrase = "is less than $"
        elif settings.get_alert_sign() == ">":
            phrase = "is greater than $"
        gui.set_alert_text("Alerting when the price " + phrase + str(settings.get_alert_number()) + "!")

    if settings.get_sound_status() == "True":
        gui.set_sound_alert_text("I will play a sound!")
    elif settings.get_sound_status() == "False":
        gui.set_sound_alert_text("I will not play a sound!")

    if settings.get_email_status() == "True":
        gui.set_email_alert_text("I will send an email to:")
        gui.set_email_text(settings.get_email())
    elif settings.get_email_status() == "False":
        gui.set_email_alert_text("I will not send an email!")
        gui.set_email_text("")

def set_ticker(root, settings, gui, current_price):
    gui.set_crypto(settings.get_symbol() + " - " + settings.get_coin())
    gui.set_font_size(5)
    gui.set_price("$" + current_price)
    root.update()
    resize_font(root, gui.get_font(), gui.get_price_label())


crypto_alert()
