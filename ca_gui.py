#Haiden Gembinski
#GUI functionality for CryptoAlert

import tkinter
from tkinter import *
from tkinter import font
from tkinter import ttk
from ttkwidgets.autocomplete import AutocompleteCombobox


#Settings screen display
def settings_screen(root):
    root.withdraw() #hide root
    settings = tkinter.Toplevel(root)
    settings.title("CryptoAlert Settings")

    x = root.winfo_x()
    y = root.winfo_y()
    h = root.winfo_height()
    w = root.winfo_width()
    settings.geometry("%dx%d+%d+%d" % (w, h, x, y))
    settings.config(bg = "azure", highlightbackground = "#000F46", highlightcolor = "#000F46", highlightthickness = 10)

    #title
    title = Label(settings, text = "Settings", bg = '#000F46', fg = "white", width = 12,
                font = (None, 40)).place(x = 350, y = 50, anchor = "s")

    #drop down list
    list_title = Label(settings, text = "Select Coin To Track ", bg = "azure", fg = "#000F46",
                font = (None, 25)).place(x = 350, y = 75, anchor = "center")
    cryptos = ["Update to load list of coins!"]
    list_font = font.Font(None, 25)
    settings.option_add("*TCombobox*Listbox*Font", list_font)
    cryptos = AutocompleteCombobox(settings, width = 22, font = (None, 22), completevalues = cryptos)
    cryptos.place(x = 350, y = 125, anchor = "center")

    #update button
    update = Button(settings, bg = "#0042FF", activebackground = 'dodgerblue2', fg = "antiquewhite1", activeforeground = "antiquewhite1",
                text = "Update", relief = "raised", width = 6, font = (None, 15, "bold"))
    update.place(x = 600, y = 125, anchor = "center")

    #alert configuration
    alert_price_text = Label(settings, text = "When the price...", bg = "azure", fg = "#000F46",
                font = (None, 30, "italic")).place(x = 150, y = 160)
    changes_text = Label(settings, text = "Changes by ", bg = "azure", fg = "#000F46",
                font = (None, 22)).place(x = 250, y = 225)
    changes_percent = Label(settings, text = "%", bg = "azure", fg = "#000F46",
                font = (None, 22)).place(x = 490, y = 225)
    changes_number = Entry(settings, font = (None, 20), width = 4, relief = "sunken").place(x = 425, y = 227)
    
    is_text = Label(settings, text = "Is ", bg = "azure", fg = "#000F46",
                font = (None, 22)).place(x = 250, y = 292)
    is_choices = ["=", "<", ">"]
    is_choice_dropdown = AutocompleteCombobox(settings, width = 2, font = (None, 20), justify = "center",
                completevalues = is_choices, state = "readonly")
    is_choice_dropdown.place(x = 300, y = 294)
    to_than_text = Label(settings, text = "to", bg = "azure", fg = "#000F46",
            justify = "center", font = (None, 22))
    to_than_text.place(x = 375, y = 292)

    #changes text to to/than depending on the sign selected in dropdown
    def to_than_change(eveny):
        if is_choice_dropdown.get() == "=":
            to_than_text.config(text = "  to")
        else:
            to_than_text.config(text = "than")

    is_choice_dropdown.bind("<<ComboboxSelected>>", to_than_change)
    is_sign = Label(settings, text = "$", bg = "azure", fg = "#000F46",
                font = (None, 22)).place(x = 450, y = 292)
    is_number = Entry(settings, font = (None, 20), width = 8, relief = "sunken").place(x = 475, y = 294)
    
    alert_config_text = Label(settings, text = "Alert me by...", bg = "azure", fg = "#000F46",
                font = (None, 30, "italic")).place(x = 150, y = 365)
    sound_alert_text = Label(settings, text = "Playing a sound!", bg = "azure", fg = "#000F46",
                font = (None, 22)).place(x = 250, y = 425)
    email_alert_text = Label(settings, text = "Sending me an email!", bg = "azure", fg = "#000F46",
                font = (None, 22)).place(x = 250, y = 490)
    email = Entry(settings, font = (None, 20), relief = "sunken")
    email.place(x = 250, y = 530)
    email.insert(0, "example@website.org")


    #toggles
    #price 'changes by' toggle
    price_changes_by = Canvas(settings, bg = "light grey", borderwidth = 0, 
                highlightthickness = 5, highlightbackground = "light grey", width = 25, height = 25)
    price_changes_by.place(x = 200, y = 225)

    #price 'is' toggle
    price_is = Canvas(settings, bg = "light grey", borderwidth = 0, 
                highlightthickness = 5, highlightbackground = "light grey", width = 25, height = 25)
    price_is.place(x = 200, y = 292)

    #alert 'play sound' toggle
    play_sound = Canvas(settings, bg = "light grey", borderwidth = 0, 
                highlightthickness = 5, highlightbackground = "light grey", width = 25, height = 25)
    play_sound.place(x = 200, y = 425)

    #'send email' toggle
    send_email = Canvas(settings, bg = "light grey", borderwidth = 0, 
                highlightthickness = 5, highlightbackground = "light grey", width = 25, height = 25)
    send_email.place(x = 200, y = 490)

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
    confirm = Button(settings, bg = "#0042FF", activebackground = 'dodgerblue2', fg = "antiquewhite1", activeforeground = "antiquewhite1",
                text = "Confirm", relief = "raised", width = 10, font = (None, 30, "bold"), command = lambda: settings_confirm(root, settings))
    confirm.place(x = 500, y = 650, anchor = "center")

    #cancel button
    cancel = Button(settings, bg = "#0042FF", activebackground = 'dodgerblue2', fg = "antiquewhite1", activeforeground = "antiquewhite1",
                text = "Cancel", relief = "raised", width = 10, font = (None, 30, "bold"), command = lambda: settings_cancel(root, settings))
    cancel.place(x = 200, y = 650, anchor = "center")



#Settings confirm button
def settings_confirm(root, settings):

    root.deiconify()
    settings.destroy()
    return

#settings cancel button
def settings_cancel(root, settings):

    root.deiconify()
    settings.destroy()
    return

#History screen display
def history_screen(root):

    return

#History back button
def history_back():

    return

#Error screen display
def error_screen(root):

    return