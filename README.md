# Maze2090

3D-Irrgarten für den Busch Microtronic 2090 mit dem [ESP2090 Studio](https://github.com/rab-berlin/ESP2090) (8x8-LED-Matrix mit Farben): Blick aus der Ich-Perspektive wie bei *3D Monster Maze*, bedient mit den Tasten des 2090.

- 256 Programmschritte, 0 frei
- Datei: [irrgarten.mic](irrgarten.mic), das kommentierte Listing
- Getestet im [Emulator2090](https://github.com/rab-berlin/Emulator2090), noch nicht am Gerät

## Spiel

- **Irrgarten:** 8x8 Räume, bei jedem Start neu ausgewürfelt. Zwischen zwei Räumen gibt es immer genau einen Weg.
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

Ein Blick braucht etwa 2,3 Sekunden, dann wartet das Programm auf die nächste Taste. Taster werden nicht gebraucht; Eingang 1 ist REQ der Matrix.

## Start

RESET, Matrix einschalten („LED on“ in der Weboberfläche, im Emulator2090 Taste `m`), `HALT` `NEXT` `00` `RUN`. Nach etwa 7 Sekunden steht der erste Blick. Die Matrix muss wach sein: Hat ein anderes Programm sie schlafen gelegt, wartet der Irrgarten, bis sie geweckt wird.

## Farben ändern

Die mittlere Ziffer des Befehls ist die Farbnummer der Matrix:

| Adresse | Befehl | Farbe |
|---|---|---|
| 08 | `198` | Wände (9 = weiß); möglich sind nur 0, 1, 4, 5, 8, 9, C, D |
| 0C | `158` | Boden (5 = türkis) |
| 17 | `1C8` | Stirnwand (C = dunkelblau) |

## Technik

- **Speicher:** 1 Bit je Raum in den 16 Speicherregistern M0-MF. Bit 1 heißt Durchgang nach Osten, Bit 0 Durchgang nach Norden (Binärbaum-Verfahren). Die Wände nach Westen und Süden ergeben sich aus den Nachbarn.
- **Zeichnen:** Die Farben der Matrix werden einmal angelegt und auf deren Stapel gelegt. Je Blick holt das Programm sie zurück, sendet ein Bild im Blockmodus (Wände und Boden) und zeichnet die Stirnwand als Rechteck.
