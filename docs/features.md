# Features

moolang ist **mehr als 3D** — eine vollständige Sprache mit breiter Runtime.

## Sprache

- **Zweisprachig** — Deutsch (`setze`, `solange`, `wenn`) und Englisch (`set`, `while`, `if`) gemischt benutzbar
- **Statische Kompilierung** über LLVM 18 zu nativem Code — keine VM, kein GC-Pause
- **Typen**: Zahl, Text, Boolean, Liste, Dictionary, Lambda, Objekt, Nichts
- **Kontrollfluss**: `wenn`/`sonst`, `solange`, `für`, `match`/`fall`, `versuche`/`fange`
- **Funktionen**: Default-Parameter, Lambdas, Pipes, List Comprehensions, Optional Chaining (`?.`), Nullish Coalescing (`??`), Spread-Operator
- **OOP**: Klassen, Vererbung, Interfaces
- **Module**: Import-System mit Diamond-Resolution, selektive Imports (`aus X importiere Y, Z`)
- **Paketverwaltung**: `moo paket install <name>` — aus `github.com/moo-packages/<name>`

## Standardbibliothek

Eingebaute Module:

| Modul | Zweck |
|-------|-------|
| `mathe` | Sinus, Cosinus, Wurzel, Logarithmus, Fakultät, Primzahlen |
| `liste` | Filter, Map, Reduce, Sort, Unique, Flatten |
| `text` | Split, Join, Trim, Case, Regex-Convenience |
| `welt` | Perlin-Noise, 3D-Terrain, Chunks, Physik |
| `primzahl` | Primzahl-Tests, Faktorisierung |

## Runtime (in jedem Binary eingebaut)

| Bereich | APIs |
|---------|------|
| [2D-Grafik](runtime/grafik.md) | Fenster, Sprites, Tileset-Animation, Input, Maus |
| [3D-Grafik](runtime/3d.md) | OpenGL 3.3, Kamera, Meshes, Licht, Tag-Nacht, Welt-Engine |
| [JSON](runtime/json.md) | `json_lesen`, `json_text`, Pretty-Print |
| [HTTP & Netz](runtime/http.md) | HTTP-Client, WebSocket-Server, TCP-Sockets, MQTT |
| [Datenbank](runtime/datenbank.md) | SQLite eingebaut, Mini-SQL-Engine, externe Clients |
| [Kryptografie](runtime/krypto.md) | SHA-256/512, MD5, HMAC, Base64, secure-random, Sanitizing |
| [Threads](runtime/threads.md) | pthread-Threads, Channels (Go-Stil), Mutex |
| Dateien | Lesen, Schreiben, Listing, Existence, Permissions |
| Regex | POSIX-Regex-Engine |
| Audio | MIDI-Player, Synth (über Beispiele) |

## Tooling

- **REPL**: `moo repl` — interaktiver Modus mit History
- **Nativer Compiler**: `moo compile datei.moo` → ELF/PE/Mach-O
- **Cross-Compilation**: `moo compile ... --target wasm32` (WASM), ARM, RISC-V
- **Bare-Metal**: `--no-stdlib` + `--linker-script` für Kernel-Entwicklung
- **Profiling**: `--profile` — Zeit pro Funktion
- **LSP**: Syntax-Diagnostics + Keyword-Completion in VS Code

## Was es (noch) nicht gibt

- Kein Typsystem (dynamisch typisiert)
- Kein Rename-Refactoring im LSP
- Kein Paket-Registry (nur git-clone)
- Keine Async/Await (Threads + Channels stattdessen)
- Keine Generics

Für einen Eindruck der Breite: **126+ Beispiele** im [Source-Repo](https://github.com/7blacky7/moo/tree/master/beispiele), vom Pong über Mini-SQL-Engine und Neural Net bis hin zum Raytracer und X86-Disassembler — alles in moolang geschrieben.
