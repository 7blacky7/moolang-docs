# Welt-Engine

High-Level-Modul für prozedurale 3D-Welten (Terrain, Biome, Bäume, Nebel, Sonne,
Tageszeit) mit eingebauter FPS-Kamera. Wrapper-Modul — `importiere welt` lädt
`stdlib/welt.moo`, das die `__welt_*`-Runtime-Bindings verkapselt.

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

### `__welt_baeume` / `__world_trees`

**Signatur**: `__welt_baeume(w, biom_name, chance)`
**Zweck**: Baum-Dichte pro Biom setzen (`chance` 0.0–1.0). Hinweis: Derzeit
**kein** `welt_baeume`-Wrapper in `stdlib/welt.moo` — nur direkter Aufruf der
internen Builtin-Funktion (Prefix `__`) möglich, bis `stdlib/welt.moo` erweitert
wird.

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
