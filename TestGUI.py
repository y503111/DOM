from tkinter import *
x1=int(0)
x2=int(0)
x3=int(0)
x4=int(0)
# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button anklickt
def LEDs_OBEN_LINKS():
    global x1
    if x1 == 0:
        LED_txt_OL.config(text="Ausschalten")
        x1=1
    else:
        LED_txt_OL.config(text="Einschalten")
        x1=0

def LEDs_OBEN_RECHTS():
    global x2
    if x2 == 0:
        LED_txt_OR.config(text="Ausschalten")
        x2=1
    else:
        LED_txt_OR.config(text="Einschalten")
        x2=0
    
def LEDs_UNTEN_LINKS():
    global x3
    if x3 == 0:
        LED_txt_UL.config(text="Ausschalten")
        x3=1
    else:
        LED_txt_UL.config(text="Einschalten")
        x3=0

def LEDs_UNTEN_RECHTS():
    global x4
    if x4 == 0:
        LED_txt_UR.config(text="Ausschalten")
        x4=1
    else:
        LED_txt_UR.config(text="Einschalten")
        x4=0


# Ein Fenster erstellen
fenster = Tk()
# Den Fenstertitle erstellen
fenster.title("Dom Beleuchtung")

# Label und Buttons erstellen.
LED_Button_OL = Button(fenster, text="LED 1 bis 15 Einschalten", command=LEDs_OBEN_LINKS)
LED_Button_OR = Button(fenster, text="LED 16 bis 30 Einschalten", command=LEDs_OBEN_RECHTS)
LED_Button_UL = Button(fenster, text="LED 31 bis 45 Einschalten", command=LEDs_UNTEN_LINKS)
LED_Button_UR = Button(fenster, text="LED 46 bis 60 Einschalten", command=LEDs_UNTEN_RECHTS)

LED_txt_OL = Label(fenster, text="Einschalten")
LED_txt_OR = Label(fenster, text="Einschalten")
LED_txt_UL = Label(fenster, text="Einschalten")
LED_txt_UR = Label(fenster, text="Einschalten")

info_label = Label(fenster, text="Ich bin eine Info:\n\Der Beenden Button schliesst das Programm.")

# Zuerst definieren wir die Grösse des Fensters
fenster.geometry("1024x600")
# Wir benutzen die absoluten Koordinaten um die Komponenten zu
# setzen und definieren deren Grösse
LED_Button_OL.place(x = 10, y = 55, width=250, height=50)
LED_txt_OL.place(x = 10, y = 5, width=250, height=50)
LED_Button_OR.place(x = 260, y = 55, width=250, height=50)
LED_txt_OR.place(x = 260, y = 5, width=250, height=50)
LED_Button_UL.place(x = 10, y = 355, width=250, height=50)
LED_txt_UL.place(x = 10, y = 405, width=250, height=50)
LED_Button_UR.place(x = 260, y = 355, width=250, height=50)
LED_txt_UR.place(x = 260, y = 405, width=250, height=50)


# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()
