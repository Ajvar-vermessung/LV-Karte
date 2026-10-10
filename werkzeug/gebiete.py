# Zerlegt bundeslaender.geojson (16 Laender, vereinfachter Umriss aus
# isellsoap/deutschlandGeoJSON, "4_niedrig", Unlicense) in je eine Datei
# gebiete/<id>.geojson plus gebiete/de.geojson (alle Laender vereinigt) und
# schreibt gebiete/liste.json (id, name) in der Reihenfolge fuer die App.
#
# Jeder Umriss bekommt einen Rand: die Vereinfachung liegt stellenweise
# innerhalb der echten Grenze, und an der Landesgrenze soll man noch ein
# Stueck ins Nachbarland sehen. 0,05 Grad sind ~4-6 km.
import json
import os
import sys

from shapely.geometry import mapping, shape
from shapely.ops import unary_union

quelle, ziel = sys.argv[1], sys.argv[2]
rand = float(sys.argv[3]) if len(sys.argv) > 3 else 0.05
os.makedirs(ziel, exist_ok=True)

with open(quelle, encoding="utf-8") as f:
    daten = json.load(f)


def schreiben(gid, flaeche):
    with open(os.path.join(ziel, gid + ".geojson"), "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": [
            {"type": "Feature", "properties": {}, "geometry": mapping(flaeche)}]}, f)


laender = []
for feature in daten["features"]:
    p = feature["properties"]
    gid = p["id"].split("-")[1].lower()          # DE-BY -> by
    flaeche = shape(feature["geometry"])
    laender.append((gid, p["name"], flaeche))
    schreiben(gid, flaeche.buffer(rand))

schreiben("de", unary_union([f for _, _, f in laender]).buffer(rand))

liste = [{"id": "de", "name": "Ganz Deutschland"}] + [
    {"id": gid, "name": name} for gid, name, _ in sorted(laender, key=lambda x: x[1])]
with open(os.path.join(ziel, "liste.json"), "w", encoding="utf-8") as f:
    json.dump(liste, f, ensure_ascii=False)
print("\n".join(f"{g['id']} {g['name']}" for g in liste))
