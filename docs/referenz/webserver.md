# Webserver

## Was ist das?

Ein Webserver spricht das HTTP-Protokoll — das ist die Sprache, in der Browser
mit Servern reden (Request/Response, wie bei Express in Node.js, Flask in
Python oder dem eingebauten `http`-Paket in Go). moo bringt einen minimalen,
eingebauten HTTP-Server: du bindest einen Port, nimmst eingehende Anfragen an,
schaust auf Pfad und Methode und schickst eine Antwort zurück — HTML, JSON,
eine statische Datei oder ein kleines Template mit `{{platzhaltern}}`. Keine
externen Libraries nötig; der Server ist synchron-blockierend und gut genug
für APIs, kleine Apps, Tools und Lerneinheiten.

---

## Server

### `web_server`

**Signatur**: `web_server(port) → server`
**Zweck**: Bindet auf `0.0.0.0:port` und gibt ein Server-Handle zurück.
Alias: `web_erstelle`.

### `server.web_annehmen()` / `web_accept(server)`

**Signatur**: `server.web_annehmen() → request | nichts`
**Zweck**: Blockierendes Accept — liefert das nächste eingehende Request-Objekt
oder `nichts` bei Shutdown.

### `server.schliessen()` / `server.close()`

**Signatur**: `server.schliessen()`
**Zweck**: Schliesst den Webserver. Die zugrundeliegende Runtime-Funktion
`moo_web_close` wird über den generischen `close`/`schliessen`-Method-Dispatch
(Tag-basierter Smart-Close) aufgerufen — es gibt keine top-level `web_schliessen`-Funktion.

## Antworten

### `web_antworten` / `web_respond`

**Signatur**: `web_antworten(req, body, status)`
**Zweck**: Sendet eine HTTP-Antwort (HTML/Text).

### `web_json`

**Signatur**: `web_json(req, daten)`
**Zweck**: Sendet `daten` als `Content-Type: application/json`. `daten` kann Dict oder Liste sein.

### `web_datei` / `web_file`

**Signatur**: `web_datei(req, pfad)`
**Zweck**: Liefert eine statische Datei vom Dateisystem aus.

### `web_template` / `web_vorlage`

**Signatur**: `web_template(req, html, vars)`
**Zweck**: Rendert ein Template (`{{name}}`-Platzhalter) mit den Variablen
aus dem Dict `vars`.

## Request-Methoden (auf `req`)

- `req.antworten(body, status)` / `req.respond(body, status)`
- `req.json_antworten(daten)` / `req.json_respond(daten)`

## Vollständiges Beispiel (aus `beispiele/http_api.moo`)

```moo
setze todos auf ["moo lernen", "REST-API bauen"]
setze server auf web_server(3000)
zeige "Server läuft auf http://localhost:3000"

solange wahr:
    setze req auf server.web_annehmen()
    wenn req == nichts:
        stopp

    setze pfad auf req["pfad"]

    wenn pfad == "/api/todos":
        web_json(req, {"todos": todos, "anzahl": länge(todos)})
    sonst wenn pfad == "/api/status":
        web_json(req, {"sprache": "moo", "todos": länge(todos)})
    sonst wenn pfad == "/":
        web_antworten(req, "<h1>moo REST API</h1>", 200)
    sonst:
        web_antworten(req, "Nicht gefunden", 404)
```
