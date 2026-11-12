# Maze2090

3D-Irrgarten für den Busch Microtronic 2090 mit dem [ESP2090 Studio](https://github.com/rab-berlin/ESP2090) (8x8-LED-Matrix mit Farben): Blick aus der Ich-Perspektive wie bei *3D Monster Maze*, bedient mit den Tasten des 2090.

- 255 Programmschritte, 1 frei
- Dateien: [irrgarten.mic](irrgarten.mic), das kommentierte Listing, und das Userscript [irrgarten_farben.py](irrgarten_farben.py) für die Farben
- Getestet im [Emulator2090](https://github.com/rab-berlin/Emulator2090), noch nicht am Gerät

## Spiel

- **Irrgarten:** 8x8 Räume, jedes Mal neu ausgewürfelt. Zwischen zwei Räumen gibt es immer genau einen Weg.
- **Start:** in einem zufälligen Raum mit zufälliger Blickrichtung.
- **Ausgang:** der Raum in der Südwest-Ecke. Ist er im Blick, hat der Boden direkt vor der Stirnwand ein dunkles Loch.
- **Geschafft:** Wer in den Ausgang geht, bekommt sofort einen neuen Irrgarten.

## Bild

- **Sichttiefe:** 3 Räume. Bleibt die Mitte dunkel, geht der Gang noch weiter.
- **Boden:** türkis, die untersten drei Zeilen mit 8, 6 und 4 LEDs.
- **Seitenwände:** weiß, in Spalte 1/8, 2/7 und 3/6 für den 1., 2. und 3. Raum. Eine Öffnung zur Seite bleibt dunkel.
- **Stirnwand:** dunkelblau, ein Quadrat in der Mitte mit 6, 4 oder 2 LEDs Kante, je nach Entfernung.

## Bedienung

| Taste | Wirkung |
|---|---|
| 1 | links drehen |
| 2 | einen Raum vor (vor einer Wand geschieht nichts) |
| 3 | rechts drehen |
| 0 | umdrehen |

Ein Blick braucht etwa 2,6 Sekunden, dann wartet das Programm auf die nächste Taste. Taster werden nicht gebraucht; Eingang 1 ist REQ der Matrix.

## Start

1. Matrix einschalten („LED on“ in der Weboberfläche).
2. Einmal nach dem Einschalten des ESP: das Userscript `irrgarten_farben.py` mit **Run** starten. Es setzt die Farben (Wände weiß, Boden türkis) und endet sofort.
3. RESET, `HALT` `NEXT` `00` `RUN`. Nach etwa 6 Sekunden steht der erste Blick.

Für jeden weiteren RUN reichen RESET und RUN: Das Programm holt die Farben selbst vom Stapel der Matrix zurück. Nur wenn zwischendurch ein anderes Programm den Farbstapel benutzt hat, den ESP neu starten und das Userscript noch einmal laufen lassen.

Die Matrix muss wach sein. Hat ein anderes Programm sie schlafen gelegt, wartet der Irrgarten, bis sie geweckt wird.

**Ohne Userscript** läuft das Programm auch und bleibt spielbar: Wände und Boden sind dann beide rot, die Standardfarbe der Matrix. Die Stirnwand ist weiter dunkelblau, das Loch am Ausgang weiter dunkel. So sieht es auch im Emulator2090 aus, der keine Userscripts kennt.

## Farben ändern

- **Wände und Boden:** im Userscript, `W = "weiss"` und `B = "tuerkis"`. Möglich sind die Farbnamen von `setColors`.
- **Stirnwand:** im Programm an Adresse 01, Befehl `1C8`. Die mittlere Ziffer ist die Farbnummer der Matrix (C = dunkelblau).

## Technik

- **Speicher:** 1 Bit je Raum in den 16 Speicherregistern M0-MF. Bit 1 heißt Durchgang nach Osten. Die Bits teilen jede Reihe in Stücke, und aus jedem Stück führt genau ein Durchgang nach Norden: in den ungeraden Reihen am Ostende, in den geraden am Westende. Dadurch zeigen die Winkel reihenweise abwechselnd nach links und rechts.
- **Zeichnen:** Am Start holt das Programm die letzte Sicherung der Farben vom Stapel der Matrix und legt sie wieder darauf. Je Blick holt das Programm sie zurück, sendet ein Bild im Blockmodus (Wände und Boden) und zeichnet die Stirnwand als Rechteck.
