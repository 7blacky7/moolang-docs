# Grafik 3D

## Was ist das?

3D-Grafik beschreibt eine Szene in echten Welt-Koordinaten (X, Y, Z) und
projiziert sie mit einer Kamera auf dein Fenster — so wie Minecraft, Quake oder
jeder Level-Editor arbeiten. moo bringt einen simplen **Immediate-Mode-Renderer**
mit drei Backends (OpenGL 3.3, OpenGL 2.1 für alte Hardware, Vulkan): du öffnest ein 3D-Fenster, setzt eine Perspektive und eine
Kamera, stapelst Transformationen (Translate, Rotate) über einen Matrix-Stack
(wie OpenGL 1.x oder Processing), und zeichnest Primitive (Würfel, Kugel,
Dreieck). Für Performance kannst du Geometrie einmal als **Chunk** (Display
List / Batched Mesh) backen und billig wieder verwenden. Mouse-Capture plus
Delta-Mausbewegung reicht für First-Person-Kamera.

---

## Fenster & Kamera

### `raum_erstelle` / `3d_create` / `re`

**Signatur**: `raum_erstelle(titel, breite, hoehe) → fenster`

### `raum_offen` / `3d_is_open`

**Signatur**: `raum_offen(win) → wahr/falsch`

### `raum_löschen` / `3d_clear`

**Signatur**: `raum_löschen(win, r, g, b)` (Farbkomponenten 0.0-1.0)

### `raum_aktualisieren` / `3d_update`, `raum_schliessen` / `3d_close`

**Signatur**: `raum_aktualisieren(win)` · `raum_schliessen(win)`

### `raum_perspektive` / `3d_perspective`

**Signatur**: `raum_perspektive(win, fov_grad, near, far)`

### `raum_kamera` / `3d_camera` / `rk`

**Signatur**: `raum_kamera(win, eye_x, eye_y, eye_z, ziel_x, ziel_y, ziel_z)`

## Transform-Stack

### `raum_push` · `raum_pop`

**Signatur**: `raum_push(win)` · `raum_pop(win)` — Matrix sichern/wiederherstellen.

### `raum_rotiere` / `3d_rotate`

**Signatur**: `raum_rotiere(win, winkel_grad, ax, ay, az)`

### `raum_verschiebe` / `3d_translate`

**Signatur**: `raum_verschiebe(win, dx, dy, dz)`

## Primitive

### `raum_würfel` / `3d_cube`

**Signatur**: `raum_würfel(win, x, y, z, groesse, farbe)`

### `raum_kugel` / `3d_sphere`

**Signatur**: `raum_kugel(win, x, y, z, radius, farbe, segmente)`

### `raum_dreieck` / `3d_triangle`

**Signatur**: `raum_dreieck(win, x1, y1, z1, x2, y2, z2, x3, y3, z3, farbe)`

## FPS-Input

### `raum_taste` / `3d_key_pressed`

**Signatur**: `raum_taste(win, taste) → wahr/falsch`

### `raum_maus_fangen` / `3d_capture_mouse`

**Signatur**: `raum_maus_fangen(win)` — relativer Mausmodus (FPS-Kamera).

### `raum_maus_dx`, `raum_maus_dy`

**Signatur**: `raum_maus_dx(win) → zahl` · `raum_maus_dy(win) → zahl`
**Zweck**: Relative Mausbewegung seit dem letzten Lesen (Raw-Mouse-Motion, consume-on-read).

### `raum_maus_freigeben`, `raum_maus_x/y/taste/rad`

**Signatur**: `raum_maus_freigeben(win)` · `raum_maus_x(win)` · `raum_maus_y(win)` · `raum_maus_taste(win, knopf)` · `raum_maus_rad(win)`
**Zweck**: Capture beenden bzw. absolute Position, Knopfstatus und Scrollrad abfragen.

## Licht, Material & Atmosphäre

| Builtin | Signatur | Zweck |
|---|---|---|
| `raum_licht` | `(win, an?)` | Beleuchtung ein/aus |
| `raum_umgebungslicht` | `(win, stärke)` | Ambient-Anteil |
| `raum_lichtfarbe` | `(win, r, g, b)` | Farbe der Lichtquelle |
| `raum_glanz` | `(win, stärke)` | Specular-Highlights (Glänzen) |
| `raum_tageszeit` | `(win, zeit)` | Tag-Nacht-Zyklus: Sonne/Farbstimmung animiert |
| `raum_nebel` | `(win, nah, fern)` | Distanz-Fog |
| `raum_nebel_farbe` | `(win, r, g, b)` | Fog-Farbe |
| `raum_löschen_farbe` / `raum_loeschen_farbe` | `(win, r, g, b)` | Clear-Farbe setzen (statt pro Frame in `raum_löschen`) |
| `raum_transparenz` | `(win, alpha)` | Alpha-Transparenz für folgende Primitive |
| `raum_wellen` | `(win, an?)` | Zeitanimierte Wasserwellen per Vertex-Displacement |
| `raum_dreieck_farben` | `(win, …koordinaten, f1, f2, f3)` | Gouraud-Dreieck mit per-Vertex-Farben |

## Test-Simulation & Screenshots

Für deterministische 3D-Tests (siehe [Test-API](test-api.md)): `raum_sim_taste(win, taste, zustand)` (Tri-State-Tastatur-Simulation), `raum_sim_maus_pos`, `raum_sim_maus_taste`, `raum_sim_maus_delta` (consume-on-read-Delta), `raum_sim_rad`, `raum_sim_reset` — sowie `raum_screenshot(win, pfad)` / `raum_screenshot_bmp` für Framebuffer-Aufnahmen.

## Chunk Display Lists

Geometrie einmal bauen, billig wiederholt zeichnen.

### `chunk_erstelle` / `chunk_create`

**Signatur**: `chunk_erstelle() → chunk_id`

### `chunk_beginne` · `chunk_ende`

**Signatur**: `chunk_beginne(chunk_id)` · `chunk_ende()`
**Zweck**: Zwischen den beiden Aufrufen gezeichnete Primitive werden in die Display-List aufgenommen.

### `chunk_zeichne` / `chunk_draw`

**Signatur**: `chunk_zeichne(chunk_id)`

### `chunk_lösche` / `chunk_delete`

**Signatur**: `chunk_lösche(chunk_id)`

## Beispiel — Rotierende Würfel (aus `beispiele/3d_demo.moo`)

```moo
setze win auf raum_erstelle("moo 3D Demo", 800, 600)
raum_perspektive(win, 45.0, 0.1, 100.0)

setze winkel auf 0.0
setze kamera_z auf 8.0

solange raum_offen(win):
    wenn raum_taste(win, "escape"):
        stopp

    raum_löschen(win, 0.05, 0.05, 0.15)
    raum_kamera(win, 0, 3, kamera_z, 0, 0, 0)

    raum_push(win)
    raum_rotiere(win, winkel, 1.0, 1.0, 0.0)
    raum_würfel(win, 0, 0, 0, 1.0, "rot")
    raum_pop(win)

    raum_aktualisieren(win)
    setze winkel auf winkel + 1.0
    warte(16)

raum_schliessen(win)
```

## Beispiel — Chunk-Mesh (aus `beispiele/welten.moo`)

```moo
funktion chunk_bauen(win, cx, cz):
    setze chunk auf chunk_erstelle()
    chunk_beginne(chunk)
    # ... raum_dreieck(...) viele Male ...
    chunk_ende()
    gib_zurück chunk

# Render-Loop:
chunk_zeichne(chunk_cache[key])
```
