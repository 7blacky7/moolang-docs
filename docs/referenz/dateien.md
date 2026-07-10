# Datei-I/O

## Was ist das?

Datei-I/O (Input/Output, File System Access) bedeutet: Daten dauerhaft auf der Festplatte ablegen oder von dort lesen. moo bietet sowohl Text-Operationen (UTF-8 Strings) als auch binaere Operationen (Byte-Listen / Buffer / ByteArray) und einen einfachen Verzeichnis-Listing-Aufruf. Pfade koennen relativ zum Arbeitsverzeichnis oder absolut sein.

Builtins fuer Datei- und Verzeichnis-Operationen. Alle Pfade sind relativ zum Arbeitsverzeichnis oder absolut.

## `datei_lesen` / `file_read` / `dl`

**Signatur**: `datei_lesen(pfad) → text`
**Zweck**: Liest eine Datei vollstaendig als UTF-8-Text ein.

**Beispiel** (aus `beispiele/datei_suche.moo`):
```moolang
setze inhalt auf datei_lesen(dateiname)
setze zeilen auf inhalt.teilen("\n")
```

## `datei_schreiben` / `file_write` / `ds`

**Signatur**: `datei_schreiben(pfad, text) → nichts`
**Zweck**: Schreibt `text` in die Datei (legt sie an, ueberschreibt bestehenden Inhalt).

**Beispiel** (aus `beispiele/ascii_editor.moo`):
```moolang
datei_schreiben("art.txt", inhalt + "\n")
```

## `datei_lesen_bytes` / `file_read_bytes`

**Signatur**: `datei_lesen_bytes(pfad) → liste<zahl>`
**Zweck**: Liest eine Datei binaer als Liste von Byte-Werten (0–255).

**Beispiel** (aus `docs/lernen.md`):
```moolang
setze bytes auf datei_lesen_bytes("bild.png")
zeige länge(bytes)
```

## `datei_schreiben_bytes` / `file_write_bytes`

**Signatur**: `datei_schreiben_bytes(pfad, bytes) → nichts`
**Zweck**: Schreibt eine Byte-Liste binaer in die Datei.

**Beispiel**:
```moolang
datei_schreiben_bytes("out.bin", [72, 105, 10])
```

## `datei_anhängen` / `file_append`

**Signatur**: `datei_anhängen(pfad, text) → nichts`
**Zweck**: Haengt Text an das Ende einer Datei an (legt sie ggf. an).

**Beispiel**:
```moolang
datei_anhängen("log.txt", "Eintrag\n")
```

## `datei_zeilen` / `file_lines`

**Signatur**: `datei_zeilen(pfad) → liste<text>`
**Zweck**: Liest eine Datei und gibt sie als Liste von Zeilen zurueck.

**Beispiel**:
```moolang
für zeile in datei_zeilen("log.txt"):
    zeige zeile
```

## `datei_existiert` / `file_exists` / `de`

**Signatur**: `datei_existiert(pfad) → boolean`
**Zweck**: Prueft, ob der Pfad auf eine vorhandene Datei zeigt.

**Beispiel** (aus `beispiele/ascii_editor.moo`):
```moolang
wenn nicht datei_existiert("art.txt"):
    zeige "noch keine Datei"
```

## `datei_löschen` / `file_delete` / `dd`

**Signatur**: `datei_löschen(pfad) → nichts`
**Zweck**: Entfernt eine Datei vom Dateisystem.

**Beispiel**:
```moolang
datei_löschen("temp.txt")
```

## `verzeichnis_liste` / `dir_list`

**Signatur**: `verzeichnis_liste(pfad) → liste<text>`
**Zweck**: Liefert die Eintraege (Dateinamen) eines Verzeichnisses als Liste.

**Beispiel**:
```moolang
für eintrag in verzeichnis_liste("."):
    zeige eintrag
```
