#!/usr/bin/env bash
# Baut EIN Gebiet: ausschneiden, pruefen, in Teile < 2 GB zerlegen, Kennzahlen
# nach $GROSS/meta/<id>.json. Aufruf: werkzeug/gebiet_bauen.sh <id> <build>
# (vom Workflow parallel fuer alle Gebiete gestartet).
set -euo pipefail
id="$1"
build="$2"
datei="$GROSS/$id.pmtiles"

./pmtiles extract "https://build.protomaps.com/$build" "$datei" \
  --region="gebiete/$id.geojson" --maxzoom="$MAXZOOM" --download-threads=4 --quiet
./pmtiles verify "$datei" > /dev/null

split -b "$TEILGROESSE" -d -a 2 "$datei" "$GROSS/teile/$id.pmtiles.teil"
groesse=$(stat -c %s "$datei")
sha=$(sha256sum "$datei" | cut -d' ' -f1)
rm "$datei"

teile=$(for f in "$GROSS"/teile/"$id".pmtiles.teil*; do
  printf '{"name":"%s","groesse":%s,"sha256":"%s"}\n' "$(basename "$f")" "$(stat -c %s "$f")" "$(sha256sum "$f" | cut -d' ' -f1)"
done | jq -s .)
jq -n --arg id "$id" --argjson groesse "$groesse" --arg sha "$sha" --argjson teile "$teile" \
  '{id: $id, groesse: $groesse, sha256: $sha, teile: $teile}' > "$GROSS/meta/$id.json"
echo "$id: $((groesse / 1000000)) MB"
