# Userscript fuer den 3D-Irrgarten (irrgarten.mic) auf dem ESP2090 Studio
# Setzt die Farbmatrix und endet. Seitenwaende und Boden eines Raums bilden einen Ring in einer Farbe,
#   zur Ferne hin dunkler: weiss (1. Raum), gelb (2. Raum), orange (3. Raum).
# Einmal nach dem Einschalten des ESP starten ("Run"), die Matrix muss eingeschaltet sein ("LED on").
# Fuer weitere RUNs ist es nicht noetig. Nach einer Aenderung der Farben hier: noch einmal starten, dann RUN.
# Die Stirnwand (blau) und das Loch am Ausgang (schwarz) faerbt das Programm selbst.

N, M, F = "weiss", "gelb", "orange"        # Ring nah, mittel, fern
_ = "schwarz"                              # hier leuchtet nur die Stirnwand, Farbe egal

farben = [
    [N, _, _, _, _, _, _, N],
    [N, M, _, _, _, _, M, N],
    [N, M, F, _, _, F, M, N],
    [N, M, F, _, _, F, M, N],
    [N, M, F, _, _, F, M, N],
    [N, M, F, F, F, F, M, N],
    [N, M, M, M, M, M, M, N],
    [N, N, N, N, N, N, N, N],
]

setColors([c for zeile in farben for c in zeile])
log("Irrgarten: Farben gesetzt")
