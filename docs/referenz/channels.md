# Channels

Gepufferte Channels zur sicheren Kommunikation zwischen Threads.

> **Hinweis**: Die Empfangs-Methode heisst in moo `empfangen` (DE) bzw. `recv` (EN). In aelteren Beispielen taucht `receive` auf — aktuell akzeptiert der Codegenerator nur `empfangen` / `recv`.

## `kanal` / `channel`

**Signatur**: `kanal(puffer = 16) → channel`
**Zweck**: Erzeugt einen Channel mit optionaler Pufferkapazitaet.

**Beispiel** (aus `docs/lernen.md`):
```moo
setze k auf kanal(16)
```

## `.senden(wert)` / `.send(wert)`

**Signatur**: `channel.senden(wert) → nichts`
**Zweck**: Legt einen Wert in den Channel. Blockiert, wenn der Puffer voll ist.

**Beispiel** (aus `docs/lernen.md`):
```moo
k.senden("Hallo vom Thread!")
```

## `.empfangen()` / `.recv()`

**Signatur**: `channel.empfangen() → wert`
**Zweck**: Entnimmt den naechsten Wert. Blockiert, bis ein Wert verfuegbar ist.

**Beispiel** (aus `docs/lernen.md`):
```moo
setze nachricht auf k.empfangen()
zeige nachricht
```

## `.schliessen()` / `.close()`

**Signatur**: `channel.schliessen() → nichts`
**Zweck**: Schliesst den Channel. Weitere `.senden()`-Aufrufe sind danach nicht mehr zulaessig.

**Beispiel** (verifiziert, `/tmp/v3_chan.moo`):
```moo
setze k auf kanal(4)
k.senden("hallo")
setze msg auf k.empfangen()
zeige msg
k.schliessen()
```
