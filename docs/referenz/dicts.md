# Dict-Methoden

## Was ist das?

Ein **Dict** (Kurzform von *Dictionary*; in anderen Sprachen: *Map*, *HashMap*, *Assoziatives Array*, *Object* in JSON) speichert **Schlüssel-Wert-Paare**. Statt über einen numerischen Index wird über einen Schlüssel zugegriffen: `person["name"]`.

Schreibweise: `{"name": "Ada", "alter": 36}`. Schlüssel sind üblicherweise Texte. Werte dürfen beliebige Typen sein. Die Reihenfolge ist nicht garantiert.

Methoden (`.hat`, `.schlüssel`, ...) gibt es für Zugriffsprüfung und Schlüssellisten. Lesen/Schreiben der Werte erfolgt über den Index-Operator `[schlüssel]`.

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
