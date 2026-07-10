# Text-Methoden (Strings)

## Was ist das?

Ein **Text** (in anderen Sprachen: *String*, *Zeichenkette*) ist eine Folge von Unicode-Zeichen. In moolang wird er mit doppelten Anführungszeichen geschrieben: `"Hallo"`. Texte sind **unveränderlich** (immutable) — Operationen wie `.ersetzen(…)` oder `.gross()` geben einen neuen Text zurück statt den ursprünglichen zu verändern.

Methoden werden über die Punkt-Notation aufgerufen: `"abc".gross()`. Verkettung geschieht mit `+`. Länge und Enthalten-Prüfung gibt es als Methode und als Builtin.

## Groß- & Kleinschreibung

### `.gross()` / `.upper()`

**Signatur**: `text.gross() → Text`
**Zweck**: Alle Zeichen in Großbuchstaben.

### `.klein()` / `.lower()`

**Signatur**: `text.klein() → Text`
**Zweck**: Alle Zeichen in Kleinbuchstaben.

Beispiel aus `beispiele/adventure.moo`:
```moolang
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
```moolang
setze teile auf t.teilen(" ")
```

### `.teilstring(start, ende)` / `.slice(start, end)`

**Signatur**: `text.teilstring(start: Zahl, ende: Zahl) → Text`
**Zweck**: Gibt den Teilstring von `start` (inklusive) bis `ende` (exklusive) zurück.

```moolang
setze s auf "moolang"
zeige s.teilstring(0, 3)   # "moo"
```

## Ersetzen & Enthalten

### `.ersetzen(alt, neu)` / `.replace(old, new)`

**Signatur**: `text.ersetzen(alt: Text, neu: Text) → Text`
**Zweck**: Ersetzt alle Vorkommen.

```moolang
zeige "hallo welt".ersetzen("welt", "moo")
```

### `.enthält(sub)` / `.contains(sub)`

**Signatur**: `text.enthält(sub: Text) → Bool`
**Zweck**: Prüft, ob der Text `sub` enthält. (Dispatcher erkennt Typ, siehe auch Listen/Dicts.)

```moolang
wenn eingabe_text.enthält("hilfe"):
    zeige "Hilfe-Menü"
```

## Länge

### `länge(text)`

**Signatur**: `länge(text: Text) → Zahl`
**Zweck**: Anzahl Zeichen. Siehe auch Kern-Referenz.

```moolang
wenn länge(name) > 0:
    zeige name
```

## Verkettung

Texte werden mit dem `+`-Operator verkettet:

```moolang
zeige "Hallo, " + name + "!"
```
