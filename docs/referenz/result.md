# Result-Typ

Ein Rust-inspirierter Erfolg/Fehler-Container. Empfohlen statt Exceptions, wenn Fehler Teil des normalen Kontrollflusses sind.

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
