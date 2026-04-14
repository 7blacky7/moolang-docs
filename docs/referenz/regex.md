# Regex

## Was ist das?

Ein regulaerer Ausdruck (Regular Expression, Regex, RegExp, Pattern) ist eine kompakte Mini-Sprache, um Muster in Text zu beschreiben — etwa "alle Ziffernfolgen", "alles zwischen Klammern" oder "E-Mail-aehnliche Strings". Damit laesst sich Text durchsuchen, validieren, splitten oder ersetzen. moo nutzt die POSIX-Regex-Syntax (Extended); ein Muster wird einmal kompiliert und kann dann beliebig oft auf verschiedene Texte angewendet werden.

POSIX-Regex-Builtins. Muster werden zuerst via `regex(...)` kompiliert und dann gegen Texte angewandt.

## `regex` / `muster`

**Signatur**: `regex(pattern) → regex`
**Zweck**: Kompiliert einen POSIX-Regex-String zu einem wiederverwendbaren Regex-Objekt.

**Beispiel** (verifiziert, `/tmp/v3_regex.moo`):
```moo
setze rx auf regex("[0-9]+")
```

## `passt` / `matches`

**Signatur**: `passt(text, regex) → boolean`
**Zweck**: Prueft, ob der Text zum Muster passt.

**Beispiel**:
```moo
setze ok auf passt("abc123", rx)
zeige ok
```

## `finde` / `find`

**Signatur**: `finde(text, regex) → liste<zahl>`
**Zweck**: Liefert `[start, ende]` des ersten Treffers oder eine leere/negative Markierung, wenn kein Treffer vorliegt.

**Beispiel**:
```moo
setze pos auf finde("abc123", rx)
zeige pos
```

## `finde_alle` / `find_all`

**Signatur**: `finde_alle(text, regex) → liste<text>`
**Zweck**: Liefert alle Treffer im Text als Liste.

**Beispiel**:
```moo
setze alle auf finde_alle("abc123def456", rx)
zeige alle
```

## `ersetze` / `replace`

**Signatur**: `ersetze(text, regex, ersatz) → text`
**Zweck**: Ersetzt alle Regex-Treffer im Text durch den Ersatz-String.

**Beispiel**:
```moo
setze ergebnis auf ersetze("abc123", rx, "X")
zeige ergebnis
```
