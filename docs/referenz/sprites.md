# Sprites

## Was ist das?

Ein Sprite (Image, Texture, Bitmap) ist eine geladene Bilddatei, die du im
2D-Fenster frei positionieren, skalieren oder in Teilbereichen (Tile-Atlas,
Spritesheet) zeichnen kannst. Das ist die Grundlage für Charakter-Animation,
Tile-Based-Level, Icons, HUD-Elemente und Partikel — also alles, was nicht als
primitive Form (Rechteck, Kreis) gezeichnet wird. moo lädt BMP und PNG, hält
das Bild in einer GPU-freundlichen Struktur und lässt dich Teil-Rechtecke aus
einem grossen Atlas auf beliebige Ziel-Rechtecke im Fenster zeichnen.

---

Setzt ein offenes 2D-Fenster voraus.

## `sprite_laden` / `sprite_load`

**Signatur**: `sprite_laden(win, pfad) → sprite`
**Zweck**: Lädt eine Bilddatei und gibt ein Sprite-Handle zurück.

```moo
setze s auf sprite_laden(win, "beispiele/assets/sprites/zelda_like/gfx/Overworld.png")
```

## `sprite_zeichnen` / `sprite_draw`

**Signatur**: `sprite_zeichnen(win, sprite, x, y)`
**Zweck**: Zeichnet das komplette Sprite in Originalgröße.

## `sprite_zeichnen_skaliert` / `sprite_draw_scaled`

**Signatur**: `sprite_zeichnen_skaliert(win, sprite, x, y, breite, hoehe)`

## `sprite_ausschnitt` / `sprite_region`

**Signatur**: `sprite_ausschnitt(win, sprite, src_x, src_y, src_w, src_h, dst_x, dst_y, dst_w, dst_h)`
**Zweck**: Zeichnet einen Teilbereich des Sprites skaliert — Grundlage für Tile-Atlanten & Animation.

## `sprite_breite` / `sprite_width`, `sprite_hoehe` / `sprite_height`

**Signatur**: `sprite_breite(sprite) → zahl` · `sprite_hoehe(sprite) → zahl`

## `sprite_freigeben` / `sprite_free`

**Signatur**: `sprite_freigeben(sprite)` — gibt GPU/RAM-Ressourcen frei.

## Beispiel — Tile-Atlas + Character-Animation (aus `beispiele/zelda.moo`)

```moo
konstante GFX auf "beispiele/assets/sprites/zelda_like/gfx/"

funktion lade_sprites(win):
    setze s auf {}
    s["char"]  = sprite_laden(win, GFX + "character.png")
    s["world"] = sprite_laden(win, GFX + "Overworld.png")
    s["obj"]   = sprite_laden(win, GFX + "objects.png")
    gib_zurück s

funktion held_zeichnen(win, s, x, y, richtung, frame, angriff):
    setze row auf richtung
    setze col auf frame % 4
    wenn angriff > 0:
        setze col auf 4
    setze sx auf col * 34
    setze sy auf row * 32
    sprite_ausschnitt(win, s["char"], sx, sy, 34, 32, x - 8, y - 8, 48, 48)

funktion tile_zeichnen(win, s, typ, dx, dy):
    wenn typ == 0:
        sprite_ausschnitt(win, s["world"], 0, 0, 16, 16, dx, dy, 32, 32)
    wenn typ == 1:
        sprite_ausschnitt(win, s["world"], 96, 0, 16, 16, dx, dy, 32, 32)
```
