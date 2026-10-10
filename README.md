# LV-Karte

Offline-Hintergrundkarte **Deutschland** für die App *Vermessung* / *Aufmaß*
(Repository `Ajvar-vermessung/LeitungsVermessung`).

Die Karte wird jede Woche (montags) automatisch aus dem neuesten
[Protomaps](https://protomaps.com)-Stand gebaut, also aus OpenStreetMap:
Deutschland bis Zoom 15 (ab dort hat Protomaps die Hausnummern), rund
5,5 GB, im Format
[PMTiles](https://docs.protomaps.com/pmtiles/).

| Datei | Inhalt |
|---|---|
| `.github/workflows/karte.yml` | der wöchentliche Bau-Ablauf |
| `stand.json` | aktueller Stand: Release-Tag, Größe, SHA-256, Teile |
| `style.json` | Kartenstil (Protomaps „light“, deutsche Namen) |
| `werkzeug/` | Deutschland-Umriss, Rand-Skript, Stil-Erzeugung |
| Releases `karte-JJJJMMTT-z15` | die Kartendatei in Teilen unter 2 GB |

Die App liest `stand.json`. Gibt es einen neuen Stand, lädt sie die Teile im
WLAN herunter, setzt sie wieder zu einer Datei zusammen, prüft die Prüfsumme
und tauscht erst dann die alte Karte aus.

Von Hand bauen: *Actions → Offline-Karte bauen → Run workflow*.

Kartendaten © [OpenStreetMap](https://www.openstreetmap.org/copyright)-Mitwirkende
(ODbL), aufbereitet von Protomaps.
