# moolang

!!! warning "Alpha-Version"
    Name und Dateiendung sind **noch nicht final**. `moolang` ist ein Platzhalter — die finale Bezeichnung wird vor v1.0 festgelegt.

**moolang** ist eine Programmiersprache auf **Deutsch** (mit Englisch-Aliases), die direkt zu **nativen Binaries** kompiliert wird — via LLVM 18. Mit breiter eingebauter Runtime: 2D/3D-Grafik, HTTP, WebSockets, SQLite, Kryptografie, Threads, Regex, JSON — alles ohne externe Pakete.

## Ein Programm

```moo
zeige "Hallo, Welt!"

funktion fakultät(n):
    wenn n <= 1:
        gib_zurück 1
    gib_zurück n * fakultät(n - 1)

zeige fakultät(10)
```

## In 30 Sekunden loslegen

```sh
wget https://github.com/7blacky7/moolang-release/releases/latest/download/moolang-0.1.0-alpha-linux-x64.tar.gz
tar -xzf moolang-0.1.0-alpha-linux-x64.tar.gz
cd moolang-0.1.0-alpha-linux-x64
./install.sh
./moo repl
```

## Was du damit bauen kannst

<div class="grid cards" markdown>

-   :material-server-network: **Web-Backends**

    HTTP-Server, WebSocket-Server, JSON-APIs, Datenbank-Anbindung — alles eingebaut. Siehe `beispiele/blog_engine.moo`, `chat/`, `http_api.moo`.

-   :material-database: **Daten-Tools**

    SQLite direkt. Mini-SQL-Engine, Mini-DB, CSV/JSON-Parser in moolang selbst geschrieben (`mini_sql.moo`, `mini_db.moo`).

-   :material-gamepad-variant: **2D-Spiele**

    Sprites, Tilesets, Input, Kollision — SDL2 eingebaut. Pong, Snake, Tetris, Zelda, Platformer bereits als Beispiele.

-   :material-cube-outline: **3D-Welten**

    OpenGL 3.3, Kamera, Meshes, Licht, Tag-Nacht-Zyklus. Inkl. Welt-Engine mit Perlin-Noise + Biomen (`welten.moo`).

-   :material-security: **Krypto & Sicherheit**

    SHA-256/512, HMAC, Base64, sichere Zufallszahlen, HTML/SQL-Sanitizing.

-   :material-parser: **Compiler & Parser**

    Eigene Mini-Sprachen bauen: Mini-Lisp, BF-Interpreter, Regex-Engine, StackVM, SAT-Solver als Beispiele.

-   :material-brain: **KI & Numerik**

    Neural Net, A*, Raytracer, Partikel-Simulation — alles in moolang. Siehe `neuralnet.moo`, `raytracer/`, `astar.moo`.

-   :material-content-save-cog: **System-Tools**

    ELF-Reader, Tar-Parser, X86-Disassembler, GIF/PNG-Encoder, DNS-Resolver — Zugriff bis auf Bit-Ebene.

-   :material-cpu-64-bit: **Bare-Metal & WASM**

    `--no-stdlib` für Kernel-Entwicklung, `--target wasm32` für Browser. Kein libc-Zwang.

</div>

## Warum moolang?

- **Low Ceremony** — kein `public static void main`, kein Cargo.toml, kein Webpack. Du schreibst `zeige "Hallo"` und tippst `moo run`.
- **Batteries included** — HTTP, DB, Crypto, Threads, 2D/3D sind Teil der Runtime, keine 500 Dependencies.
- **Nativ kompiliert** — LLVM macht Binaries. Keine VM, kein JIT, kein GC-Pause-Problem.
- **Zweisprachig** — Deutsch für Anfänger, Englisch für den Rest. Mischbar in einer Datei.

## Wohin als Nächstes?

- [Installation](installation.md) — Download und erste Schritte
- [Features](features.md) — vollständige Feature-Übersicht
- [Tutorial](tutorial.md) — Schritt für Schritt von Variable bis 3D-Welt (993 Zeilen)
- [Sprache](sprache/grundlagen.md) — Syntax-Referenz
- [Runtime-APIs](runtime/grafik.md) — Grafik, Netz, DB, Krypto, Threads
- [Beispiele](beispiele.md) — 126+ Programme zum Durchstöbern
- [VS Code](editor.md) — Editor-Integration

## Status

| Bereich | Stand |
|---------|-------|
| Compiler (Rust + LLVM 18) | Stabil |
| Runtime (C11) | Stabil |
| Stdlib (`liste`, `mathe`, `welt` …) | Basis vorhanden |
| Paketmanager | Minimal (git-clone) |
| LSP (VS Code) | Syntax-Level, kein Typsystem |
| Linux x64 Release | ✅ |
| Windows Release | In Arbeit |
| macOS Release | In Arbeit |
| Finaler Name | ⏳ noch nicht entschieden |
