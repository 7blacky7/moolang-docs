# Test-API

Deterministische Tests für moo-Programme mit Fenster: Screenshots + simulierte
Eingaben. Nützlich für headless Regression-Tests von Spielen.

## `screenshot` / `bildschirmfoto`

**Signatur**: `screenshot(win, pfad)`
**Zweck**: Schreibt den aktuellen Framebuffer als BMP-Datei.

```moo
screenshot(win, "beispiele/test_screenshots/pong_01_start.bmp")
```

## `taste_simulieren` / `simulate_key`

**Signatur**: `taste_simulieren(taste, gedrückt)`
**Zweck**: Injiziert einen Key-Event in die SDL-Event-Queue.
`gedrückt = wahr` = key-down, `falsch` = key-up.

```moo
taste_simulieren("hoch", wahr)
# ... Frames laufen lassen ...
taste_simulieren("hoch", falsch)
```

## `maus_simulieren` / `simulate_mouse`

**Signatur**: `maus_simulieren(x, y, knopf)`
**Zweck**: Setzt Mausposition und Knopfstatus (`0`=keiner, `1`=links, …).

## Vollständiges Beispiel (aus `beispiele/test_pong.moo`)

```moo
# Frame 0: Start-Screenshot
fenster_löschen(win, "#111111")
zeichne_rechteck(win, 20, p1_y, 12, 80, "#4CAF50")
fenster_aktualisieren(win)
screenshot(win, "beispiele/test_screenshots/pong_01_start.bmp")

# Paddle hoch fahren: 60 Frames lang "hoch" drücken
taste_simulieren("hoch", wahr)
setze f auf 0
solange f < 60:
    # ... Update + Render + fenster_aktualisieren ...
    setze f auf f + 1
taste_simulieren("hoch", falsch)

screenshot(win, "beispiele/test_screenshots/pong_02_paddle_oben.bmp")
```
