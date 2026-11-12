# Userscript fuer den 3D-Irrgarten (irrgarten.mic) auf dem ESP2090 Studio
# Setzt die Farbmatrix und endet: Waende gelb, Boden blau (unten 8, 6, 4 LEDs).
# Einmal nach dem Einschalten des ESP starten ("Run"), die Matrix muss eingeschaltet sein ("LED on").
# Fuer weitere RUNs ist es nicht noetig. Nach einer Aenderung der Farben hier: noch einmal starten, dann RUN.
# Die Stirnwand faerbt das Programm selbst (oliv).

W = "gelb"       # Waende
B = "blau"       # Boden

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
