# Welt-Engine

## Was ist das?

Die Welt-Engine (Voxel/Terrain World Engine) ist eine fertige Mini-Minecraft-
bzw. Open-World-Runtime: mit wenigen Zeilen bekommst du eine prozedural
generierte 3D-Welt mit Terrain, Biomen, Bäumen, Nebel, beweglicher Sonne und
Tageszeit sowie einer First-Person-Kamera. Die Generierung basiert auf
Perlin-Noise und ist durch einen Seed deterministisch — gleicher Seed liefert
dieselbe Welt. Anders als das rohe 3D-Modul musst du hier keine Dreiecke selbst
platzieren; das Modul kümmert sich um Chunks, Rendering, Kollisions-ähnliche
Höhenabfragen und Steuerung. Ideal für Prototypen, Spiele-Experimente oder
einfach zum Reinlaufen.

---

`importiere welt` lädt `stdlib/welt.moo`, das die `__welt_*`-Runtime-Bindings verkapselt.

## Nutzung

```moo
importiere welt
```

## Kern-Funktionen

### `welt_erstelle` / `world_create`

**Signatur**: `welt_erstelle(titel, breite, hoehe) → welt`

### `welt_offen` / `world_is_open`

**Signatur**: `welt_offen(w) → wahr/falsch`

### `welt_aktualisieren` / `world_update`

**Signatur**: `welt_aktualisieren(w)` — Input, Physik, Rendering, Frame-Swap.

### `welt_beenden` / `world_close`

**Signatur**: `welt_beenden(w)`

## Konfiguration

### `welt_seed` / `world_seed`

**Signatur**: `welt_seed(w, seed)` — deterministische Welt-Generierung.

### `welt_biom` / `world_biome`

**Signatur**: `welt_biom(w, name, h_min, h_max, farbe, baeume)`

### `welt_sonne` / `world_sun`

**Signatur**: `welt_sonne(w, x, y, z)` — Sonnenrichtung (Licht).

### `welt_nebel` / `world_fog`

**Signatur**: `welt_nebel(w, distanz)`

### `welt_meeresspiegel` / `world_sea_level`

**Signatur**: `welt_meeresspiegel(w, hoehe)`

### `welt_render_distanz` / `world_render_dist`

**Signatur**: `welt_render_distanz(w, distanz)` (in Chunks)

### `welt_tageszeit` / `world_time_of_day`

**Signatur**: `welt_tageszeit(w, zeit)` (0.0–1.0)

### `welt_baeume` / `world_trees`

**Signatur**: `welt_baeume(w, biom_name, chance)`
**Zweck**: Baum-Dichte pro Biom setzen (`chance` 0.0–1.0). Wrapper um die
Runtime-Builtin `__welt_baeume` / `__world_trees`.

## Beleuchtung (Backend-intern)

Die Welt-Engine delegiert die eigentliche Szenenbeleuchtung an das aktive
3D-Backend (`moo_3d_backend.h`: `set_light_dir`, `set_ambient`, `set_fog_density`).
Du steuerst sie **nicht** direkt über einzelne `welt_ambient`- oder
`welt_licht_*`-Funktionen, sondern indirekt über:

- `welt_sonne(w, x, y, z)` — Basisrichtung der Sonne (Vektor, darauf setzt die
  Engine auf).
- `welt_tageszeit(w, zeit)` — treibt pro Frame automatisch die Backend-Hooks
  `set_light_dir` (Sonnenrichtung aus Tageszeit-Winkel) und `set_ambient`
  (Umgebungslicht-Level `0.02–0.20` abhängig vom Tages-Faktor). So werden
  Nacht/Morgen/Mittag/Abend ohne zusätzlichen User-Code korrekt beleuchtet.
- `welt_nebel(w, distanz)` — ruft backend-intern `set_fog_density`.

Die Sonne wird zusätzlich als sichtbare Kugel gerendert und ihre Farbe aus
der Tageszeit abgeleitet (`#FFFFCC` Mittag, `#FF8C00` Morgen, `#FF4500` Abend,
`#FF6B35` Dämmerung). Wenn du rohe Kontrolle über `set_light_dir` oder
`set_ambient` brauchst, arbeite nicht mit der Welt-Engine, sondern direkt mit
dem 3D-Modul (`raum_*`).

## Abfragen

### `welt_hoehe_bei` / `world_height_at`

**Signatur**: `welt_hoehe_bei(w, x, z) → zahl` — Terrain-Höhe an Weltkoordinate.

## Vollständiges Beispiel (aus `beispiele/welt_test.moo`)

```moo
importiere welt

setze w auf welt_erstelle("moo Welt Test", 1024, 768)
welt_seed(w, 42)
welt_render_distanz(w, 20)
welt_nebel(w, 0.003)

solange welt_offen(w):
    welt_aktualisieren(w)

welt_beenden(w)
```
