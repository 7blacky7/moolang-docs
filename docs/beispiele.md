# Beispiele

Alle Beispiele liegen im Source-Repo: <https://github.com/7blacky7/moo/tree/master/beispiele>

Verifiziert im Alpha-Bundle: **`welten.moo`** (3D-Welt).
Weitere folgen in kommenden Releases, sobald plattformübergreifend verifiziert.

## 3D-Welt — das Flaggschiff

`welten.moo` (~400 Zeilen) demonstriert fast die ganze Runtime:

- **Perlin Noise + fBm** für Terrain-Generierung
- **6 Biome**: Ozean, Strand, Wiese, Wald, Berg, Schnee
- **Flüsse** über Noise-Schwellwerte
- **First-Person-Kamera** mit Gravitation und Maus-Steuerung
- **Tag-Nacht-Zyklus** mit dynamischem Licht

Steuerung: `WASD` bewegen · Maus umsehen · `Leertaste` springen · `Escape` beenden.

## Kategorien

### Spiele (nicht im Bundle, im Repo)

| Kategorie | Beispiele |
|-----------|-----------|
| Klassiker | `pong`, `snake`, `tetris`, `breakout`, `invaders`, `pacman`, `asteroids`, `galaga`, `frogger`, `defender` |
| Puzzle | `sokoban`, `minesweeper`, `sudoku`, `mastermind`, `match3`, `columns`, `bubble_shooter`, `lights_out`, `connect4` |
| Action | `bomberman`, `platformer`, `brawler`, `fighter`, `space_shooter`, `helicopter`, `artillery` |
| Strategie | `tower_defense`, `strategie`, `siedler`, `td_procgen` |
| RPG/Adventure | `zelda`, `adventure`, `rpg_world`, `dungeon`, `survival`, `farm` |
| Simulation | `racing`, `ski`, `pinball`, `golf`, `flappy`, `doodle_jump` |

### Utilities & Systemnah

| Kategorie | Beispiele |
|-----------|-----------|
| Daten | `mini_db`, `mini_sql`, `mini_redis`, `mqtt_broker`, `mysql_client`, `postgres_client`, `redis_client` |
| Netz | `http_api`, `websocket_server`, `dns_resolver`, `proxy`, `chat/` |
| Parser/Sprachen | `mini_lisp`, `bf_interp`, `regex_engine`, `datalog`, `sat_solver`, `stackvm`, `json_schema` |
| Encoding | `png_encoder`, `gif_encoder`, `elf_reader`, `tar_reader`, `x86dis`, `midi_player` |
| Content | `blog_engine`, `markdown_cms`, `md_to_pdf` |
| KI/Math | `neuralnet`, `astar`, `raytracer`, `partikel`, `physik` |

## Code-Umfang

126+ Beispiele, die meisten unter 500 Zeilen. Lies dir ein paar durch — das ist der schnellste Weg, die Sprache zu lernen.

```sh
# Lokales Browsen:
git clone https://github.com/7blacky7/moo
ls moo/beispiele/

# Eines ausführen:
./moo run moo/beispiele/pong.moo
```
