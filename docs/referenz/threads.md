# Threads

Builtins fuer Hintergrund-Ausfuehrung. Threads werden mit `starte(callable, arg)` gestartet und liefern ein Thread-Handle, dessen Methoden `warten()` und `fertig()` verfuegbar sind.

## `starte` / `spawn`

**Signatur**: `starte(funktion, argument) → thread`
**Zweck**: Startet `funktion(argument)` in einem neuen Thread und liefert ein Handle.

**Beispiel** (verifiziert, `/tmp/v3_thread.moo`):
```moo
setze t auf starte((x) => x * 2, 21)
zeige t.warten()
```

## `.warten()` / `.wait()`

**Signatur**: `thread.warten() → wert`
**Zweck**: Blockiert bis der Thread fertig ist und liefert sein Ergebnis.

**Beispiel**:
```moo
setze ergebnis auf t.warten()
zeige ergebnis
```

## `.fertig()` / `.done()`

**Signatur**: `thread.fertig() → boolean`
**Zweck**: Prueft ohne zu blockieren, ob der Thread bereits terminiert ist.

**Beispiel**:
```moo
wenn t.fertig():
    zeige "Thread ist fertig"
```
