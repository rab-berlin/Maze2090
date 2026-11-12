# Userscript fuer den 3D-Irrgarten (irrgarten.mic) auf dem ESP2090 Studio
# Setzt die Farben und endet: Seitenwaende weiss, Boden blau, beide zur Ferne in drei Stufen dunkler,
#   Stirnwand dunkles Gelb.
# Einmal nach dem Einschalten des ESP starten ("Run"), die Matrix muss eingeschaltet sein ("LED on").
# Fuer weitere RUNs ist es nicht noetig. Nach einer Aenderung der Farben hier: noch einmal starten, dann RUN.
#
# setColors kennt nur zehn Farbnamen. Deshalb legt das Script eigene Farbwerte (r, g, b) auf einige
# dieser Namen. Das gilt bis zum Neustart des ESP, auch fuer andere Programme.
# Die Stirnwand zeichnet das Programm mit Farbe 13 (Vorgabe: oliv), das Loch am Ausgang mit 0 (schwarz).

WAND = ((10, 10, 10), (6, 6, 6), (3, 3, 3))     # nah, mittel, fern
BODEN = ((0, 0, 10), (0, 0, 6), (0, 0, 4))      # nah, mittel, fern (nicht dunkler: sonst sieht man das Loch kaum)
STIRNWAND = (6, 6, 0)

setPalette(9, WAND[0])          # "weiss"
setPalette(8, WAND[1])          # "magenta"
setPalette(7, WAND[2])          # "violett"
setPalette(6, BODEN[0])         # "blau"
setPalette(5, BODEN[1])         # "tuerkis"
setPalette(4, BODEN[2])         # "gruen"
setPalette(13, STIRNWAND)       # Farbe 13 (oliv), nur im Programm benutzt

W1, W2, W3 = "weiss", "magenta", "violett"     # Waende nah, mittel, fern
B1, B2, B3 = "blau", "tuerkis", "gruen"        # Boden nah, mittel, fern
_ = "schwarz"                                  # hier leuchtet nur die Stirnwand, Farbe egal

farben = [
    [W1, _,  _,  _,  _,  _,  _,  W1],
    [W1, W2, _,  _,  _,  _,  W2, W1],
    [W1, W2, W3, _,  _,  W3, W2, W1],
    [W1, W2, W3, _,  _,  W3, W2, W1],
    [W1, W2, W3, _,  _,  W3, W2, W1],
    [W1, W2, B3, B3, B3, B3, W2, W1],
    [W1, B2, B2, B2, B2, B2, B2, W1],
    [B1, B1, B1, B1, B1, B1, B1, B1],
]

setColors([c for zeile in farben for c in zeile])
log("Irrgarten: Farben gesetzt")
