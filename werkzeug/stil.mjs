// Erzeugt style.json fuer die Offline-Karte aus dem Protomaps-Stilpaket
// (@protomaps/basemaps, Variante "light", deutsche Namen).
//
// Die Quelle "protomaps" zeigt auf den Platzhalter pmtiles://DATEI - die App
// setzt dort den Pfad der heruntergeladenen Datei auf dem Geraet ein.
// Schriften und Symbole kommen von protomaps.github.io (MapLibre haelt sie
// nach dem ersten Laden im Zwischenspeicher).
import { writeFileSync } from "node:fs";
import { layers, namedFlavor } from "@protomaps/basemaps";

const stil = {
  version: 8,
  name: "Protomaps Light (Deutschland, offline)",
  glyphs: "https://protomaps.github.io/basemaps-assets/fonts/{fontstack}/{range}.pbf",
  sprite: "https://protomaps.github.io/basemaps-assets/sprites/v4/light",
  sources: {
    protomaps: {
      type: "vector",
      url: "pmtiles://DATEI",
      attribution: "Protomaps © OpenStreetMap",
    },
  },
  layers: layers("protomaps", namedFlavor("light"), { lang: "de" }),
};

writeFileSync(process.argv[2] ?? "style.json", JSON.stringify(stil));
