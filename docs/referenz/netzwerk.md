# Netzwerk (TCP / UDP)

## Was ist das?

Sockets sind der Low-Level-Kanal, über den zwei Programme übers Netzwerk Bytes
austauschen — darunter sitzt kein HTTP, kein Framing, nichts. Es gibt zwei
Geschmacksrichtungen: **TCP** (Stream, zuverlässig, reihenfolgetreu — wie eine
Telefonverbindung; das Modell hinter HTTP, SSH, Datenbank-Protokollen) und
**UDP** (Datagramme, unzuverlässig, verbindungslos — wie eine Postkarte; das
Modell hinter DNS, Spielen, Voice). Der Umgang entspricht der Berkeley-Sockets-
API aus Python `socket`, C oder Go `net`: binde einen Server-Port oder
verbinde dich, lies und schreibe Strings oder rohe Bytes. In moo sind alle
Operationen blockierend, mit optionalem Timeout und einer einheitlichen
Bytes-Liste für binäre Daten.

---

## TCP

### `tcp_server`

**Signatur**: `tcp_server(port) → server`
**Zweck**: Listening-Socket auf `0.0.0.0:port`.

### `tcp_verbinde` / `tcp_connect`

**Signatur**: `tcp_verbinde(host, port) → socket | nichts`

## UDP

### `udp_socket`

**Signatur**: `udp_socket(port) → socket`
**Zweck**: Erstellt ein UDP-Socket. `port=0` = automatisch freier Port.

### `sock.udp_verbinden(host, port)` / `udp_connect`

**Signatur**: `sock.udp_verbinden(host, port)` — setzt Default-Ziel für `schreiben`.

## Socket-Methoden (TCP + UDP)

| Methode | Alias | Zweck |
|---|---|---|
| `sock.annehmen()` | `accept` | Nimmt eingehende TCP-Verbindung an → Client-Socket |
| `sock.lesen(max)` | `read` | Liest bis zu `max` Bytes als **String** |
| `sock.schreiben(daten)` | `write` | Schreibt **String** auf Socket |
| `sock.lesen_bytes(max)` | `read_bytes` | Liest als **Bytes-Liste** |
| `sock.schreiben_bytes(bytes)` | `write_bytes` | Schreibt eine **Bytes-Liste** |
| `sock.timeout_setzen(ms)` | `set_timeout` | Read/Write-Timeout in ms |
| `sock.schliessen()` | `close` | Socket schliessen |

## Bytes-Konvertierung

### `string_zu_bytes` / `string_to_bytes` · `bytes_zu_liste` / `bytes_to_list`

**Signatur**: `string_zu_bytes(text) → bytes` · `bytes_zu_liste(bytes) → text`

### `bytes_neu` / `bytes_new`

**Signatur**: `bytes_neu(liste<zahl>) → bytes`
**Zweck**: Erzeugt einen binary-safe String (Byte-Puffer) aus einer Liste von
Byte-Werten (0–255). Nuetzlich zum Zusammenbauen von Netzwerk-Frames,
Protokoll-Headern oder File-Signaturen byteweise, bevor sie an `.schreiben()`
oder `datei_schreiben_bytes(...)` gehen.

**Beispiel**:
```moo
setze magic auf bytes_neu([0x89, 0x50, 0x4E, 0x47])  # PNG-Magic
datei_schreiben_bytes("header.bin", magic)
```

## Beispiel — TCP-Reverse-Proxy (aus `beispiele/proxy.moo`)

```moo
setze server auf tcp_server(LISTEN_PORT)

solange wahr:
    setze client auf server.annehmen()
    wenn client == nichts:
        zeige "Accept fehlgeschlagen"
        warte(100)
    sonst:
        setze req auf lese_http_header(client)
        setze up auf tcp_verbinde(UPSTREAM_HOST, UPSTREAM_PORT)
        up.schreiben(req)
        setze resp_bytes auf stream_bis_eof(up, client)
        up.schliessen()
        client.schliessen()
```

## Beispiel — UDP-DNS-Client (aus `beispiele/dns_resolver.moo`)

```moo
setze sock auf udp_socket(0)
sock.udp_verbinden(selbst.server_host, selbst.server_port)
sock.schreiben_bytes(query)
setze antwort auf sock.lesen_bytes(512)
sock.schliessen()
```
