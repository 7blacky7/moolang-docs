# Text-Methoden (Strings)

Methoden werden über die Punkt-Notation auf einem Text-Wert aufgerufen.

## Groß- & Kleinschreibung

### `.gross()` / `.upper()`

**Signatur**: `text.gross() → Text`
**Zweck**: Alle Zeichen in Großbuchstaben.

### `.klein()` / `.lower()`

**Signatur**: `text.klein() → Text`
**Zweck**: Alle Zeichen in Kleinbuchstaben.

Beispiel aus `beispiele/adventure.moo`:
```moo
setze t auf eingabe_text.klein()
```

## Trimmen & Teilen

### `.trimmen()` / `.trim()`

**Signatur**: `text.trimmen() → Text`
**Zweck**: Entfernt führende/abschließende Whitespaces.

### `.teilen(trenner)` / `.split(sep)`

**Signatur**: `text.teilen(trenner: Text) → Liste<Text>`
**Zweck**: Teilt den Text am Trennzeichen in eine Liste.

Beispiel aus `beispiele/adventure.moo`:
```moo
setze teile auf t.teilen(" ")
```

### `.teilstring(start, ende)` / `.slice(start, end)`

**Signatur**: `text.teilstring(start: Zahl, ende: Zahl) → Text`
**Zweck**: Gibt den Teilstring von `start` (inklusive) bis `ende` (exklusive) zurück.

```moo
setze s auf "moolang"
zeige s.teilstring(0, 3)   # "moo"
```

## Ersetzen & Enthalten

### `.ersetzen(alt, neu)` / `.replace(old, new)`

**Signatur**: `text.ersetzen(alt: Text, neu: Text) → Text`
**Zweck**: Ersetzt alle Vorkommen.

```moo
zeige "hallo welt".ersetzen("welt", "moo")
```

### `.enthält(sub)` / `.contains(sub)`

**Signatur**: `text.enthält(sub: Text) → Bool`
**Zweck**: Prüft, ob der Text `sub` enthält. (Dispatcher erkennt Typ, siehe auch Listen/Dicts.)

```moo
wenn eingabe_text.enthält("hilfe"):
    zeige "Hilfe-Menü"
```

## Länge

### `länge(text)`

**Signatur**: `länge(text: Text) → Zahl`
**Zweck**: Anzahl Zeichen. Siehe auch Kern-Referenz.

```moo
wenn länge(name) > 0:
    zeige name
```

## Verkettung

Texte werden mit dem `+`-Operator verkettet:

```moo
zeige "Hallo, " + name + "!"
```
