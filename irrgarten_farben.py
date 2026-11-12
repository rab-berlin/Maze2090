# Userscript fuer den 3D-Irrgarten (irrgarten.mic) auf dem ESP2090 Studio
# Setzt die Farbmatrix und endet. Die Farben werden mit der Entfernung dunkler:
#   Seitenwaende gelb, orange, rot (1., 2., 3. Raum), Boden weiss, tuerkis, blau (unten 8, 6, 4 LEDs).
# Einmal nach dem Einschalten des ESP starten ("Run"), die Matrix muss eingeschaltet sein ("LED on").
# Fuer weitere RUNs ist es nicht noetig. Nach einer Aenderung der Farben hier: noch einmal starten, dann RUN.
# Die Stirnwand (violett) und das Loch am Ausgang (schwarz) faerbt das Programm selbst.

G, O, R = "gelb", "orange", "rot"          # Seitenwaende: nah, mittel, fern
W, T, B = "weiss", "tuerkis", "blau"       # Boden: nah, mittel, fern
_ = "schwarz"                              # hier leuchtet nur die Stirnwand, Farbe egal

farben = [
    [G, _, _, _, _, _, _, G],
    [G, O, _, _, _, _, O, G],
    [G, O, R, _, _, R, O, G],
    [G, O, R, _, _, R, O, G],
    [G, O, R, _, _, R, O, G],
    [G, O, B, B, B, B, O, G],
    [G, T, T, T, T, T, T, G],
    [W, W, W, W, W, W, W, W],
]

setColors([c for zeile in farben for c in zeile])
log("Irrgarten: Farben gesetzt")
