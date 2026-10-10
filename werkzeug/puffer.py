# Vergroessert den groben Deutschland-Umriss (deutschland.geojson, ~1,4 KB)
# um einen Rand, damit an der Grenze keine Kacheln fehlen: der Umriss ist
# stark vereinfacht und liegt stellenweise einige Kilometer innerhalb der
# echten Grenze. 0,15 Grad sind ~10-17 km.
import json
import sys

from shapely.geometry import mapping, shape

quelle, ziel, rand = sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 0.15
with open(quelle, encoding="utf-8") as f:
    daten = json.load(f)
flaeche = shape(daten["features"][0]["geometry"]).buffer(rand)
with open(ziel, "w", encoding="utf-8") as f:
    json.dump({"type": "FeatureCollection", "features": [
        {"type": "Feature", "properties": {}, "geometry": mapping(flaeche)}]}, f)
