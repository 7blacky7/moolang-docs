# Events & Freeze

## Was ist das?

**Events** (Ereignisse) sind ein Mechanismus, mit dem Objekte **Nachrichten** veröffentlichen, auf die andere Teile des Programms reagieren können — ohne dass das sendende Objekt wissen muss, wer zuhört. In anderen Sprachen bekannt als *Observer Pattern*, *Pub/Sub*, *EventEmitter* (Node.js) oder *Signals* (Qt, Godot).

**Freeze** bedeutet, eine Liste oder ein Dict **unveränderlich** zu machen. Weitere Schreibzugriffe lösen einen Fehler aus. Ähnlich zu `Object.freeze` in JavaScript oder `frozen` Dataclasses in Python. Nützlich für Konfigurationen oder geteilten State.

## Events

moolang-Objekte können Events publizieren und abonnieren (Beobachter-Muster).

### `ereignis_bei(obj, event, callback)` / `event_on(obj, event, cb)`

**Signatur**: `ereignis_bei(obj, event: Text, callback: Funktion)`
**Zweck**: Registriert `callback`, der ausgelöst wird, wenn auf `obj` das Event `event` emittiert wird.

### `ereignis_auslösen(obj, event)` / `event_emit(obj, event)`

**Signatur**: `ereignis_auslösen(obj, event: Text)`
**Zweck**: Löst das Event aus — alle registrierten Callbacks werden aufgerufen.

### Beispiel

```moo
setze spieler auf neues Objekt
ereignis_bei(spieler, "tod", funktion():
    zeige "Game Over"
ende)

ereignis_auslösen(spieler, "tod")
```

Alternative Punkt-Syntax: `obj.bei("event", cb)` / `obj.auslösen("event")` — gleiche Semantik.

## Freeze / Immutable

### `einfrieren(wert)` / `freeze(wert)`

**Signatur**: `einfrieren(wert) → Wert`
**Zweck**: Macht eine Liste oder ein Dict unveränderlich. Weitere Mutationen werfen zur Laufzeit einen Fehler.

### `ist_eingefroren(wert)` / `is_frozen(wert)`

**Signatur**: `ist_eingefroren(wert) → Bool`
**Zweck**: Prüft, ob `wert` eingefroren ist.

```moo
setze config auf einfrieren({"port": 8080, "host": "0.0.0.0"})
wenn ist_eingefroren(config):
    zeige "Konfiguration ist schreibgeschützt"
```
