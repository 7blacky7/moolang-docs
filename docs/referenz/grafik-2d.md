# Grafik 2D

2D-Fenster, Zeichen-Primitive, Tastatur- und Maus-Eingabe. Runtime: SDL2.
Ground-Truth: `compiler/src/runtime_bindings.rs`, Aliase: `compiler/src/codegen.rs`.

## Fenster

### `fenster_erstelle` / `window_create` / `fe`

**Signatur**: `fenster_erstelle(titel, breite, hoehe) → fenster`
**Zweck**: Erstellt ein 2D-Fenster und gibt ein Handle zurück.

```moo
setze win auf fenster_erstelle("moo Pong", 800, 500)
```

### `fenster_offen` / `window_is_open`

**Signatur**: `fenster_offen(win) → wahr/falsch`
**Zweck**: Prüft ob das Fenster noch offen ist (Haupt-Loop-Bedingung).

### `fenster_löschen` / `window_clear` / `fl`

**Signatur**: `fenster_löschen(win, farbe)`
**Zweck**: Füllt das Fenster mit einer Farbe (Hex-String `"#RRGGBB"`).

### `fenster_aktualisieren` / `window_update` / `fa`

**Signatur**: `fenster_aktualisieren(win)`
**Zweck**: Präsentiert den Frame (Double-Buffer-Swap).

### `fenster_schliessen` / `window_close`

**Signatur**: `fenster_schliessen(win)`
**Zweck**: Schliesst das Fenster und gibt Ressourcen frei.

## Zeichnen

### `zeichne_rechteck` / `draw_rect` / `zr`

**Signatur**: `zeichne_rechteck(win, x, y, breite, hoehe, farbe)`

### `zeichne_kreis` / `draw_circle` / `zk`

**Signatur**: `zeichne_kreis(win, x, y, radius, farbe)`

### `zeichne_linie` / `draw_line`

**Signatur**: `zeichne_linie(win, x1, y1, x2, y2, farbe)`

### `zeichne_pixel` / `draw_pixel`

**Signatur**: `zeichne_pixel(win, x, y, farbe)`

## Eingabe

### `taste_gedrückt` / `key_pressed`

**Signatur**: `taste_gedrückt(taste) → wahr/falsch`
**Zweck**: Prüft ob eine Taste aktuell gedrückt ist. Keys: `"w"`, `"s"`, `"a"`, `"d"`, `"oben"`, `"unten"`, `"links"`, `"rechts"`, `"leertaste"`, `"escape"` …

### `maus_x` / `mouse_x`, `maus_y` / `mouse_y`

**Signatur**: `maus_x(win) → zahl` · `maus_y(win) → zahl`
**Zweck**: Aktuelle Mausposition im Fenster.

### `maus_gedrückt` / `mouse_pressed`

**Signatur**: `maus_gedrückt(win) → wahr/falsch`
**Zweck**: Prüft ob eine Maustaste gedrückt ist.

### `warte` / `delay`

**Signatur**: `warte(ms)` — blockiert für Millisekunden (Frame-Pacing).

## Vollständiges Beispiel (aus `beispiele/pong.moo`)

```moo
setze win auf fenster_erstelle("moo Pong", 800, 500)

solange fenster_offen(win):
    wenn taste_gedrückt("escape"):
        stopp
    wenn taste_gedrückt("w"):
        setze p1_y auf p1_y - 6

    fenster_löschen(win, "#111111")
    zeichne_rechteck(win, 20, p1_y, 12, 80, "#4CAF50")
    zeichne_kreis(win, ball_x, ball_y, 8, "#FFFFFF")
    fenster_aktualisieren(win)
    warte(16)

fenster_schliessen(win)
```
