# LV-Karte

Offline-Hintergrundkarte **Deutschland** für die App *Vermessung* / *Aufmaß*
(Repository `Ajvar-vermessung/LeitungsVermessung`).

Die Karte wird jede Woche (montags) automatisch aus dem neuesten
[Protomaps](https://protomaps.com)-Stand gebaut, also aus OpenStreetMap:
je Bundesland eine Datei und zusätzlich ganz Deutschland (~5,7 GB), bis
Zoom 15 (ab dort hat Protomaps die Hausnummern), im Format
[PMTiles](https://docs.protomaps.com/pmtiles/).

| Datei | Inhalt |
|---|---|
| `.github/workflows/karte.yml` | der wöchentliche Bau-Ablauf |
| `stand.json` | aktueller Stand: Release-Tag, je Gebiet Größe, SHA-256, Teile |
| `style.json` | Kartenstil (Protomaps „light“, deutsche Namen) |
| `werkzeug/` | Länder-Umrisse, Gebiete zerlegen und bauen, Stil-Erzeugung |
| Releases `karte-JJJJMMTT-z15-l` | die Gebiete in Teilen unter 2 GB |

Die App liest `stand.json` und lädt nur die Gebiete, die auf dem Gerät
ausgewählt sind, im WLAN herunter. Sie setzt die Teile wieder zu einer Datei
zusammen, prüft die Prüfsumme und tauscht erst dann die alte Datei aus.

Von Hand bauen: *Actions → Offline-Karte bauen → Run workflow*.

Länder-Umrisse: [isellsoap/deutschlandGeoJSON](https://github.com/isellsoap/deutschlandGeoJSON)
(Unlicense). Kartendaten © [OpenStreetMap](https://www.openstreetmap.org/copyright)-Mitwirkende
(ODbL), aufbereitet von Protomaps.
