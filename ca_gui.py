#Haiden Gembinski
#GUI class for CryptoAlert

import os
import tkinter
from tkinter import *
from tkinter import font
import tkinter.font
from tkinter import ttk
from ttkwidgets.autocomplete import AutocompleteCombobox
import ca_helpers
from ca_helpers import *

class ca_gui:
    def __init__(self, master, settings):
        #GUI setup
        self.master = master
        master.title("CryptoAlert")
        master.geometry("700x750")
        master.resizable(False, False)
        master.config(bg = "azure", highlightbackground = "#000F46", highlightcolor = "#000F46", highlightthickness = 10)

        self.title = Label(master, text = "CryptoAlert", bg = '#000F46', fg = "white", width = 12,
                    font = (None, 40)).place(x = 350, y = 50, anchor = "s")
        self.cryptoname = Label(master, text = "No Coin Selected", bg = "azure", fg = "#000F46", font = (None, 35, "bold"))
        self.cryptoname.place(x = 350, y = 125, anchor = "center")

        #price ticker
        self.priceframe = Frame(master, bg = 'grey9', highlightbackground = "#000F46", highlightcolor = "#000F46",
                    highlightthickness = 12.5, relief = "flat", height = 200, width = 500).place(x = 350, y = 300, anchor = "center")
        self.price_font = font.Font(size = 5)
        self.price = Label(master, text = "$0000.00", bg = "grey9", fg = "grey9", font = self.price_font)
        self.price.place(x = 350, y = 300, anchor = "center")
        master.update()

        #alert display
        self.alert_display = Label(master, text = "No Alert Set!", bg = "azure", fg = "#000F46",font = (None, 25))
        self.alert_display.place(x = 350, y = 430, anchor = "center")
                    
        self.sound_display = Label(master, text = "I will not play a sound!", bg = "azure", fg = "#000F46",font = (None, 25))
        self.sound_display.place(x = 350, y = 480, anchor = "center")

        self.email_display = Label(master, text = "I will not send an email!", bg = "azure", fg = "#000F46", font = (None, 25))
        self.email_display.place(x = 350, y = 530, anchor = "center")

        self.email_address_display = Label(master, text = "", bg = "azure", fg = "#000F46",font = (None, 20))
        self.email_address_display.place(x = 350, y = 570, anchor = "center")

        #buttons
        self.settings_button = Button(self.master, bg = "#0042FF", activebackground = "dodgerblue2", fg = "antiquewhite1", 
                    activeforeground = "antiquewhite1", text = "Settings", relief = "raised", width = 10, font = (None, 30, "bold"), 
                    command = lambda: self.show_settings_screen(master, settings))
        self.settings_button.place(x = 500, y = 650, anchor = "center")

        self.history_button = Button(self.master, bg = "#0042FF", activebackground = 'dodgerblue2', fg = "antiquewhite1", 
                    activeforeground = "antiquewhite1", text = "History", relief = "raised", width = 10, font = (None, 30, "bold"))
        self.history_button.place(x = 200, y = 650, anchor = "center")

    def set_crypto(self, new_name):
        self.cryptoname.config(text = new_name)

    def set_price(self, new_price):
        self.price.config(text = new_price)

    def set_price_color(self, color):
        self.price.config(fg = color)
        
    def set_alert_text(self, new_text):
        self.alert_display.config(text = new_text)

    def set_sound_alert_text(self, new_text):
        self.sound_display.config(text = new_text)

    def set_email_alert_text(self, new_text):
        self.email_display.config(text = new_text)

    def set_email_text(self, new_text):
        self.email_address_display.config(text = new_text)

    def get_font(self):
        return self.price_font

    def set_font_size(self, new_size):
        self.price_font.config(size = new_size)

    def get_price_label(self):
        return self.price

    def show_settings_screen(self, master, settings):
        #construct dict of coins
        csv_file = "cryptos.csv"
        coin_dict = csv_to_dict(csv_file)
        coin_list = []
        for key in coin_dict.keys():
            coin_list.append(coin_dict[key][0] + " - " + key)
        
        if settings.get_coin() != "": #for displaying coin in combobox entry field
            coin_name = settings.get_symbol() + " - " + settings.get_coin()
        else:
            coin_name = ""

        #GUI
        settings_gui = tkinter.Toplevel(master)
        settings_gui.title("CryptoAlert Settings")
        settings_gui.resizable(False, False)
        settings_gui.grab_set()

        x = master.winfo_x()
        y = master.winfo_y()
        h = master.winfo_height()
        w = master.winfo_width()
        settings_gui.geometry("%dx%d+%d+%d" % (w, h, x, y))
        settings_gui.config(bg = "azure", highlightbackground = "#000F46", highlightcolor = "#000F46", highlightthickness = 10)

        #title
        title = Label(settings_gui, text = "Settings", bg = '#000F46', fg = "white", width = 12,
                    font = (None, 40)).place(x = 350, y = 50, anchor = "s")

        #drop down list
        list_title = Label(settings_gui, text = "Select Coin To Track ", bg = "azure", fg = "#000F46",
                    font = (None, 25)).place(x = 350, y = 75, anchor = "center")
        list_font = font.Font(None, 25)
        settings_gui.option_add("*TCombobox*Listbox*Font", list_font)
        cryptos = AutocompleteCombobox(settings_gui, width = 30, font = (None, 15), completevalues = coin_list)
        cryptos.place(x = 350, y = 125, anchor = "center")
        cryptos.set(coin_name)

        #update button
        update = Button(settings_gui, bg = "#0042FF", activebackground = 'dodgerblue2', fg = "antiquewhite1", activeforeground = "antiquewhite1",
                    text = "Update", relief = "raised", width = 6, font = (None, 15, "bold"))
        update.place(x = 600, y = 125, anchor = "center")

        #alert options
        alert_price_text = Label(settings_gui, text = "When the price...", bg = "azure", fg = "#000F46",
                    font = (None, 30, "italic")).place(x = 150, y = 160)
        changes_text = Label(settings_gui, text = "Changes by ", bg = "azure", fg = "#000F46",
                    font = (None, 22)).place(x = 250, y = 225)
        changes_percent = Label(settings_gui, text = "%", bg = "azure", fg = "#000F46",
                    font = (None, 22)).place(x = 490, y = 225)
        changes_number = Entry(settings_gui, font = (None, 20), width = 4, relief = "sunken")
        changes_number.place(x = 425, y = 227)
        if settings.get_alert_type() == "Percent":
            changes_number.insert(0, settings.get_alert_number())

        is_text = Label(settings_gui, text = "Is ", bg = "azure", fg = "#000F46",
                font = (None, 22)).place(x = 250, y = 292)
        is_choices = ["=", "<", ">"]
        is_choice_dropdown = AutocompleteCombobox(settings_gui, width = 2, font = (None, 20), justify = "center",
                    completevalues = is_choices, state = "readonly")
        is_choice_dropdown.place(x = 300, y = 294)
        if settings.get_alert_sign() != "N/A":
            is_choice_dropdown.set(settings.get_alert_sign())
        to_than_text = Label(settings_gui, text = "  to", bg = "azure", fg = "#000F46",
                justify = "center", font = (None, 22))
        to_than_text.place(x = 375, y = 292)

        #changes text to to/than depending on the sign selected in dropdown
        def to_than_change(event):
            if is_choice_dropdown.get() == "=":
                to_than_text.config(text = "  to")
            else:
                to_than_text.config(text = "than")

        is_choice_dropdown.bind("<<ComboboxSelected>>", to_than_change)
        if settings.get_alert_sign() == "=":
            to_than_text.config(text = "  to")
        elif settings.get_alert_sign() == "<" or ">":
            to_than_text.config(text = "than")

        is_sign = Label(settings_gui, text = "$", bg = "azure", fg = "#000F46",
                font = (None, 22)).place(x = 450, y = 292)
        is_number = Entry(settings_gui, font = (None, 20), width = 8, relief = "sunken")
        is_number.place(x = 475, y = 294)
        if settings.get_alert_type() == "Flat":
            is_number.insert(0, settings.get_alert_number())

        #alert type configurations
        alert_config_text = Label(settings_gui, text = "Alert me by...", bg = "azure", fg = "#000F46",
                font = (None, 30, "italic")).place(x = 150, y = 365)
        sound_alert_text = Label(settings_gui, text = "Playing a sound!", bg = "azure", fg = "#000F46",
                    font = (None, 22)).place(x = 250, y = 425)

        email_alert_text = Label(settings_gui, text = "Sending me an email!", bg = "azure", fg = "#000F46",
                    font = (None, 22)).place(x = 250, y = 490)
        email_address = Entry(settings_gui, font = (None, 20), relief = "sunken")
        email_address.place(x = 250, y = 530)
        if settings.get_email() != "N/A":
            email_address.insert(0, settings.get_email())

        #toggles
        #price 'changes by' toggle
        price_changes_by = Canvas(settings_gui, bg = "light grey", borderwidth = 0, 
                    highlightthickness = 5, highlightbackground = "light grey", width = 25, height = 25) #default on display
        price_changes_by.place(x = 200, y = 225)
        if settings.get_alert_type() == "Percent":
            price_changes_by.config(bg = "#000F46")


        #price 'is' toggle
        price_is = Canvas(settings_gui, bg = "light grey", borderwidth = 0, 
                    highlightthickness = 5, highlightbackground = "light grey", width = 25, height = 25)
        price_is.place(x = 200, y = 292)
        if settings.get_alert_type() == "Flat":
            price_is.config(bg = "#000F46")

        #alert 'play sound' toggle
        play_sound = Canvas(settings_gui, bg = "light grey", borderwidth = 0, 
                    highlightthickness = 5, highlightbackground = "light grey", width = 25, height = 25)
        play_sound.place(x = 200, y = 425)
        if settings.get_sound_status() == "True":
            play_sound.config(bg = "#000F46")

        #'send email' toggle
        send_email = Canvas(settings_gui, bg = "light grey", borderwidth = 0, 
                    highlightthickness = 5, highlightbackground = "light grey", width = 25, height = 25)
        send_email.place(x = 200, y = 490)
        if settings.get_email_status() == "True":
            send_email.config(bg = "#000F46")

        #toggle events
        def changes_by_toggle(event):
            if price_changes_by["background"] == "light grey":
                price_changes_by.config(bg = "#000F46")
                price_is.config(bg = "light grey")
            else:
                price_changes_by.config(bg = "light grey")
        price_changes_by.bind("<Button-1>", changes_by_toggle)

        def is_toggle(event):
            if price_is["background"] == "light grey":
                price_is.config(bg = "#000F46")
                price_changes_by.config(bg = "light grey")
            else:
                price_is.config(bg = "light grey")
        price_is.bind("<Button-1>", is_toggle)

        def sound_alert_toggle(event):
            if play_sound["background"] == "light grey":
                play_sound.config(bg = "#000F46")
            else:
                play_sound.config(bg = "light grey")
        play_sound.bind("<Button-1>", sound_alert_toggle)

        def email_alert_toggle(event):
            if send_email["background"] == "light grey":
                send_email.config(bg = "#000F46")
            else:
                send_email.config(bg = "light grey")
        send_email.bind("<Button-1>", email_alert_toggle)

        #confirm button
        confirm = Button(settings_gui, bg = "#0042FF", activebackground = 'dodgerblue2', fg = "antiquewhite1", activeforeground = "antiquewhite1",
                text = "Confirm", relief = "raised", width = 10, font = (None, 30, "bold"), 
                command = lambda: settings_confirm())
        confirm.place(x = 500, y = 650, anchor = "center")

        #Settings confirm function
        def settings_confirm():
            settings_file = "settings.txt"
            name = cryptos.get().split(" - ", 1) #split out the coin name, 2nd element is the "spelled out" name of the coin
            if len(name) > 1 and name[1] in coin_dict.keys() and name[1]!= "Update to load list of coins!":
                coin = name[1]
                symbol = coin_dict[name[1]][0]
                url = coin_dict[name[1]][1]
            else:
                print("Invalid coin") #TO-DO: CALL TO ERROR SCREEN HERE
                return

            if price_changes_by["background"] == "#000F46":
                alert_type = "Percent"
                alert_sign = "N/A"
                if float(changes_number.get()) > 0 and float(changes_number.get()) < 1000:
                    alert_number = float(changes_number.get())
                else:
                    print("Invalid changes number") #TO-DO: CALL TO ERROR SCREEN HERE

            elif price_is["background"] == "#000F46" and is_choice_dropdown != "":
                alert_type = "Flat"
                alert_sign = is_choice_dropdown.get()
                try:
                    alert_number = float(is_number.get())
                except ValueError: #TO-DO: CALL TO ERROR SCREEN HERE
                    print("Invalid Is number")
                    return
            else:
                print("Invalid alert") #TO-DO: CALL TO ERROR SCREEN HERE
                return

            if play_sound["background"] == "#000F46":
                is_sound = "True"
            else:
                is_sound = "False"
            
            if send_email["background"] == "#000F46":
                is_email = "True"
                test_email = email_address.get()
                if (check_email(test_email)):
                    email = email_address.get()
                else:
                    print("Invalid email") #TO-DO: CALL TO ERROR SCREEN HERE
                    return
            else:
                is_email = "False"
                email = "N/A"

            #save to file   
            with open(settings_file, "w+") as f:
                f.write(str(coin) + "\n" + symbol + "\n" + url + "\n" + str(alert_type) + "\n" + str(alert_sign) 
                + "\n" + str(alert_number) + "\n" +str(is_sound) + "\n" + str(is_email) + "\n" + str(email))

            #set the settings object values accordingly
            settings.new_settings(coin, symbol, url, alert_type, alert_sign, alert_number, is_sound, is_email, email)

            settings_gui.destroy()

        #cancel button
        cancel = Button(settings_gui, bg = "#0042FF", activebackground = 'dodgerblue2', fg = "antiquewhite1", activeforeground = "antiquewhite1",
                    text = "Cancel", relief = "raised", width = 10, font = (None, 30, "bold"), command = lambda: settings_cancel())
        cancel.place(x = 200, y = 650, anchor = "center")

        #settings cancel button function
        def settings_cancel():
            settings_gui.destroy()

    def show_history_screen(self):

        def history_back():
            return
        
        return

    def show_error_screen(self, message):
        
        def error_close():
            return

        return

        