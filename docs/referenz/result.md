# Result-Typ

## Was ist das?

Ein **Result** ist ein Wert, der entweder **Erfolg** (`ok`) oder **Fehler** (`fehler`) enthält — ein aus Rust bekanntes Muster (dort `Result<T, E>`), das auch in Haskell (`Either`), Swift (`Result`), TypeScript (per Library) und Kotlin zu finden ist.

Statt einen Fehler als Exception zu werfen (die unsichtbar durch den Aufrufbaum reist), gibt eine Funktion einen Result zurück. Der Aufrufer muss explizit prüfen, ob das Ergebnis ok ist, bevor er den Inhalt verwendet. Das macht den Fehlerpfad sichtbar im Typ und Kontrollfluss — sinnvoll für **erwartbare** Fehler (Parsen, Netzwerk, I/O). Für unerwartete Programmfehler (Bugs, Assertions) siehe **Fehlerbehandlung** mit `wirf`/`versuche`.

## Konstruktoren

### `ok(wert)`

**Signatur**: `ok(wert) → Result`
**Zweck**: Erfolgs-Result mit dem angegebenen Wert.

### `fehler(msg)` / `err(msg)`

**Signatur**: `fehler(msg) → Result`
**Zweck**: Fehler-Result mit einer Fehlermeldung (oder beliebigem Wert).

## Prüfen

### `ist_ok(r)` / `is_ok(r)`

**Signatur**: `ist_ok(r: Result) → Bool`
**Zweck**: Wahr, wenn `r` ein Erfolg ist.

### `ist_fehler(r)` / `is_err(r)`

**Signatur**: `ist_fehler(r: Result) → Bool`
**Zweck**: Wahr, wenn `r` ein Fehler ist.

## Entpacken

### `entpacke(r)` / `unwrap(r)`

**Signatur**: `entpacke(r: Result) → Wert`
**Zweck**: Gibt den inneren Wert zurück. Bei Fehler-Result wird eine Exception ausgelöst.

## Muster

```moo
funktion hole_datei(pfad):
    wenn nicht datei_existiert(pfad):
        gib_zurück fehler("Datei fehlt: " + pfad)
    gib_zurück ok(datei_lesen(pfad))

setze r auf hole_datei("config.json")
wenn ist_ok(r):
    zeige entpacke(r)
sonst:
    zeige "Fehler aufgetreten"
```
