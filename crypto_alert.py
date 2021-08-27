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

    if settings.get_coin() != "":
        current_price = get_price(settings.get_url())
        last_price = current_price
    else:
        current_price = ""
        last_price = ""
    initial = ""
    counter = 0
    counter2 = 0
    start = ""

    #GUI init
    root = tkinter.Tk()
    gui = ca_gui(root, settings)


    def update():
        nonlocal settings, current_price, last_price, initial, counter, counter2, start
        counter = counter + 1
        #print(counter)
        #print("-----")
        if start == "":
            start = time.time()

        if settings.get_coin() != "" :
            if settings.get_is_new():
                current_price = get_price(settings.get_url())
                set_ticker(root, settings, gui, current_price)
                set_alert_info(settings, gui)
                initial = current_price
                settings.set_is_new(False)
                counter = 61
            
            else:
                if counter > 60:
                    counter = 0

                    if current_price != "" and last_price != current_price:
                        last_price = current_price

                    current_price = get_price(settings.get_url())

                    if alert_check(settings, initial, current_price):
                        print("Alert!")
                        to_history('history.txt', '{month}/{day}/{year},{time},{symbol},${price},{email_sent}'.format(month = date.today().month, day = date.today().day,
                            year = date.today().year, time = strftime("%H:%M:%S", localtime()), symbol = settings.get_symbol(), price = current_price,
                            email_sent = settings.get_email_status()))
                        gui.show_alert_screen(root, settings, initial)
                        
                        settings.blank_settings()
                        delete_file(settings_file)
                        gui.default_display()

                    elif current_price != "":
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
                        counter2 = counter2 + 1
                        end = time.time()
                        print("Elapsed time: " + str(end - start))
                        start = time.time()
                        end = 0
        root.after(500, update)


    update()
    root.mainloop()

crypto_alert()
