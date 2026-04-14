# Grafik 3D

3D-Fenster, Kamera, Transform-Stack, Primitive, FPS-Input, Chunk-Display-Lists.
Runtime: OpenGL 3.3.

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
