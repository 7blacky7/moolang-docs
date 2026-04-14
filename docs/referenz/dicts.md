# Dict-Methoden

Dictionaries (Schlüssel-Wert-Maps) haben Punkt-Methoden für Zugriffsprüfung und Schlüssellisten. Lesen/Schreiben der Werte erfolgt über den Index-Operator `[schlüssel]`.

## Lesen & Schreiben

```moo
setze raum auf {"name": "Höhle", "items": []}
zeige raum["name"]
setze raum["besucht"] auf wahr
```

## Methoden

### `.hat(schlüssel)` / `.has(key)`

**Signatur**: `dict.hat(schlüssel) → Bool`
**Zweck**: Prüft, ob ein Schlüssel existiert.

```moo
wenn raum.hat("items"):
    zeige raum["items"]
```

### `.schlüssel()` / `.keys()`

**Signatur**: `dict.schlüssel() → Liste<Text>`
**Zweck**: Liste aller Schlüssel.

Beispiel aus `beispiele/adventure.moo`:
```moo
setze keys auf raum.schlüssel()
solange i < länge(keys):
    zeige keys[i]
    setze i auf i + 1
```

### `.enthält(schlüssel)` / `.contains(key)`

**Signatur**: `dict.enthält(schlüssel) → Bool`
**Zweck**: Alias für `.hat()` — funktioniert durch den Typ-Dispatch auf Dicts, Listen und Texten gleich.

## Länge

```moo
zeige länge(raum)   # Anzahl Schlüssel
```
