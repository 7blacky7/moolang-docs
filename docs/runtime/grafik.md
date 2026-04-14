# 2D-Grafik & Sprites

2D-Grafik ist direkt in der Runtime (SDL2). Kein externes Paket, keine Setup-Schritte.

## Fenster erstellen

```moo
setze win auf fenster_erstellen("Mein Spiel", 800, 600)

solange fenster_offen(win):
    fenster_löschen(win, 0, 0, 0)        # Schwarz

    # Rechteck zeichnen
    fenster_rechteck(win, 100, 100, 200, 150, "rot")

    # Kreis zeichnen
    fenster_kreis(win, 400, 300, 50, "blau")

    # Text
    fenster_text(win, 10, 10, "Hallo!", 24, "weiss")

    fenster_aktualisieren(win)

    wenn fenster_taste(win, "escape"):
        stopp

    warte(16)

fenster_schliessen(win)
```

## Sprites

Bilder laden und zeichnen:

```moo
setze spieler auf sprite_laden("assets/spieler.png")

solange fenster_offen(win):
    fenster_löschen(win, 0, 0, 0)
    sprite_zeichnen(win, spieler, x, y)      # an Position
    sprite_zeichnen(win, spieler, x, y, 2.0) # mit 2-facher Skalierung
    fenster_aktualisieren(win)
```

## Animationen (Spritesheets)

```moo
setze held auf sprite_laden("assets/held.png")

setze frame auf 0
solange fenster_offen(win):
    # Nur Teil des Sprites zeichnen (Spritesheet)
    setze src_x auf (frame % 8) * 32     # 8 Frames à 32px
    sprite_zeichnen_teil(win, held, x, y, src_x, 0, 32, 32)
    setze frame auf frame + 1
    warte(100)
```

## Input

```moo
wenn fenster_taste(win, "links"):
    setze spieler_x auf spieler_x - 4
wenn fenster_taste(win, "rechts"):
    setze spieler_x auf spieler_x + 4
wenn fenster_taste(win, "leer"):
    schießen()

# Maus
setze maus auf fenster_maus(win)
zeige maus["x"], maus["y"], maus["taste"]
```

## Siehe auch

- [Beispiel: pong.moo](https://github.com/7blacky7/moo/blob/master/beispiele/pong.moo)
- [Beispiel: snake.moo](https://github.com/7blacky7/moo/blob/master/beispiele/snake.moo)
- [Beispiel: breakout.moo](https://github.com/7blacky7/moo/blob/master/beispiele/breakout.moo)
- [Beispiel: zelda.moo](https://github.com/7blacky7/moo/blob/master/beispiele/zelda.moo) — Sprites + Tileset + Kollision
- [Beispiel: tetris.moo](https://github.com/7blacky7/moo/blob/master/beispiele/tetris.moo)

126+ weitere Beispiele im [Source-Repo](https://github.com/7blacky7/moo/tree/master/beispiele).
