# Listen-Methoden

## Was ist das?

Eine **Liste** (in anderen Sprachen: *Array*, *Vector*, *List*) speichert mehrere Werte in einer geordneten Reihenfolge. Zugriff erfolgt über einen Index: `liste[0]` ist das erste Element. Listen wachsen dynamisch — über `.hinzufügen(wert)` werden Elemente angehängt.

Schreibweise: `[1, 2, 3]`. Elemente dürfen gemischte Typen sein (`[1, "abc", wahr]`). Index beginnt bei `0`.

Methoden werden über die Punkt-Notation auf einer Liste aufgerufen.

## Hinzufügen & Entfernen

### `.hinzufügen(wert)` / `.append(wert)`

**Signatur**: `liste.hinzufügen(wert)`
**Zweck**: Hängt `wert` ans Ende an.

Beispiel aus `beispiele/breakout.moo`:
```moo
brick_aktiv.hinzufügen(wahr)
brick_x.hinzufügen(BRICK_START_X + spalte * (BRICK_W + BRICK_ABSTAND))
```

### `.pop()`

**Signatur**: `liste.pop() → Wert`
**Zweck**: Entfernt und gibt das letzte Element zurück.

## Zugriff

Der Elementzugriff erfolgt über Index-Operator `[i]`:

```moo
setze erster auf snake[0]
setze snake[0] auf [10, 5]
```

### `länge(liste)`

**Signatur**: `länge(liste) → Zahl`
**Zweck**: Anzahl der Elemente (siehe Kern).

Beispiel aus `beispiele/adventure.moo`:
```moo
solange i < länge(inv):
    zeige inv[i]
    setze i auf i + 1
```

## Sortieren & Umkehren

### `.sortieren()` / `.sort()`

**Signatur**: `liste.sortieren() → Liste`
**Zweck**: Sortierte Kopie (aufsteigend).

### `.umkehren()` / `.reverse()`

**Signatur**: `liste.umkehren() → Liste`
**Zweck**: Liste in umgekehrter Reihenfolge.

## Verbinden & Enthalten

### `.verbinden(trenner)` / `.join(sep)`

**Signatur**: `liste.verbinden(trenner: Text) → Text`
**Zweck**: Verbindet Text-Elemente zu einem einzigen Text.

```moo
setze csv auf ["a", "b", "c"].verbinden(",")
```

### `.enthält(wert)` / `.contains(wert)`

**Signatur**: `liste.enthält(wert) → Bool`
**Zweck**: Prüft, ob `wert` in der Liste vorkommt.

Beispiel aus `beispiele/wireframe.moo`:
```moo
wenn FONT.enthält(ch):
    zeige ch
```
