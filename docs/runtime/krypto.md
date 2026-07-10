# Kryptografie & Sicherheit

## Hashing

```moolang
setze hash auf sha256("geheimer Text")
zeige hash                        # Hex-String

setze md5_hash auf md5("text")
setze sha1_hash auf sha1("text")
setze sha512_hash auf sha512("text")
```

## Zufall (kryptografisch sicher)

```moolang
setze token auf sichere_zufall(16)     # 16 Bytes Zufall, hex-kodiert
# Englisch: secure_random(16)
```

## Base64-Kodierung

```moolang
setze kodiert auf base64_encode("Hallo Welt")
zeige kodiert                          # "SGFsbG8gV2VsdA=="

setze original auf base64_decode(kodiert)
zeige original                         # "Hallo Welt"
```

## Sanitizing

Verhindern typischer Injection-Angriffe:

```moolang
# HTML-Tags entschaerfen
setze sicher auf html_bereinigen("<script>alert('hack')</script>")
zeige sicher    # "&lt;script&gt;alert('hack')&lt;/script&gt;"

# SQL-Injection verhindern
setze sicher auf sql_bereinigen("'; DROP TABLE users; --")
```

!!! warning "Besser: Prepared Statements"
    `sql_bereinigen` ist ein Notbehelf. Benutze stattdessen Prepared Statements mit `?`-Platzhaltern (siehe [Datenbank](datenbank.md)).

## HMAC (Message Authentication)

```moolang
setze mac auf hmac_sha256("geheimer_schluessel", "nachricht")
```

## Anwendungsbeispiel: Token generieren

```moolang
funktion session_token():
    setze random auf sichere_zufall(32)
    setze timestamp auf text(zeit_ms())
    gib_zurück base64_encode(random + ":" + timestamp)
```
