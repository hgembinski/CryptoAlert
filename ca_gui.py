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
    cryptos = ["One", "Two", "Three", "Four", "Five"]
    list_font = font.Font(None, 25)
    settings.option_add("*TCombobox*Listbox*Font", list_font)
    cryptos = AutocompleteCombobox(settings, font = (None, 25), completevalues = cryptos)
    cryptos.place(x = 350, y = 125, anchor = "center")

    #update button
    update = Button(settings, bg = "#0042FF", activebackground = 'dodgerblue2', fg = "antiquewhite1", activeforeground = "antiquewhite1",
                text = "Update", relief = "raised", width = 6, font = (None, 15, "bold"))
    update.place(x = 600, y = 125, anchor = "center")

    #alert configuration
    alert_text_1 = Label(settings, text = "When the price...", bg = "azure", fg = "#000F46",
                font = (None, 30, "italic")).place(x = 150, y = 160)
    alert_text_2 = Label(settings, text = "Changes by ", bg = "azure", fg = "#000F46",
                font = (None, 22)).place(x = 250, y = 225)
    price_changes_by = Canvas(settings, bg = "light grey", width = 25, height = 25).place(x = 200, y = 231) #'changes by' toggle
    alert_text_3 = Label(settings, text = "Is ", bg = "azure", fg = "#000F46",
                font = (None, 22)).place(x = 250, y = 290)
    price_is = Canvas(settings, bg = "light grey", width = 25, height = 25).place(x = 200, y = 296) #'is' toggle
    
    alert_config_text = Label(settings, text = "Alert me by...", bg = "azure", fg = "#000F46",
                font = (None, 30, "italic")).place(x = 150, y = 365)
    sound_alert_text = Label(settings, text = "Playing a sound!", bg = "azure", fg = "#000F46",
                font = (None, 22)).place(x = 250, y = 425)
    play_sound = Canvas(settings, bg = "light grey", width = 25, height = 25).place(x = 200, y = 431) #'play sound' toggle
    email_alert_text = Label(settings, text = "Sending me an email!", bg = "azure", fg = "#000F46",
                font = (None, 22)).place(x = 250, y = 490)
    email = Entry(settings, font = (None, 22), relief = "sunken").place(x = 250, y = 530)
    send_email = Canvas(settings, bg = "light grey", width = 25, height = 25).place(x = 200, y = 496) #'send email' toggle

    #confirm button
    confirm = Button(settings, bg = "#0042FF", activebackground = 'dodgerblue2', fg = "antiquewhite1", activeforeground = "antiquewhite1",
                text = "Confirm", relief = "raised", width = 10, font = (None, 30, "bold"), command = lambda: settings_confirm(root, settings))
    confirm.place(x = 500, y = 650, anchor = "center")

    #cancel button
    cancel = Button(settings, bg = "#0042FF", activebackground = 'dodgerblue2', fg = "antiquewhite1", activeforeground = "antiquewhite1",
                text = "Cancel", relief = "raised", width = 10, font = (None, 30, "bold"), command = lambda: settings_cancel(root, settings))
    cancel.place(x = 200, y = 650, anchor = "center")

    return

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