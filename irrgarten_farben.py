# Userscript fuer den 3D-Irrgarten (irrgarten.mic) auf dem ESP2090 Studio
# Setzt die Farbmatrix und endet: Waende weiss, Boden tuerkis (unten 8, 6, 4 LEDs).
# Vor jedem RUN des Irrgartens starten ("Run"), die Matrix muss eingeschaltet sein ("LED on").
# Die Stirnwand faerbt das Programm selbst (dunkelblau).

W = "weiss"      # Waende
B = "tuerkis"    # Boden

farben = [
    [W, W, W, W, W, W, W, W],
    [W, W, W, W, W, W, W, W],
    [W, W, W, W, W, W, W, W],
    [W, W, W, W, W, W, W, W],
    [W, W, W, W, W, W, W, W],
    [W, W, B, B, B, B, W, W],
    [W, B, B, B, B, B, B, W],
    [B, B, B, B, B, B, B, B],
]

setColors([c for zeile in farben for c in zeile])
log("Irrgarten: Farben gesetzt")
