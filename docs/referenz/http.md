# HTTP

## Was ist das?

HTTP (HyperText Transfer Protocol) ist das Standard-Protokoll, mit dem Programme Daten von Webservern abrufen oder an sie schicken (Request / Response). moo bringt einen einfachen synchronen HTTP-Client mit: ein Aufruf blockiert, bis die Gegenseite geantwortet hat, und liefert den Antwort-Body als Text zurueck. Damit lassen sich REST-APIs, Wetterdienste oder eigene Backends ohne Zusatzbibliothek ansprechen.

HTTP-Client-Builtins fuer GET- und POST-Anfragen. Aufrufe blockieren bis zur Antwort.

## `http_hole` / `http_get` / `hg`

**Signatur**: `http_hole(url) → text`
**Zweck**: Fuehrt einen HTTP-GET aus und gibt den Response-Body als String zurueck.

**Beispiel** (aus `beispiele/wetter_api.moo`):
```moo
setze url auf "https://wttr.in/" + stadt + "?format=3"
setze antwort auf http_get(url)
zeige antwort
```

## `http_sende` / `http_post` / `hp`

**Signatur**: `http_sende(url, daten) → text`
**Zweck**: Fuehrt einen HTTP-POST mit `daten` (Dict wird als JSON serialisiert) aus und liefert den Response-Body.

**Beispiel** (aus `docs/lernen.md`):
```moo
setze ergebnis auf http_post("https://api.example.com/submit", {"name": "Anna"})
zeige ergebnis
```
