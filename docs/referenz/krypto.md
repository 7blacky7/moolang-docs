# Kryptografie & Bereinigung

## Was ist das?

Kryptografie (Cryptography) bezeichnet mathematische Verfahren, um Daten gegen Manipulation oder Mitlesen abzusichern. Hashing (Digest, Fingerprint) erzeugt aus beliebigen Eingaben einen kurzen, einseitigen Pruefwert. Sicherer Zufall (Cryptographically Secure RNG) liefert nicht vorhersagbare Werte fuer Tokens und Schluessel. Encoding wie Base64 macht binaere Daten textsicher transportierbar. Bereinigung (Sanitizing, Escaping) entschaerft gefaehrliche Zeichen aus Nutzereingaben, bevor sie in HTML oder SQL landen.

Builtins fuer Hashing, sicheren Zufall, Base64-Kodierung und Input-Bereinigung.

## `sha256` / `sh`

**Signatur**: `sha256(text) → text`
**Zweck**: Berechnet den SHA-256-Hash des Strings und liefert ihn als Hex-String.

**Beispiel** (aus `beispiele/showcase.moo`):
```moo
setze hash auf sha256("moo ist toll")
zeige f"SHA256: {hash}"
```

## `sha1`

**Signatur**: `sha1(text) → text`
**Zweck**: SHA-1-Hash als Hex-String (fuer Altsysteme — SHA-256 bevorzugen).

**Beispiel**:
```moo
setze hash auf sha1("moo")
zeige hash
```

## `sha1_bytes`

**Signatur**: `sha1_bytes(bytes) → liste<zahl>`
**Zweck**: SHA-1-Hash einer Byte-Liste, zurueckgegeben als 20 Bytes.

**Beispiel**:
```moo
setze hash auf sha1_bytes([72, 105])
```

## `sichere_zufall` / `secure_random`

**Signatur**: `sichere_zufall(laenge) → text`
**Zweck**: Kryptografisch sichere Zufallsbytes als Hex-String (`laenge` = Anzahl Bytes).

**Beispiel** (aus `docs/lernen.md`):
```moo
setze token auf sichere_zufall(16)
```

## `base64_kodieren` / `base64_encode` / `b64e`

**Signatur**: `base64_kodieren(text) → text`
**Zweck**: Base64-Kodierung eines Strings.

**Beispiel** (aus `beispiele/showcase.moo`):
```moo
setze encoded auf base64_kodieren("Hallo moo!")
zeige f"Base64: {encoded}"
```

## `base64_dekodieren` / `base64_decode` / `b64d`

**Signatur**: `base64_dekodieren(text) → text`
**Zweck**: Dekodiert einen Base64-String zurueck zum Original.

**Beispiel** (aus `beispiele/showcase.moo`):
```moo
zeige f"Decoded: {base64_dekodieren(encoded)}"
```

## `html_bereinigen` / `sanitize_html`

**Signatur**: `html_bereinigen(text) → text`
**Zweck**: Escaped HTML-Sonderzeichen, um XSS zu verhindern.

**Beispiel** (aus `docs/lernen.md`):
```moo
setze sicher auf html_bereinigen("<script>alert('hack')</script>")
```

## `sql_bereinigen` / `sanitize_sql`

**Signatur**: `sql_bereinigen(text) → text`
**Zweck**: Escaped SQL-Sonderzeichen (einfache Anfuehrungszeichen etc.), um einfache SQL-Injection zu entschaerfen.

**Beispiel** (aus `docs/lernen.md`):
```moo
setze sicher auf sql_bereinigen("'; DROP TABLE users; --")
```
