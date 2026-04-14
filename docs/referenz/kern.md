# Kern-Builtins

## Was ist das?

**Builtins** (eingebaute Funktionen) sind die grundlegenden Werkzeuge, die moolang ohne Import zur Verfügung stellt — vergleichbar mit Pythons `print`, `len`, `input` oder JavaScripts `console.log`. Sie liegen in der Laufzeit (Runtime) selbst und decken Ausgabe, Eingabe, Typ-Prüfung, Zeit, Zahlen-Konvertierung und Prozess-Steuerung ab.

Fast jede Funktion hat einen deutschen und einen englischen Namen (z.B. `länge` / `len`), manchmal auch eine Kurzform. Beide sind gleichwertig — wähle, was lesbarer ist.

Quelle: `compiler/src/runtime_bindings.rs`, `compiler/src/codegen.rs`.

## Ausgabe & Eingabe

### `zeige` (Schlüsselwort)

**Signatur**: `zeige <ausdruck>`
**Zweck**: Gibt einen Wert auf der Standardausgabe aus (mit Zeilenumbruch).

```moo
zeige "Hallo, Welt!"
zeige 1 + 2
```

### `eingabe` / `input`

**Signatur**: `eingabe(prompt: Text) → Text`
**Zweck**: Liest eine Zeile von der Standardeingabe, zeigt vorher `prompt`.

Beispiel aus `beispiele/adventure.moo`:
```moo
setze eingabe_text auf eingabe("> ")
```

## Typ & Länge

### `typ_von` / `type_of`

**Signatur**: `typ_von(wert) → Text`
**Zweck**: Gibt den Typnamen als Text zurück (`"Zahl"`, `"Text"`, `"Liste"`, `"Dict"`, `"Bool"`, ...).

```moo
zeige typ_von(42)       # "Zahl"
zeige typ_von("abc")    # "Text"
```

### `länge` / `len`

**Signatur**: `länge(x) → Zahl`
**Zweck**: Länge einer Liste, eines Texts oder eines Dicts.

Beispiel aus `beispiele/adventure.moo`:
```moo
wenn länge(raum["items"]) > 0:
    zeige raum["items"]
```

## Konvertierung

### `text` / `str`

**Signatur**: `text(wert) → Text`
**Zweck**: Wandelt einen Wert in einen Text um.

```moo
zeige "Zahl: " + text(42)
```

### `zahl` / `num`

**Signatur**: `zahl(text) → Zahl`
**Zweck**: Parst eine Zahl aus einem Text.

```moo
setze n auf zahl("42")
zeige n + 1   # 43
```

## Zeit

### `zeit` / `time`

**Signatur**: `zeit() → Zahl`
**Zweck**: Aktueller Unix-Zeitstempel in Sekunden.

### `zeit_ms` / `time_ms`

**Signatur**: `zeit_ms() → Zahl`
**Zweck**: Aktueller Zeitstempel in Millisekunden (für Delta-Time-Berechnungen).

```moo
setze start auf zeit_ms()
# ... Arbeit ...
setze verstrichen auf zeit_ms() - start
```

### `warte` / `delay`

**Signatur**: `warte(ms: Zahl)`
**Zweck**: Blockiert für `ms` Millisekunden. Typischer Game-Loop-Takt.

Beispiel aus `beispiele/breakout.moo`:
```moo
warte(16)   # ~60 FPS
```

### `schlafe` / `sleep`

**Signatur**: `schlafe(sekunden: Zahl)`
**Zweck**: Pausiert den Thread für die angegebene Anzahl Sekunden (feinerer Variant von `warte`, das in ms arbeitet).

```moo
schlafe(1)
```

## Prozess & Umgebung

### `argumente` / `args`

**Signatur**: `argumente() → Liste<Text>`
**Zweck**: Kommandozeilenargumente des aktuellen Prozesses.

```moo
setze args auf argumente()
zeige args
```

### `umgebung` / `env`

**Signatur**: `umgebung(name: Text) → Text`
**Zweck**: Liest eine Umgebungsvariable.

```moo
setze pfad auf umgebung("PATH")
```

### `beende` / `exit`

**Signatur**: `beende(code: Zahl)`
**Zweck**: Beendet den Prozess mit dem angegebenen Exit-Code.

```moo
beende(0)
```

### `systemaufruf` / `syscall`

**Signatur**: `systemaufruf(nr, a1, a2, a3) → Zahl`
**Zweck**: Direkter Linux-Syscall (vier Argumente). Nur für Low-Level-Code.

## Iteration

### Range `..` Operator

**Syntax**: `<start>..<ende>` (Ausdruck, nicht Funktion)
**Zweck**: Erzeugt einen Bereich von `start` (inklusive) bis `ende` (exklusive) zur Nutzung in `für`-Schleifen.

```moo
fuer i in 0..10:
    zeige i
```

### `range`

**Signatur**: `range(start, ende) → Liste<Zahl>`
**Zweck**: Gleiche Semantik wie `..`, als Funktionsausdruck (Liste der Indizes).

## Debug

### `haltepunkt` / `breakpoint`

**Signatur**: `haltepunkt(zeile?: Zahl)`
**Zweck**: Löst einen Debugger-Breakpoint aus (für Entwicklungs-Builds).

### `ausfuehren` / `eval`

**Signatur**: `ausfuehren(code: Text) → Wert`
**Zweck**: Kompiliert und führt moo-Quellcode zur Laufzeit aus.
