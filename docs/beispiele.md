# Beispiele

Alle Beispiele liegen im Source-Repo unter [`beispiele/`](https://github.com/7blacky7/moo/tree/master/beispiele) — **jeder Link unten führt direkt zur Datei**. Die Beispiele sind Teil der Test-Gates, laufen also verifiziert.

!!! tip "Ausprobieren in 3 Befehlen"
    ```sh
    git clone https://github.com/7blacky7/moo && cd moo
    cd compiler && cargo build --release && cd ..
    ./compiler/target/release/moo-compiler run beispiele/pong.moo
    ```
    Voraussetzungen (Rust, LLVM 18): siehe [Installation](installation.md). Jedes Beispiel unten startet nach demselben Muster — Pfad austauschen, fertig.

## 3D-Welt — das Flaggschiff

[`welten.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/welten.moo) (~400 Zeilen) demonstriert fast die ganze Runtime:

- **Perlin Noise + fBm** für Terrain-Generierung
- **6 Biome**: Ozean, Strand, Wiese, Wald, Berg, Schnee
- **Flüsse** über Noise-Schwellwerte
- **First-Person-Kamera** mit Gravitation und Maus-Steuerung
- **Tag-Nacht-Zyklus** mit dynamischem Licht

Steuerung: `WASD` bewegen · Maus umsehen · `Leertaste` springen · `Escape` beenden.
Verwandt: [`voxel_sandbox.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/voxel_sandbox.moo) (Voxel-Engine).

## KI & LLM

| Beispiel | Was es zeigt |
|-----------|-----------|
| [`ki_kinderleicht.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ki_kinderleicht.moo) | Ein neuronales Netz in 5 Zeilen (XOR) — der Einstieg |
| [`ki_xor.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ki_xor.moo) | Dasselbe eine Ebene tiefer (Optimizer von Hand) |
| [`ki_mnist.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ki_mnist.moo) | Ziffern erkennen (MNIST) |
| [`ki_sprachmodell.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ki_sprachmodell.moo) | Ein kleines Sprachmodell trainieren (Transformer) |
| [`ki_moe.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ki_moe.moo) | Mixture-of-Experts mit Balance-Verlust |
| [`ki_mtp.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ki_mtp.moo) | MTP-Head + Speculative Decoding |
| [`ki_denken.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ki_denken.moo) | Reasoning-Modus mit Denk-Budget |
| [`ki_grpo.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ki_grpo.moo) | Reward-API + GRPO (Reinforcement Learning) |
| [`ki_safetensors_import.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ki_safetensors_import.moo) | Fremde safetensors-Modelle laden |
| [`neuralnet.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/neuralnet.moo) | Neural Net komplett von Hand (321 Zeilen — der Kontrast zur 5-Zeilen-API) |

## Natives UI

| Beispiel | Was es zeigt |
|-----------|-----------|
| [`ui_login_demo.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ui_login_demo.moo) | Login-Fenster aus fertigen Komponenten |
| [`ui_layout_demo.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ui_layout_demo.moo) | Zeilen/Spalten-Layout statt Pixel-Koordinaten |
| [`ui_binding_demo.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ui_binding_demo.moo) | Two-Way-Data-Binding (State ↔ Widgets) |
| [`ui_modular_app.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ui_modular_app.moo) | Größere App aus Setup-Bausteinen |
| [`ui_table_demo.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ui_table_demo.moo) · [`ui_file_browser_demo.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ui_file_browser_demo.moo) · [`ui_wizard_demo.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ui_wizard_demo.moo) | Tabellen, Datei-Browser, Wizard |
| [`ui_automation_demo.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ui_automation_demo.moo) · [`ui_snapshot_demo.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/ui_snapshot_demo.moo) | UI-Tests: Klicks per ID, Snapshots mit Sidecar |

## Kernel & Bootloader

| Beispiel | Was es zeigt |
|-----------|-----------|
| [`kernel/hallo_kern.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/kernel/hallo_kern.moo) | OS-Kernel in moo (x86_64, Multiboot2) |
| [`kernel/arm64_test.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/kernel/arm64_test.moo) | Derselbe Kernel-Baukasten auf ARM64 (qemu-virt) |
| [`bootloader/stage2.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/bootloader/stage2.moo) | Eigener Bootloader-Stage2 in moo |
| [`uefi/hallo_uefi.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/uefi/hallo_uefi.moo) | UEFI-App (PE32+) |
| [`domain/system/kernel_hello.moo`](https://github.com/7blacky7/moo/blob/master/beispiele/domain/system/kernel_hello.moo) | Kernel-Einstieg mit `--target x86_64-bare --kernel` |

## Spiele

| Kategorie | Beispiele |
|-----------|-----------|
| Klassiker | [`pong`](https://github.com/7blacky7/moo/blob/master/beispiele/pong.moo), [`snake`](https://github.com/7blacky7/moo/blob/master/beispiele/snake.moo), [`tetris`](https://github.com/7blacky7/moo/blob/master/beispiele/tetris.moo), [`breakout`](https://github.com/7blacky7/moo/blob/master/beispiele/breakout.moo), [`invaders`](https://github.com/7blacky7/moo/blob/master/beispiele/invaders.moo), [`pacman`](https://github.com/7blacky7/moo/blob/master/beispiele/pacman.moo), [`asteroids`](https://github.com/7blacky7/moo/blob/master/beispiele/asteroids.moo), [`galaga`](https://github.com/7blacky7/moo/blob/master/beispiele/galaga.moo), [`frogger`](https://github.com/7blacky7/moo/blob/master/beispiele/frogger.moo), [`defender`](https://github.com/7blacky7/moo/blob/master/beispiele/defender.moo), [`game_2048`](https://github.com/7blacky7/moo/blob/master/beispiele/game_2048.moo), [`wordle`](https://github.com/7blacky7/moo/blob/master/beispiele/wordle.moo) |
| Puzzle | [`sokoban`](https://github.com/7blacky7/moo/blob/master/beispiele/sokoban.moo), [`minesweeper`](https://github.com/7blacky7/moo/blob/master/beispiele/minesweeper.moo), [`sudoku`](https://github.com/7blacky7/moo/blob/master/beispiele/sudoku.moo), [`mastermind`](https://github.com/7blacky7/moo/blob/master/beispiele/mastermind.moo), [`match3`](https://github.com/7blacky7/moo/blob/master/beispiele/match3.moo), [`columns`](https://github.com/7blacky7/moo/blob/master/beispiele/columns.moo), [`bubble_shooter`](https://github.com/7blacky7/moo/blob/master/beispiele/bubble_shooter.moo), [`lights_out`](https://github.com/7blacky7/moo/blob/master/beispiele/lights_out.moo), [`connect4`](https://github.com/7blacky7/moo/blob/master/beispiele/connect4.moo) |
| Action | [`bomberman`](https://github.com/7blacky7/moo/blob/master/beispiele/bomberman.moo), [`platformer`](https://github.com/7blacky7/moo/blob/master/beispiele/platformer.moo), [`brawler`](https://github.com/7blacky7/moo/blob/master/beispiele/brawler.moo), [`fighter`](https://github.com/7blacky7/moo/blob/master/beispiele/fighter.moo), [`space_shooter`](https://github.com/7blacky7/moo/blob/master/beispiele/space_shooter.moo), [`helicopter`](https://github.com/7blacky7/moo/blob/master/beispiele/helicopter.moo), [`artillery`](https://github.com/7blacky7/moo/blob/master/beispiele/artillery.moo) |
| Strategie | [`tower_defense`](https://github.com/7blacky7/moo/blob/master/beispiele/tower_defense.moo), [`strategie`](https://github.com/7blacky7/moo/blob/master/beispiele/strategie.moo), [`siedler`](https://github.com/7blacky7/moo/blob/master/beispiele/siedler.moo), [`td_procgen`](https://github.com/7blacky7/moo/blob/master/beispiele/td_procgen.moo), [`schach`](https://github.com/7blacky7/moo/blob/master/beispiele/schach.moo), [`city_builder/`](https://github.com/7blacky7/moo/tree/master/beispiele/city_builder) |
| RPG/Adventure | [`zelda`](https://github.com/7blacky7/moo/blob/master/beispiele/zelda.moo) **(Referenz-Beispiel: 5 Räume, Boss, headless Selftest)**, [`adventure`](https://github.com/7blacky7/moo/blob/master/beispiele/adventure.moo) *(repariert, mit Selftest)*, [`dungeon`](https://github.com/7blacky7/moo/blob/master/beispiele/dungeon.moo) *(in Reparatur)*, [`survival`](https://github.com/7blacky7/moo/blob/master/beispiele/survival.moo), [`farm`](https://github.com/7blacky7/moo/blob/master/beispiele/farm.moo) |
| Tech-Demos | [`rpg_world`](https://github.com/7blacky7/moo/blob/master/beispiele/rpg_world.moo) *(bewusst ohne Spielziel — Welt-Rendering-Demo)* |
| Simulation | [`racing`](https://github.com/7blacky7/moo/blob/master/beispiele/racing.moo), [`ski`](https://github.com/7blacky7/moo/blob/master/beispiele/ski.moo), [`pinball`](https://github.com/7blacky7/moo/blob/master/beispiele/pinball.moo), [`golf`](https://github.com/7blacky7/moo/blob/master/beispiele/golf.moo), [`flappy`](https://github.com/7blacky7/moo/blob/master/beispiele/flappy.moo), [`doodle_jump`](https://github.com/7blacky7/moo/blob/master/beispiele/doodle_jump.moo) |

## Utilities & Systemnah

| Kategorie | Beispiele |
|-----------|-----------|
| Daten | [`mini_db`](https://github.com/7blacky7/moo/blob/master/beispiele/domain/db/mini_db.moo), [`mini_sql`](https://github.com/7blacky7/moo/blob/master/beispiele/domain/db/mini_sql.moo), [`mini_redis/`](https://github.com/7blacky7/moo/tree/master/beispiele/mini_redis), [`mqtt_broker`](https://github.com/7blacky7/moo/blob/master/beispiele/mqtt_broker.moo), [`mysql_client`](https://github.com/7blacky7/moo/blob/master/beispiele/domain/db/mysql_client.moo), [`postgres_client`](https://github.com/7blacky7/moo/blob/master/beispiele/domain/db/postgres_client.moo), [`redis_client`](https://github.com/7blacky7/moo/blob/master/beispiele/domain/db/redis_client.moo) |
| Netz | [`http_api`](https://github.com/7blacky7/moo/blob/master/beispiele/domain/web/http_api.moo), [`websocket_server`](https://github.com/7blacky7/moo/blob/master/beispiele/domain/web/websocket_server.moo), [`dns_resolver`](https://github.com/7blacky7/moo/blob/master/beispiele/dns_resolver.moo), [`proxy`](https://github.com/7blacky7/moo/blob/master/beispiele/domain/web/proxy.moo), [`chat/`](https://github.com/7blacky7/moo/tree/master/beispiele/chat) |
| Parser/Sprachen | [`mini_lisp`](https://github.com/7blacky7/moo/blob/master/beispiele/mini_lisp.moo), [`bf_interp`](https://github.com/7blacky7/moo/blob/master/beispiele/bf_interp.moo), [`regex_engine`](https://github.com/7blacky7/moo/blob/master/beispiele/regex_engine.moo), [`datalog`](https://github.com/7blacky7/moo/blob/master/beispiele/datalog.moo), [`sat_solver`](https://github.com/7blacky7/moo/blob/master/beispiele/sat_solver.moo), [`stackvm`](https://github.com/7blacky7/moo/blob/master/beispiele/stackvm.moo), [`json_schema`](https://github.com/7blacky7/moo/blob/master/beispiele/json_schema.moo) |
| Encoding | [`png_encoder`](https://github.com/7blacky7/moo/blob/master/beispiele/png_encoder.moo), [`gif_encoder`](https://github.com/7blacky7/moo/blob/master/beispiele/gif_encoder.moo), [`elf_reader`](https://github.com/7blacky7/moo/blob/master/beispiele/domain/system/elf_reader.moo), [`tar_reader`](https://github.com/7blacky7/moo/blob/master/beispiele/domain/system/tar_reader.moo), [`x86dis`](https://github.com/7blacky7/moo/blob/master/beispiele/domain/system/x86dis.moo), [`midi_player`](https://github.com/7blacky7/moo/blob/master/beispiele/midi_player.moo) |
| Content | [`blog_engine`](https://github.com/7blacky7/moo/blob/master/beispiele/domain/db/blog_engine.moo), [`markdown_cms`](https://github.com/7blacky7/moo/blob/master/beispiele/markdown_cms.moo), [`md_to_pdf`](https://github.com/7blacky7/moo/blob/master/beispiele/md_to_pdf.moo) |
| Math/Physik | [`astar`](https://github.com/7blacky7/moo/blob/master/beispiele/astar.moo), [`raytracer/`](https://github.com/7blacky7/moo/tree/master/beispiele/raytracer), [`partikel`](https://github.com/7blacky7/moo/blob/master/beispiele/partikel.moo), [`physik`](https://github.com/7blacky7/moo/blob/master/beispiele/physik.moo) |

## Code-Umfang

134 Beispiele, die meisten unter 500 Zeilen. Lies dir ein paar durch — das ist der schnellste Weg, die Sprache zu lernen.
