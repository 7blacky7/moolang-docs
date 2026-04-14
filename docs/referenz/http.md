# HTTP

## Was ist das?

HTTP (HyperText Transfer Protocol) ist das Standard-Protokoll, mit dem Programme Daten von Webservern abrufen oder an sie schicken (Request / Response). moo bringt einen einfachen synchronen HTTP-Client mit: ein Aufruf blockiert, bis die Gegenseite geantwortet hat, und liefert ein Response-Dict zurueck (Status, Body, OK-Flag). Damit lassen sich REST-APIs, Wetterdienste oder eigene Backends ohne Zusatzbibliothek ansprechen.

## `http_hole` / `http_get` / `hg`

**Signatur**: `http_hole(url) → dict`
**Rueckgabe-Dict**: `{"status": zahl, "body": text, "ok": boolean}` — `ok` ist `wahr` fuer 2xx-Status.
**Zweck**: Fuehrt einen HTTP-GET aus.

**Beispiel** (aus `beispiele/wetter_api.moo`):
```moo
setze url auf "https://wttr.in/" + stadt + "?format=3"
setze antwort auf http_get(url)
zeige antwort["body"]
```

## `http_sende` / `http_post` / `hp`

**Signatur**: `http_sende(url, daten) → dict`
**Rueckgabe-Dict**: `{"status": zahl, "body": text, "ok": boolean}`.
**Zweck**: Fuehrt einen HTTP-POST aus. `daten` wird automatisch als JSON serialisiert, der Content-Type ist `application/json`.

**Beispiel**:
```moo
setze ergebnis auf http_post("https://api.example.com/submit", {"name": "Anna"})
zeige ergebnis["status"]
```

## `http_hole_mit_headers` / `http_get_with_headers`

**Signatur**: `http_hole_mit_headers(url, request_headers) → dict`
**Rueckgabe-Dict**: `{"status": zahl, "body": text, "ok": boolean, "headers": dict}` — `headers` enthaelt die Response-Headers mit klein geschriebenen Schluesseln.
**Zweck**: Wie `http_hole`, sendet aber zusaetzliche Request-Header (z.B. `Authorization`, `User-Agent`, `Accept`) und liefert Response-Header zurueck. Nuetzlich fuer APIs mit Token-Authentifizierung oder wenn `Content-Type` / `Location` der Antwort benoetigt wird.

**Beispiel** (verifiziert, `/tmp/moo-verify/http_hdr_2_with_headers.moo`):
```moo
setze h auf {"Authorization": "Bearer abc123", "X-App": "moo"}
setze r auf http_hole_mit_headers("https://api.example.com/me", h)
zeige r["status"]
zeige r["headers"]["content-type"]
```

## `http_sende_mit_headers` / `http_post_with_headers`

**Signatur**: `http_sende_mit_headers(url, daten, request_headers) → dict`
**Rueckgabe-Dict**: `{"status": zahl, "body": text, "ok": boolean, "headers": dict}`.
**Zweck**: Wie `http_sende`, mit zusaetzlichen Request-Headern. Gibt der Aufruf einen eigenen `Content-Type`-Header mit, ersetzt dieser den Standard `application/json`.

**Beispiel** (verifiziert, `/tmp/moo-verify/http_hdr_3_post_headers.moo`):
```moo
setze h auf {"Authorization": "Bearer abc", "X-App": "moo"}
setze r auf http_sende_mit_headers("https://api.example.com/post", {"k": "v"}, h)
zeige r["ok"]
```
