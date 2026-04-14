# Hybrid 2D + 3D (Phase M5)

## Was ist das?

Hybrid-Rendering (Mixed-Mode, Layered Compositing, 2.5D + 3D) bedeutet:
ein **einziges Fenster** mit **einem GL-Context** und **gemeinsamem
Z-Buffer**, in dem klassische 2D-Sprites/Tiles/Linien neben echten
3D-Primitiven (Wuerfel, Kugel, Mesh) leben — und der Tiefen-Test sich
korrekt zwischen beiden Welten austraegt. Klassischer Anwendungsfall:
isometrische Spiele mit 3D-Charakteren ueber 2.5D-Tile-Welt
(Siedler 3, Diablo, RimWorld).

> **Status**: Phase M5 — additiv. Die alten Pipelines
> (`fenster_*` SDL_Renderer, `raum_*` als eigenes 3D-Fenster) bleiben
> unveraendert. Hybrid ist ein dritter Modus, kein Ersatz.

## Window-Lifecycle

### `fenster_unified` / `unified_window` / `fenster_hybrid`

**Signatur**: `fenster_unified(titel, breite, hoehe) → win`
**Zweck**: Oeffnet ein Fenster mit GL3.3-Core-Profile, GL_DEPTH_TEST
(LEQUAL) und Color+Depth-Clear pro Frame. In dieses Fenster duerfen
sowohl `zeichne_*_z`-Aufrufe (2D mit Z) als auch `raum_*`-Aufrufe (3D)
hineinrendern. Der Z-Test sortiert beide gemeinsam. Window-Tag ist
`MOO_WINDOW_HYBRID` (= 18).

### `hybrid_offen` / `hybrid_is_open`

**Signatur**: `hybrid_offen(win) → boolean`
**Zweck**: Prueft Event-Polling und liefert `wahr`, solange das Fenster offen ist.

### `hybrid_löschen` / `hybrid_clear`

**Signatur**: `hybrid_löschen(win, r, g, b) → nichts`
**Zweck**: `glClear(COLOR | DEPTH)` mit `glClearColor(r, g, b, 1.0)`. Pro Frame zu Beginn aufrufen.

### `hybrid_aktualisieren` / `hybrid_update`

**Signatur**: `hybrid_aktualisieren(win) → nichts`
**Zweck**: SwapBuffers + PollEvents. Pro Frame am Ende aufrufen.

### `hybrid_schliessen` / `hybrid_close`

**Signatur**: `hybrid_schliessen(win) → nichts`
**Zweck**: GL-Context + Window freigeben. `.close()`/`.schliessen()` via `moo_smart_close` greift auch auf `MOO_WINDOW_HYBRID` durch.

## 2D mit Z (texted/getrenderte Quads im Z-Buffer)

### `zeichne_rechteck_z` / `draw_rect_z`

**Signatur**: `zeichne_rechteck_z(win, x, y, z, breite, hoehe, farbe)`
**Zweck**: Wie `zeichne_rechteck`, aber mit zusaetzlichem Welt-Z-Wert.
Niedrigere Z-Werte sind naeher an der Kamera (Z-Test `<=`). `farbe` ist
ein Hex-/Namen-String (`"rot"`, `"#ff0000"`).

### `zeichne_kreis_z` / `draw_circle_z`

**Signatur**: `zeichne_kreis_z(win, cx, cy, z, radius, farbe)`
**Zweck**: Wie `zeichne_kreis` mit Z (gefuellt, getriangulierter Fan).

### `zeichne_linie_z` / `draw_line_z`

**Signatur**: `zeichne_linie_z(win, x1, y1, x2, y2, z, farbe)`
**Zweck**: Wie `zeichne_linie` mit Welt-Z (beide Endpunkte gleicher Z).

### `sprite_zeichnen_z` / `sprite_draw_z`

**Signatur**: `sprite_zeichnen_z(win, sprite_id, x, y, z, breite, hoehe)`
**Zweck**: Sprite als textured Quad mit Welt-Z. Voll-z-getestet mit
3D-Pass — ein Sprite kann hinter einem `raum_würfel` verschwinden.

## Beispiel — Mixed Quad + Wuerfel mit Z-Test

```moo
setze win auf fenster_unified("Hybrid Demo", 800, 600)
solange hybrid_offen(win):
    hybrid_löschen(win, 0.1, 0.1, 0.15)
    raum_kamera(win, 0.0, 2.0, 5.0, 0.0, 0.0, 0.0)
    # 2D-Quad weit vorne (kleiner Z)
    zeichne_rechteck_z(win, 100, 100, 0.3, 200, 150, "rot")
    # 3D-Wuerfel dahinter (groesserer Z) — verdeckt Quad teilweise
    raum_würfel(win, 0.0, 0.0, 1.0, 1.0, "blau")
    hybrid_aktualisieren(win)
hybrid_schliessen(win)
```

## Z-Range-Konvention

Welt-Z-Werte werden im selben Bereich erwartet wie `raum_*`-Koordinaten
(typisch 0–50, je nach `raum_perspektive` Near/Far). Die 2D-API rechnet
intern auf den GL-Depth-Range um. **Niedrigere Z = naeher an Kamera**.

## Grenzen

- Nur GL3.3-Backend (Cargo-Feature `gl33`). gl21- und Vulkan-Hybrid
  sind separater Aufwand und derzeit nicht implementiert.
- Klassische `fenster_erstelle`-Pipeline (SDL_Renderer) bleibt parallel
  ohne Z-Test — wer Hybrid will, muss `fenster_unified` benutzen.
- Sprite-Loading via `sprite_lade` ist beim Hybrid-Window identisch.
