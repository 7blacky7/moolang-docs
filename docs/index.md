# moolang

!!! warning "Alpha-Version"
    Name und Dateiendung sind **noch nicht final**. `moolang` ist ein Platzhalter — die finale Bezeichnung wird vor v1.0 festgelegt.

**moolang** ist eine Programmiersprache auf **Deutsch** (mit Englisch-Aliases), die direkt zu **nativen Binaries** kompiliert wird — via LLVM.

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
./moo run beispiele/welten.moo
```

## Was drin ist

<div class="grid cards" markdown>

-   :material-cube-outline: **2D & 3D Grafik**

    SDL2 für Sprites, OpenGL 3.3 für 3D — eingebaut in der Runtime.

-   :material-earth: **Prozedurale Welten**

    Perlin-Noise, Biome, First-Person-Kamera, Tag-Nacht-Zyklus.

-   :material-network: **Netzwerk**

    HTTP-Client, WebSocket-Server, TCP-Sockets, MQTT.

-   :material-database: **Persistenz**

    SQLite, JSON, Dateien, Kryptografie — alles ohne externe Crates.

-   :material-translate: **Zweisprachig**

    Schreib `setze x auf 5` oder `set x to 5` — beides funktioniert.

-   :material-rocket-launch: **Native Binaries**

    Per LLVM kompiliert, keine VM, keine Runtime-Dependencies zur Compile-Zeit.

</div>

## Wohin als Nächstes?

- [Installation](installation.md) — Download + erste Schritte
- [Tutorial](tutorial.md) — Von `zeige "Hallo"` bis 3D-Welt
- [Sprache](sprache/grundlagen.md) — Referenz aller Konstrukte
- [Beispiele](beispiele.md) — 126+ Programme zum Durchstöbern
- [VS Code](editor.md) — Syntax-Highlighting + LSP einrichten

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
