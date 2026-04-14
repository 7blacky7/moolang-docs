# Installation

## Linux x64 (Alpha)

```sh
wget https://github.com/7blacky7/moolang-release/releases/latest/download/moolang-0.1.0-alpha-linux-x64.tar.gz
tar -xzf moolang-0.1.0-alpha-linux-x64.tar.gz
cd moolang-0.1.0-alpha-linux-x64
./install.sh                       # installiert SDL2, GLFW, OpenGL, curl, sqlite
./moo run beispiele/welten.moo     # startet das 3D-Welt-Beispiel
```

`install.sh` erkennt **Arch**, **Debian/Ubuntu** und **Fedora** automatisch und ruft den passenden Paketmanager auf.

## Windows & macOS

In Arbeit. Aktueller Build-Workflow unterstützt nur Linux x64.

Wer jetzt schon auf Windows/Mac bauen möchte: Source-Repo klonen und selbst kompilieren (siehe [Selbst bauen](#selbst-bauen)).

## Systemvoraussetzungen

Runtime-Bibliotheken (werden von `install.sh` installiert):

| Lib | Zweck |
|-----|-------|
| SDL2 + SDL2_image | 2D-Grafik, Sprites, Input |
| GLFW | 3D-Fenster |
| OpenGL 3.3+ | 3D-Rendering |
| curl | HTTP-Client |
| sqlite3 | Datenbank |

## Selbst bauen

Für eigene Compiler-Builds:

```sh
git clone https://github.com/7blacky7/moo
cd moo
# Mit mise (empfohlen):
mise run devenv
# Oder manuell:
cd compiler && cargo build --release --features gl33
```

Build-Voraussetzungen:

- **Rust 1.85+** (Edition 2024)
- **LLVM 18** (Header + `llvm-config` im `PATH`)
- **cc / gcc**
- **SDL2, GLFW, curl, sqlite3** als Development-Pakete

Das fertige Binary liegt unter `compiler/target/release/moo-compiler`.

## Erstes Programm

```moo
# hallo.moo
zeige "Hallo, Welt!"
```

```sh
./moo run hallo.moo         # direkt ausführen
./moo compile hallo.moo     # native Binary erzeugen
./moo repl                  # interaktiver Modus
```

Weiter mit dem [Tutorial](tutorial.md).
